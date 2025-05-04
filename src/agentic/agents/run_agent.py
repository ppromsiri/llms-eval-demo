from langchain_core.messages import HumanMessage

from agentic.agents.agent_factory import create_default_character, create_mage_character


def test_suggestions():
    # Create the default character agent
    default_character_agent = create_default_character()
    # Create the mage character agent
    mage_character_agent = create_mage_character()

    # Example usage of the default character agent
    user_input = "How do I cross a dangerous river?"
    print("=" * 20)
    print("📣 User Input:\n", user_input)

    response = default_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🐣 Default Character Response:\n", response)

    # Example usage of the mage character agent
    response = default_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🧙‍♀️ Mage Character Response:\n", response)


def test_introduce_youself():
    # Create the default character agent
    default_character_agent = create_default_character()
    # Create the mage character agent
    mage_character_agent = create_mage_character()

    # Example usage of the default character agent
    user_input = "Introduce yourself."
    print("=" * 20)
    print("📣  User Input:\n", user_input)

    response = default_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🐣 Default Character Response:\n", response)

    # Example usage of the mage character agent
    response = mage_character_agent.invoke({"msgs": [HumanMessage(content=user_input)]})
    print("=" * 20)
    print("🧙‍♀️ Mage Character Response:\n", response)


def test_fight():
    # Create the default character agent
    default_character_agent = create_default_character()
    # Create the mage character agent
    mage_character_agent = create_mage_character()

    # Example usage of the default character agent
    user_input = "Fight!"
    print("=" * 20)
    print("📣  User Input:\n", user_input)

    response = default_character_agent.invoke(
        {"msgs": [HumanMessage(content=user_input)]}
    )
    print("=" * 20)
    print("🐣 Default Character Response:\n", response)

    # Example usage of the mage character agent
    response = mage_character_agent.invoke({"msgs": [HumanMessage(content=user_input)]})
    print("=" * 20)
    print("🧙‍♀️ Mage Character Response:\n", response)


if __name__ == "__main__":
    test_suggestions()
    test_introduce_youself()
    test_fight()
