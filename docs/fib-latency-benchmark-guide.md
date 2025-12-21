# Fibonacci Latency Benchmark (Custom)

This benchmark measures **per-request latency** for LLMs on a simple coding prompt (Fibonacci),
using a custom script.

It produces:
- [`results/fib_latency_benchmark/fib_latency_summary.csv`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/fib_latency_summary.csv) - one row per measured run.
- [`results/fib_latency_benchmark/fib_latency_mean.csv`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/fib_latency_mean.csv) - mean latency per model, used in the report.
- [`results/fib_latency_benchmark/sample_outputs/`](https://github.com/akrav4enk0/Data-Science-Lab/tree/main/results/fib_latency_benchmark/sample_outputs) - a few example outputs.

---

## Prerequisites

- Python 3.10+
- Dependencies installed from [`requirements.txt`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/requirements.txt)
- An API key configured (SwissAI or OpenRouter), depending on your setup

---

## Setup

```bash
git clone https://github.com/akrav4enk0/Data-Science-Lab.git
cd Data-Science-Lab

python3 -m venv .venv
source .venv/bin/activate

---

## Configure API access (SwissAI example)

cp configs/env_swissai_example.sh configs/env_swissai.sh
# edit configs/env_swissai.sh and add your key, save the file
source configs/env_swissai.sh
pip install -r requirements.txt

---

## Running the benchmark

The main runner script executes multiple measured runs per model and writes the per-run log.

chmod +x scripts/bench_loop_fib.sh

# choose available models (spun up models are shown here: https://serving.swissai.cscs.ch/)
CLEAR_RESULTS=1 \
MODELS="MODEL_A,MODEL_B,MODEL_C" \
./scripts/bench_loop_fib.sh "" fib 50 3
