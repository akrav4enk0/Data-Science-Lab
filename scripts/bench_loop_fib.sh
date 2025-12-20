#!/usr/bin/env bash
set -euo pipefail

# Always run from repo root, no matter where the script is called from
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PYTHON_BIN="${PYTHON_BIN:-python3}"

PROMPT=${1:-"Write a Python function fib(n) that returns the first n Fibonacci numbers and print(fib(10))."}
TAG=${2:-fib}
RUNS=${3:-50}
WARMUP=${4:-3}

mkdir -p results
SUMMARY="results/fib_latency_summary.csv"

MODELS=(
  "swiss-ai/Apertus-8B-Instruct-2509"
  "Qwen/Qwen3-32B"
  "swiss-ai/Apertus-70B-Instruct-2509"
  "deepseek-ai/DeepSeek-V3.1"
  "moonshotai/Kimi-K2-Thinking"
  "mistralai/Mistral-7B-Instruct-v0.2"
)

echo "Writing results to: $SUMMARY"
echo

for m in "${MODELS[@]}"; do
  echo "=== $m ==="
  export OPENAI_MODEL="$m"

  # Warmup (not recorded)
  for _ in $(seq 1 "$WARMUP"); do
    BENCH_SKIP_LOG=1 "$PYTHON_BIN" src/bench_once_fib.py "$PROMPT" "$TAG" >/dev/null 2>/dev/null || true
  done

  # Measured runs
  for _ in $(seq 1 "$RUNS"); do
    "$PYTHON_BIN" src/bench_once_fib.py "$PROMPT" "$TAG"
  done
done

echo
echo "Per-model mean over $RUNS runs (excluding $WARMUP warmups):"
awk -F, '
  NR>1 {sum[$2]+=$4; n[$2]++}
  END {
    printf "%-40s %5s %10s\n","model","n","mean(s)";
    for (m in n) printf "%-40s %5d %10.2f\n", m, n[m], sum[m]/n[m]
  }' "$SUMMARY" | sort
