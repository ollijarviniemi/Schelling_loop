# Control Hackathon 2025: Schelling coordination in agentic loops

Read Inspect_agent/prompt_basic.txt for context on the project.

## Dependencies

- UK AISI's Inspect (https://github.com/UKGovernmentBEIS/inspect_ai)
- Docker

## Setup

Create a file named .env in the Inspect_agent folder with the content

ANTHROPIC_API_KEY="insert-your-api-key-here"

Copy an API key for the LLM agents to use to key.txt.

## Running

- Clone the repository
- Start Docker
- In the Inspect_agent folder, run
  inspect eval inspect_agent.py --model anthropic/claude-3-7-sonnet-latest --temperature 0

Note that inspect_agent.py spins off a Docker container and copies (by default) 1000 files to it. This is slow (~3 minutes), and only after it will actual LLM sampling begin.

One run consumes around 100k-300k tokens.

(Note: inspect_agent.py is hacky due to my limited familiarity with Inspect.)
