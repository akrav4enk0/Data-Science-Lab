# Terminal-Bench Guide

## Prerequisites
Terminal-Bench executes coding tasks in isolated Docker containers, so [Docker](https://www.docker.com/) must be installed on your system.

## Terminal-bench
The official website is [here](https://www.tbench.ai/)

Once Docker is installed and running, you can install Terminal-Bench using `uvx`:
```
uvx terminal-bench
```

Set up API credentials for LLM provider, see examples in [/configs](https://github.com/akrav4enk0/Data-Science-Lab/tree/main/configs)

Replace `<SWISSAI_API_KEY>` with your actual SwissAI API key.
```
export OPENAI_BASE_URL="https://api.swissai.cscs.ch/v1"
export OPENAI_API_KEY="<SWISSAI_API_KEY>"
```
After Docker and Terminal-Bench setup are done, you can test all the models through SwissAI.


###


