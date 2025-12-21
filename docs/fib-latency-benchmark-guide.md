# Fibonacci Latency Benchmark 

This custom-created benchmark measures **per-request latency** for LLMs on a simple coding prompt (Fibonacci),
using a custom script.

It produces:
- [`results/fib_latency_benchmark/fib_latency_summary.csv`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/fib_latency_summary.csv) - one row per measured run.
- [`results/fib_latency_benchmark/fib_latency_mean.csv`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/fib_latency_mean.csv) - mean latency per model, used in the report.
- [`results/fib_latency_benchmark/sample_outputs/`](https://github.com/akrav4enk0/Data-Science-Lab/tree/main/results/fib_latency_benchmark/sample_outputs) - a few example outputs.

---

## Prerequisites

- Python 3.10+
- Dependencies installed from [`requirements.txt`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/requirements.txt)
- An API key configured ( get an API key on [SwissAI](https://serving.swissai.cscs.ch/) or [OpenRouter](https://openrouter.ai/), depending on your prefered setup).  

---

## 1) Setup
```
```bash
git clone https://github.com/akrav4enk0/Data-Science-Lab.git
cd Data-Science-Lab

python3 -m venv .venv
source .venv/bin/activate
```
---

## 2) Configure API access
see [`env_openrouter_example.sh`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/configs/env_openrouter_example.sh) or [`env_swissai_example.sh`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/configs/env_swissai_example.sh))

Here is SwissAI API usage example:

```
cp configs/env_swissai_example.sh configs/env_swissai.sh
# edit configs/env_swissai.sh and add your key, save the file
source configs/env_swissai.sh
pip install -r requirements.txt
```
---

## 3) Running the benchmark

The main runner script executes multiple measured runs per model and writes the per-run log.
```
chmod +x scripts/bench_loop_fib.sh
```
---

# 4 Models

Choose available models (spun up models are shown here: https://serving.swissai.cscs.ch/)

```
CLEAR_RESULTS=1 \
MODELS="MODEL_A,MODEL_B,MODEL_C" \
./scripts/bench_loop_fib.sh "" fib 50 3
```
---
