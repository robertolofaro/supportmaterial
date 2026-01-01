import os
import json
import hashlib
import re
from pathlib import Path

# --- CONFIGURATION ---
GPT4ALL_DIR = Path("/home/modeldisk/gpt4all/models")
OLLAMA_MODELS_DIR = Path("/usr/share/ollama/.ollama/models")
BLOBS_DIR = OLLAMA_MODELS_DIR / "blobs"
MANIFEST_DIR = OLLAMA_MODELS_DIR / "manifests/registry.ollama.ai/library"

def sanitize_name(name):
    """Clean name to meet Ollama's registry requirements."""
    # 1. Lowercase and replace spaces/special chars with dashes
    name = name.lower().replace(" ", "-").replace("_", "-")
    # 2. Remove any character that isn't alphanumeric, dot, or dash
    name = re.sub(r'[^a-z0-9.-]', '', name)
    # 3. Truncate if name is too long (Ollama prefers < 64 chars for names)
    if len(name) > 60:
        name = name[:55] + "-ext"
    # 4. Remove leading/trailing dashes or dots
    return name.strip("-.")

def get_sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def sideload():
    BLOBS_DIR.mkdir(parents=True, exist_ok=True)

    for gguf in GPT4ALL_DIR.glob("*.gguf"):
        # Automatically clean the name for Ollama
        model_name = sanitize_name(gguf.stem)
        print(f"Syncing: {gguf.name} -> ollama:{model_name}")

        # 1. Link weights
        weight_hash = get_sha256(gguf)
        weight_blob_path = BLOBS_DIR / f"sha256-{weight_hash}"
        if not weight_blob_path.exists():
            os.symlink(gguf.absolute(), weight_blob_path)

        # 2. Config Blob
        config_data = {"architecture": "amd64", "os": "linux", 
                       "rootfs": {"type": "layers", "diff_ids": [f"sha256:{weight_hash}"]}}
        config_json = json.dumps(config_data).encode('utf-8')
        config_hash = hashlib.sha256(config_json).hexdigest()
        config_blob_path = BLOBS_DIR / f"sha256-{config_hash}"
        
        if not config_blob_path.exists():
            with open(config_blob_path, "wb") as f:
                f.write(config_json)

        # 3. Manifest
        manifest_data = {
            "schemaVersion": 2,
            "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "config": {"mediaType": "application/vnd.ollama.image.config", "digest": f"sha256:{config_hash}", "size": len(config_json)},
            "layers": [{"mediaType": "application/vnd.ollama.image.model", "digest": f"sha256:{weight_hash}", "size": gguf.stat().st_size}]
        }
        
        model_manifest_dir = MANIFEST_DIR / model_name
        model_manifest_dir.mkdir(parents=True, exist_ok=True)
        with open(model_manifest_dir / "latest", "w") as f:
            json.dump(manifest_data, f)

if __name__ == "__main__":
    sideload()
