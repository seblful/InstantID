from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="InstantX/InstantID",
                filename="ControlNetModel/config.json", local_dir="./checkpoints")
hf_hub_download(repo_id="InstantX/InstantID",
                filename="ControlNetModel/diffusion_pytorch_model.safetensors", local_dir="./checkpoints")
hf_hub_download(repo_id="InstantX/InstantID",
                filename="ip-adapter.bin", local_dir="./checkpoints")
hf_hub_download(repo_id="latent-consistency/lcm-lora-sdxl",
                filename="pytorch_lora_weights.safetensors", local_dir="./checkpoints")
