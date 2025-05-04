import os

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from agentic.prompts.default_character import DEFAULT_CHARACTER_SYSTEM_PROMPT_TEMPLATE
from agentic.prompts.mage_character import MAGE_CHARACTER_SYSTEM_PROMPT_TEMPLATE


load_dotenv()


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

