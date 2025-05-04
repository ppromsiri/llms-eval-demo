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

## Installing Poetry

If you don't have Poetry installed, follow these instructions based on your operating system:

### macOS / Linux

Install with the official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

After installation, you may need to add Poetry to your PATH. Add this line to your shell configuration file (.bashrc, .zshrc, etc.):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows

#### Using PowerShell

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

After installation, Poetry should be automatically added to your PATH. If not, you may need to add `%APPDATA%\Python\Scripts` to your system PATH.

#### Using Chocolatey

If you have Chocolatey package manager:

```
choco install poetry
```

### Verifying Installation

To verify that Poetry is installed correctly:

```bash
poetry --version
```

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
source $(poetry env info --path)/bin/activate  # On macOS/Linux
# OR
# On Windows (PowerShell)
# & $(poetry env info --path)\Scripts\Activate.ps1
# On Windows (CMD)
# call $(poetry env info --path)\Scripts\activate.bat

export PYTHONPATH=~/Project/llms-eval-demo/src  # On macOS/Linux
# OR 
# On Windows (PowerShell)
# $env:PYTHONPATH="$HOME\Project\llms-eval-demo\src"
# On Windows (CMD)
# set PYTHONPATH=%USERPROFILE%\Project\llms-eval-demo\src

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

## Troubleshooting

### Common Issues

- **Poetry not found**: Make sure Poetry is properly installed and added to your PATH
- **Python version mismatch**: Ensure you have Python 3.12+ installed
- **Phoenix server connection issues**: Verify the Phoenix server is running at http://localhost:6006

## License

[License information]
