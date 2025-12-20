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
```source ~/miniconda3/etc/profile.d/conda.sh
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
