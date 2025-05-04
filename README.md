# LLMs Evaluation Demo

This project demonstrates how to evaluate Large Language Models (LLMs) using Phoenix for tracking experiments and metrics. It focuses on evaluating character roleplay performance and other metrics for different RPG characters.

## Project Overview

This demo showcases:
- Character-based LLM agents (default novice adventurer and arcane mage)
- Evaluation of responses using LLM-as-judge approaches
- Integration with Phoenix for experiment tracking
- Datasets of example character interactions

## Project Structure

```
src/
├── agentic/
│   ├── agents/             # Agent definitions and factory
│   ├── data/               # Evaluation datasets
│   ├── evaluations/        # Evaluation runners
│   ├── evaluators/         # Evaluation logic
│   └── prompts/            # System prompts for characters and judges
```

## Requirements

- Python 3.12+
- Poetry for dependency management
- Phoenix server running locally for experiment tracking

## Setup

1. Clone the repository
2. Create a .env file based on .env.example with your Gemini API key
3. Install dependencies with Poetry

```bash
poetry config virtualenvs.in-project true
poetry install
```

## Running the Demo

### Start Phoenix Server

```bash
phoenix start
```

This will start the Phoenix server on http://localhost:6006

### Run Character Demos

To test the character agents and see their responses:

```bash
source $(poetry env info --path)/bin/activate
export PYTHONPATH=~/Project/llms-eval-demo/src
python src/agentic/agents/run_agent.py
```

### Create Evaluation Datasets

If you need to upload datasets to Phoenix:

```bash
python src/agentic/evaluators/add_dataset.py
```

### Run Evaluations

To run evaluations using LLM judges:

```bash
python src/agentic/evaluations/run_evaluation_llm.py
```

For non-LLM-based evaluations:

```bash
python src/agentic/evaluations/run_evaluation_non_llm.py
```

## Project Components

### Character Agents

- Default Novice Adventurer: A basic level 1 RPG character with limited skills
- Arcane Mage: A powerful level 12 magic user with various spells

### Evaluation Methods

The project demonstrates two evaluation approaches:
1. LLM-as-judge: Using another LLM to evaluate roleplay quality
2. Conciseness evaluation: Measuring how efficient the responses are

### Phoenix Integration

All evaluations are tracked in Phoenix for easy visualization and comparison between models and prompts.

## License

[License information]
