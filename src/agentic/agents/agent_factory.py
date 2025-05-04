import os

import phoenix as px
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from phoenix.otel import register

from agentic.prompts.default_character import DEFAULT_CHARACTER_SYSTEM_PROMPT_TEMPLATE
from agentic.prompts.mage_character import MAGE_CHARACTER_SYSTEM_PROMPT_TEMPLATE

load_dotenv()

client = px.Client()
tracer_provider = register(
    project_name="evaluation-demo",
    endpoint="http://0.0.0.0:6006/v1/traces",
    auto_instrument=True,
)

tracer = tracer_provider.get_tracer(__name__)


@tracer.chain
def create_default_character():

    prompt_template = ChatPromptTemplate(
        [
            ("system", DEFAULT_CHARACTER_SYSTEM_PROMPT_TEMPLATE),
            MessagesPlaceholder("msgs"),
        ]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=os.getenv("gemini_api_key"),
        temperature=0,
        max_tokens=50,
    )
    chain = prompt_template | llm | StrOutputParser()
    return chain


@tracer.chain
def create_mage_character():

    prompt_template = ChatPromptTemplate(
        [
            ("system", MAGE_CHARACTER_SYSTEM_PROMPT_TEMPLATE),
            MessagesPlaceholder("msgs"),
        ]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=os.getenv("gemini_api_key"),
        temperature=0,
        max_tokens=50,
    )
    chain = prompt_template | llm | StrOutputParser()
    return chain
