# Qwen3-Next-80B-A3B-Instruct

First access to the Clariden and get the swissAI key. Then clone this repo:
```
git clone https://github.com/akrav4enk0/Data-Science-Lab.git
cd Data-Science-Lab
```
Copy to: 
```
mkdir -p ~/cluster
cp cluster/qwen-sgl.toml ~/cluster/
cp cluster/qwen3.job ~/cluster/
```
Replace <YOUR_USERNAME> and <YOUR_HF_API_KEY>
```
nano ~/cluster/qwen-sgl.toml 
nano ~/cluster/qwen3.job
```
Then launch the job:
```
cd ~/cluster
sbatch qwen3.job
```
