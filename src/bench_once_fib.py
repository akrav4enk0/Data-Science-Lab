
import os, time, csv, pathlib, datetime, sys, math
from openai import OpenAI

API_KEY  = os.environ.get("OPENAI_API_KEY")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.swissai.cscs.ch/v1")
MODEL    = os.environ.get("OPENAI_MODEL", "swiss-ai/Apertus-70B-Instruct-2509")

PROMPT = (sys.argv[1] if len(sys.argv) > 1
          else "Write a Python function fib(n) that returns the first n Fibonacci numbers and print(fib(10)).")
TAG    = sys.argv[2] if len(sys.argv) > 2 else "fib"

root   = pathlib.Path.home() / "swissai-demo"
outdir = root / "opencode"
outdir.mkdir(parents=True, exist_ok=True)

safe_model = MODEL.replace("/", "_").replace(":", "-")
outfile    = outdir / f"{safe_model}_{TAG}.txt"
csv_path   = root / "summary.csv"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def _extract_text(choice):
    msg = getattr(choice, "message", None)
    content = getattr(msg, "content", None)
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for p in content:
            if isinstance(p, dict):
                t = p.get("text") or p.get("content")
                if isinstance(t, str):
                    parts.append(t)
        if parts:
            return "\n".join(parts).strip()
    try:
        d = choice.model_dump()
        c = d.get("message", {}).get("content")
        if isinstance(c, str):
            return c.strip()
        if isinstance(c, list):
            parts = []
            for p in c:
                if isinstance(p, dict):
                    t = p.get("text") or p.get("content")
                    if isinstance(t, str):
                        parts.append(t)
            if parts:
                return "\n".join(parts).strip()
    except Exception:
        pass
    return ""

def call_with_retry(max_attempts=3, base_sleep=0.8):
    for attempt in range(1, max_attempts + 1):
        t0 = time.perf_counter()
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": PROMPT}],
                temperature=0,
                max_tokens=300,
            )
            dt = time.perf_counter() - t0
            return resp, dt, None
        except Exception as e:
            dt = time.perf_counter() - t0
            err = str(e).splitlines()[-1]
            if attempt == max_attempts:
                return None, dt, err
            time.sleep(base_sleep * (2 ** (attempt - 1)))

resp, dt, err = call_with_retry()

if err is None and resp and getattr(resp, "choices", None):
    text = _extract_text(resp.choices[0]) or "[empty response]"
else:
    text = f"[error: {err}]"

skip = os.environ.get("BENCH_SKIP_LOG") == "1"

if not skip:
    outfile.write_text(text, encoding="utf-8")

if not skip:
    hdr = ["timestamp","model","task","real_seconds","output_file"]
    csv_path_exists = csv_path.exists()
    with csv_path.open("a", newline="") as f:
        w = csv.writer(f)
        if not csv_path_exists:
            w.writerow(hdr)
        w.writerow([
            datetime.datetime.now().isoformat(timespec="seconds"),
            MODEL, TAG, f"{dt:.3f}", str(outfile)
        ])

print(f"Model: {MODEL}")
print(f"Time: {dt:.3f}s")
if not skip:
    print(f"Saved: {outfile}")
if err:
    print(f"Note: API error recorded (continuing): {err}")

