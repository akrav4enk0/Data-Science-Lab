# Data-Science-Lab
Reproducible code for the ETH Zurich Data Science Lab (263-3300-10L) project (Dec 2025). Includes experiments, evaluation scripts, and report-related notebooks.

## Prerequisites
Before running the model deployment, you need access to Clariden cluster, please follow the [official setup guide for Clariden Cluster](https://github.com/swiss-ai/documentation/blob/main/pages/setup_clariden.md) to request credentials and keys.

Once you got the keys:
1. Update your keys (valid 24h)
```
./cscs-keygen.sh
ssh-add -t 1d ~/.ssh/cscs-key
```
2. Access to ETH Clariden cluster
```
ssh clariden
```

4. Conda environment
```
source ~/miniconda3/etc/profile.d/conda.sh
conda activate
```

## Model Deployment
All model deployments in this project follow the deployment methodology provided by the [swiss-ai/model-launch](https://github.com/swiss-ai/model-launch) repository. This repository provides standardized tools and configurations for deploying large language models on the Clariden cluster using SLURM job scheduling.

The following models were successfully deployed and evaluated using the model-launch framework:
- Apertus-8B-Instruct-2509 
- DeepSeek-V3.1
- Kimi-K2-Instruct
- Kimi-K2-Thinking
- Mistral-7B-v0.1
- GLM-4.6

As for the Qwen3-Next-80B-A3B-Instruct model, see xxxxxx detail.


## Run Evaluation
### Terminal-bench
tbc


## Quickstart with SwissAI API

### Prerequisites
- Python 3.10+
- A SwissAI API key 

### Setup
```bash
git clone https://github.com/akrav4enk0/Data-Science-Lab.git
cd Data-Science-Lab

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


cp configs/env_swissai_example.sh configs/env_swissai.sh
# edit configs/env_swissai.sh and paste your key using - nano configs/env_swissai.sh
source configs/env_swissai.sh

chmod +x scripts/bench_loop_fib.sh
# choose available models (spun up models shown here: https://serving.swissai.cscs.ch/)

CLEAR_RESULTS=1 MODELS="AVAILABLE_MODEL" ./scripts/bench_loop_fib.sh "" fib 50 3





