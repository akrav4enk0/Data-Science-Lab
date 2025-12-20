# Data-Science-Lab
Reproducible code for the ETH Zurich Data Science Lab (263-3300-10L) project (Dec 2025). Includes experiments, evaluation scripts, and report-related notebooks.

## Prerequisites
Before running the model deployment, you need access to Clariden cluster, please follow the [official setup guide for Clariden Cluster](https://github.com/swiss-ai/documentation/blob/main/pages/setup_clariden.md) to request credentials and keys.
Once you got the keys:
```
# Update your keys (valid 24h)
./cscs-keygen.sh
ssh-add -t 1d ~/.ssh/cscs-key

# Access to ETH Clariden cluster
ssh clariden

# Conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate

```

## Model Deployment
All model deployments in this project follow the deployment methodology provided by the [swiss-ai/model-launch](https://github.com/swiss-ai/model-launch) repository. This repository provides standardized tools and configurations for deploying large language models on the Clariden cluster using SLURM job scheduling.


