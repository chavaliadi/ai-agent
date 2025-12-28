# AI Research Agent

A Python-based research assistant that combines web search capabilities with AI-powered responses using LangChain and Groq's Llama model.

## Overview

This project is an interactive research agent that helps answer questions by:
1. **Searching the web** using DuckDuckGo to find relevant information
2. **Processing search results** with an AI language model (Llama 3.1 8B Instant via Groq)
3. **Providing concise, well-informed answers** based on the search results

## Features

- 🔍 **Web Search Integration**: Uses DuckDuckGo to search for real-time information
- 🤖 **AI-Powered Responses**: Leverages Groq's fast Llama 3.1 8B Instant model for quick responses
- 💬 **Interactive CLI**: Simple command-line interface for easy interaction
- ⚡ **Fast Performance**: Groq's optimized inference for near-instant responses
- 🛡️ **Error Handling**: Graceful handling of rate limits and other errors

## Tech Stack

- **LangChain**: Framework for building LLM applications
- **Groq**: High-performance AI inference platform
- **DuckDuckGo**: Privacy-focused web search
- **Python 3.13**: Programming language

## Setup

### Prerequisites

- Python 3.13+
- Groq API key ([Get one here](https://console.groq.com/))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/chavaliadi/ai-agent.git
cd ai-agent
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Run the research agent:
```bash
python main.py
```

The agent will prompt you for questions. Type your question and press Enter. The agent will:
1. Search the web for relevant information
2. Process the results with AI
3. Display a concise answer

Type `exit` to quit the application.

## Example Output

```
==================================================
RESEARCH AGENT
==================================================
Type 'exit' to quit

Your question: Who is Messi?

🔍 Searching...

==================================================
Lionel Messi is an Argentine professional footballer widely regarded as one of the greatest players of all time. He currently plays as a forward for Inter Miami CF in Major League Soccer and captains the Argentina national team.

Messi spent the majority of his career with FC Barcelona, where he won numerous titles including 10 La Liga championships and 4 UEFA Champions League titles. He has won the Ballon d'Or award a record eight times and holds multiple records for goals scored in both club and international football. In 2022, he led Argentina to victory in the FIFA World Cup, cementing his legacy as one of the sport's all-time greats.
==================================================

Your question: exit

Thank you for using the Research Agent. Goodbye!
```

## Project Structure

```
ai-agent/
├── main.py              # Main application entry point
├── tools.py             # Search tool implementation
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Key Components

### `main.py`
- Initializes the Groq LLM model
- Implements the interactive CLI loop
- Combines search results with AI processing
- Handles user input and error cases

### `tools.py`
- Defines the `search_tool` function using LangChain's `@tool` decorator
- Integrates DuckDuckGo search API
- Formats search results for the LLM

## Error Handling

The application handles:
- **Rate Limiting**: Displays a warning if API rate limits are hit
- **Empty Queries**: Prompts user to enter a valid question
- **Search Errors**: Gracefully handles search failures
- **Keyboard Interrupts**: Clean exit on Ctrl+C

## Notes

- The `.env` file is excluded from version control for security
- Make sure to keep your Groq API key secure and never commit it to the repository
- The agent uses DuckDuckGo for search, which respects user privacy

## License

This project is open source and available for personal and educational use.
