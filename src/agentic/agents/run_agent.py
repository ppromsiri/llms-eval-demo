import phoenix as px
from langchain_core.messages import HumanMessage
from phoenix.otel import register

from agentic.agents.agent_factory import create_default_character, create_mage_character

client = px.Client()
tracer_provider = register(
    project_name="evaluation-demo",
    endpoint="http://0.0.0.0:6006/v1/traces",
    auto_instrument=True,
)

tracer = tracer_provider.get_tracer(__name__)


@tracer.chain
def test_suggestions():
    # Create the default character agent
    default_character_agent = create_default_character()
    # Create the mage character agent
    mage_character_agent = create_mage_character()

    # Example usage of the default character agent
    user_input = "How do I cross a dangerous river?"
    print("=" * 20)
    print("📣 User Input:\n", user_input)

    response_default = default_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🐣 Default Character Response:\n", response_default)

    # Example usage of the mage character agent
    response_mage = mage_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🧙‍♀️ Mage Character Response:\n", response_mage)
    return {
        "default_character": response_default,
        "mage_character": response_mage,
    }


@tracer.chain
def test_introduce_youself():
    # Create the default character agent
    default_character_agent = create_default_character()
    # Create the mage character agent
    mage_character_agent = create_mage_character()

    # Example usage of the default character agent
    user_input = "Introduce yourself."
    print("=" * 20)
    print("📣  User Input:\n", user_input)

    response_default = default_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🐣 Default Character Response:\n", response_default)

    # Example usage of the mage character agent
    response_mage = mage_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🧙‍♀️ Mage Character Response:\n", response_mage)
    return {
        "default_character": response_default,
        "mage_character": response_mage,
    }


@tracer.chain
def test_fight():
    # Create the default character agent
    default_character_agent = create_default_character()
    # Create the mage character agent
    mage_character_agent = create_mage_character()

    # Example usage of the default character agent
    user_input = "Fight!"
    print("=" * 20)
    print("📣  User Input:\n", user_input)

    response_default = default_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🐣 Default Character Response:\n", response_default)

    # Example usage of the mage character agent
    response_mage = mage_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🧙‍♀️ Mage Character Response:\n", response_mage)
    return {
        "default_character": response_default,
        "mage_character": response_mage,
    }


if __name__ == "__main__":
    test_suggestions()
    test_introduce_youself()
    test_fight()
