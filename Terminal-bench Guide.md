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
You can test if the model works:
```
curl https://api.swissai.cscs.ch/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "<YOUR_TEST_MODEL>",
    "messages": [
      {"role": "user", "content": "who are you?"}
    ],
    "max_tokens": 100
  }'
```

After Docker and Terminal-Bench setup are done, you can test all the models through SwissAI.

The basic command is:
```
uvx terminal-bench run   -d terminal-bench-core==0.1.1  -a terminus    -m openai/<YOUR_MODEL_NAME>
```
`-d terminal-bench-core==0.1.1` includes 80 tasks, use `uvx terminal-bench datasets list` to check available datasets.


### deepseek-ai/DeepSeek-V3.1
```
uvx terminal-bench run   -d terminal-bench-core==0.1.1  -a terminus    -m openai/deepseek-ai/DeepSeek-V3.1
```

### mistralai/Mistral-7B-v0.1
```
uvx terminal-bench run   -d terminal-bench-core==0.1.1  -a terminus    -m openai/mistralai/Mistral-7B-v0.1
```

### swiss-ai/Apertus-8B-Instruct-2509
```
uvx terminal-bench run -d terminal-bench-core==0.1.1 -a terminus  -m openai/swiss-ai/Apertus-8B-Instruct-2509
```

### swiss-ai/Apertus-70B-Instruct-2509
```
uvx terminal-bench run -d terminal-bench-core==0.1.1 -a terminus  -m openai/swiss-ai/Apertus-70B-Instruct-2509
```

### moonshotai/Kimi-K2-Instruct
```
uvx terminal-bench run -d terminal-bench-core==0.1.1 -a terminus  -m openai/moonshotai/Kimi-K2-Instruct
```

### moonshotai/Kimi-K2-Thinking
```
uvx terminal-bench run -d terminal-bench-core==0.1.1 -a terminus  -m openai/moonshotai/Kimi-K2-Thinking
```

### zai-org/GLM-4.6
```
uvx terminal-bench run -d terminal-bench-core==0.1.1 -a terminus  -m openai/zai-org/GLM-4.6
```
