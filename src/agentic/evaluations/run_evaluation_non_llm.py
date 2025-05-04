"""
This module contains the evaluation functions for the Agentic Graph.
It includes functions to evaluate the performance of the model on various tasks.
"""

import json
import time
from datetime import datetime

import phoenix as px
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from phoenix.experiments import run_experiment
from phoenix.experiments.types import Example
from phoenix.otel import register

from agentic.agents.agent_factory import create_default_character, create_mage_character
from agentic.evaluators.evaluators import (
    create_conciseness_judge,
    create_roleplay_judge,
    evaluate_conciseness,
    evaluate_roleplay,
)

client = px.Client()
tracer_provider = register(
    project_name="evaluation-demo",
    endpoint="http://0.0.0.0:6006/v1/traces",
    auto_instrument=True,
)

tracer = tracer_provider.get_tracer(__name__)


def evaluate_default_roleplay():

    dataset = client.get_dataset(
        name="default_character",
        version_id="RGF0YXNldFZlcnNpb246Mw==",
    )

    @tracer.chain
    def run_roleplay(example: Example) -> dict:
        """Roleplay Evaluator based on LLMs as Judge"""

        human_question = example.input["user_query"]
        reference_answer = example.output["expected_response"]
        default_character_agent = create_default_character()

        # Build the required LangGraph agent state
        state = {
            "msgs": [HumanMessage(content=human_question)],
        }

        response = default_character_agent.invoke(state)

        return {
            "user_query": human_question,
            "reference_answer": reference_answer,
            "llm_answer": response,
        }

    # Define an evaluator. This just an example.
    @tracer.chain
    def roleplay_evaluator(output) -> float:
        """Evaluate the roleplay of the response"""

        # print("=" * 20)
        # print(f"Evaluating Roleplay: {output['llm_answer']}")
        # print(f"Reference Answer: {output['reference_answer']}")
        # print(f"User Query: {output['user_query']}")

        chain_roleplay = create_roleplay_judge()
        response = evaluate_roleplay(
            chain_roleplay,
            "default",
            output["user_query"],
            output["reference_answer"],
            output["llm_answer"],
        )

        print("=" * 20)
        print(f"Response Roleplay Evaluator\n: {response}")

        try:
            json_obj = json.loads(response)
            return float(json_obj["score"])
        except Exception as e:
            print(f"Error parsing response: {response}")
            print(f"Exception: {e}")
            # Fallback to returning 0.0 in case of parsing error
            return 0.0

    # Store the evaluators for later use
    evaluators = [roleplay_evaluator]

    # Run an experiment
    experiment = run_experiment(dataset, run_roleplay, evaluators=evaluators)


def evaluate_mage_roleplay():

    dataset = client.get_dataset(
        name="mage_character",
        version_id="RGF0YXNldFZlcnNpb246NA==",
    )

    @tracer.chain
    def run_roleplay(example: Example) -> dict:
        """Roleplay Evaluator based on LLMs as Judge"""

        human_question = example.input["user_query"]
        reference_answer = example.output["expected_response"]
        mage_character_agent = create_mage_character()

        # Build the required LangGraph agent state
        state = {
            "msgs": [HumanMessage(content=human_question)],
        }

        response = mage_character_agent.invoke(state)

        return {
            "user_query": human_question,
            "reference_answer": reference_answer,
            "llm_answer": response,
        }

    # Define an evaluator. This just an example.
    @tracer.chain
    def roleplay_evaluator(output) -> float:
        """Evaluate the roleplay of the response"""

        # print("=" * 20)
        # print(f"Evaluating Roleplay: {output['llm_answer']}")
        # print(f"Reference Answer: {output['reference_answer']}")
        # print(f"User Query: {output['user_query']}")

        chain_roleplay = create_roleplay_judge()
        response = evaluate_roleplay(
            chain_roleplay,
            "mage",
            output["user_query"],
            output["reference_answer"],
            output["llm_answer"],
        )

        print("=" * 20)
        print(f"Response Roleplay Evaluator\n: {response}")

        try:
            json_obj = json.loads(response)
            return float(json_obj["score"])
        except Exception as e:
            print(f"Error parsing response: {response}")
            print(f"Exception: {e}")
            # Fallback to returning 0.0 in case of parsing error
            return 0.0

    # Store the evaluators for later use
    evaluators = [roleplay_evaluator]

    # Run an experiment
    experiment = run_experiment(dataset, run_roleplay, evaluators=evaluators)


if __name__ == "__main__":
    # evaluate_default_roleplay()
    evaluate_mage_roleplay()
