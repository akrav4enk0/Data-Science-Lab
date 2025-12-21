# Terminal-Bench Guide

## Prerequisites
Terminal-Bench executes coding tasks in isolated Docker containers, so [Docker](https://www.docker.com/) must be installed on your system.

## Terminal-bench
The official [website](https://www.tbench.ai/)

Once Docker is installed and running, you can install Terminal-Bench using `uvx`:
```
uvx terminal-bench
```

Set up API credentials for LLM provider, see examples in [/configs](https://github.com/akrav4enk0/Data-Science-Lab/tree/main/configs)

Change `<SWISSAI_API_KEY>` to your own.
```
export OPENAI_BASE_URL="https://api.swissai.cscs.ch/v1"
export OPENAI_API_KEY="<SWISSAI_API_KEY>"
```
