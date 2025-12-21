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

As for the Qwen3-Next-80B-A3B-Instruct model, see [/cluster](https://github.com/akrav4enk0/Data-Science-Lab/tree/main/cluster) details.


## Run Evaluation Guides

### Terminal-bench
Terminal-Bench provides a standardized evaluation suite for coding agents using containerized tasks (Docker required), with outputs stored as per-model JSON run records plus summary statistics.

- See [docs/terminal-bench guide](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/docs/terminal-bench-guide.md) for more details.

### Fibonacci latency benchmark (custom)
This custom benchmark focuses on latency measurement using a controlled Fibonacci prompt, logging every run (timestamp + runtime) and generating an aggregated mean-latency table used in the report.

- See [docs/fib-latency-benchmark-guide](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/docs/fib-latency-benchmark-guide.md)

## Results

Generated artifacts are stored under [`results/`](results/), separated into:
- [`results/terminal-bench/`](results/terminal-bench/)
- [`results/fib_latency_benchmark/`](results/fib_latency_benchmark/)


