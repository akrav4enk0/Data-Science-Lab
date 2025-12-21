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

git clone https://github.com/akrav4enk0/Data-Science-Lab.git
cd Data-Science-Lab

python3 -m venv .venv
source .venv/bin/activate
```
---

## 2) Configure API access
For details see [`env_openrouter_example.sh`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/configs/env_openrouter_example.sh) or [`env_swissai_example.sh`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/configs/env_swissai_example.sh))

Here is SwissAI API usage example:

```
cp configs/env_swissai_example.sh configs/env_swissai.sh
# edit configs/env_swissai.sh and add your key, save the file

source configs/env_swissai.sh #reload env
pip install -r requirements.txt #install requirements
```
---

## 3) Running the benchmark

The main runner script executes multiple measured runs per model and writes the per-run log.
```
chmod +x scripts/bench_loop_fib.sh
```
---

## 4) Add Models

Choose available models on the server (for SwissAI API, spun-up models are shown here: https://serving.swissai.cscs.ch/) and paste model's names instead of `MODEL_A`, etc. 

```
CLEAR_RESULTS=1 \
MODELS="MODEL_A,MODEL_B,MODEL_C" \
./scripts/bench_loop_fib.sh "" fib 50 3
```
##### Arguments used above:
`fib` — benchmark task

`50` — number of measured runs

`3` — warmup runs (excluded from latency mean)

`CLEAR_RESULTS=1` — clears previous CSV logs before writing new ones

##### Outputs:
- Per-run log (evidence of runs) [`results/fib_latency_benchmark/fib_latency_summary.csv`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/fib_latency_summary.csv) contains one row per measured run with: `timestamp`, `model`, `task`, `real_seconds`, `output_file`.

Note: `output_file` typically contains a local absolute path (machine-specific).

- Mean latency table (used in report) [`results/fib_latency_benchmark/fib_latency_mean.csv`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/fib_latency_mean.csv) is a compact table with mean latency per model.

If you want to regenerate it from the per-run log:
```
awk -F, '
NR==1 {next}
{sum[$2]+=$4; n[$2]++}
END {
  print "model,Number of runs,Mean latency [s]"
  for (m in n) printf "%s,%d,%.6f\n", m, n[m], sum[m]/n[m]
}' results/fib_latency_benchmark/fib_latency_summary.csv | sort > results/fib_latency_benchmark/fib_latency_mean.csv
```

- Sample outputs committed to the repo

[`results/fib_latency_benchmark/sample_outputs/`](https://github.com/akrav4enk0/Data-Science-Lab/tree/main/results/fib_latency_benchmark/sample_outputs) contains a few .txt outputs (e.g. [`Apertus-70B`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/sample_outputs/swiss-ai_Apertus-70B-Instruct-2509_fib_20251221_013332.txt) and [`Apertus-8B`](https://github.com/akrav4enk0/Data-Science-Lab/blob/main/results/fib_latency_benchmark/sample_outputs/swiss-ai_Apertus-8B-Instruct-2509_fib_20251221_012833.txt))
as examples/proof-of-run. Full outputs can be large, so only a small subset is tracked.

### Troubleshooting

If you get “model not found / not spun up”, check the currently available SwissAI models:
https://serving.swissai.cscs.ch/

If you get auth errors, re-source your env file and confirm the key is set.
