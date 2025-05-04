import os

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from phoenix.otel import register

from agentic.prompts.judge_conciseness_prompt import (
    CONCISENESS_EVALUATION_TEMPLATE,
    CONCISENESS_JUDGE_SYSTEM_PROMPT,
)
from agentic.prompts.judge_roleplay_prompt import (
    ROLEPLAY_EVALUATION_TEMPLATE,
    ROLEPLAY_JUDGE_SYSTEM_PROMPT,
)

load_dotenv()

tracer_provider = register(
    project_name="evaluation-demo",
    endpoint="http://0.0.0.0:6006/v1/traces",
    auto_instrument=True,
)

tracer = tracer_provider.get_tracer(__name__)


@tracer.chain
def create_conciseness_judge():
    prompt_template = ChatPromptTemplate(
        [
            ("system", CONCISENESS_JUDGE_SYSTEM_PROMPT),
            ("human", CONCISENESS_EVALUATION_TEMPLATE),
        ]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=os.getenv("gemini_api_key"),
        temperature=0,
        max_tokens=200,
    )
    chain = prompt_template | llm | StrOutputParser()
    return chain


@tracer.chain
def create_roleplay_judge():
    prompt_template = ChatPromptTemplate(
        [
            ("system", ROLEPLAY_JUDGE_SYSTEM_PROMPT),
            ("human", ROLEPLAY_EVALUATION_TEMPLATE),
        ]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=os.getenv("gemini_api_key"),
        temperature=0,
        max_tokens=200,
    )
    chain = prompt_template | llm | StrOutputParser()
    return chain


@tracer.chain
def evaluate_conciseness(judge_chain, question, response, reference_answer):
    """
    Evaluate the conciseness of a response using the judge chain

    Args:
        judge_chain: The conciseness judge chain
        question: The user query
        response: The AI response to evaluate
        reference_answer: The reference answer from the golden dataset

    Returns:
        The evaluation result
    """
    result = judge_chain.invoke(
        {
            "question": question,
            "response": response,
            "reference_answer": reference_answer,
        }
    )
    return result


@tracer.chain
def evaluate_roleplay(
    judge_chain, character_type, question, response, reference_answer
):
    """
    Evaluate the roleplay quality of a response using the judge chain

    Args:
        judge_chain: The roleplay judge chain
        character_type: The type of character (e.g., "mage", "default")
        question: The user query
        response: The AI response to evaluate
        reference_answer: The reference answer from the golden dataset

    Returns:
        The evaluation result
    """
    result = judge_chain.invoke(
        {
            "character_type": character_type,
            "question": question,
            "response": response,
            "reference_answer": reference_answer,
        }
    )
    return result
