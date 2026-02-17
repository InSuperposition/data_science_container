---
license: mit
size_categories:
  - n<1K
task_categories:
  - image-to-text
  - zero-shot-image-classification
tags:
  - clip
  - embeddings
  - qdrant
  - image-retrieval
  - educational
  - latent-assembly
  - pre-computed
---

# Latent Assembly — CLIP + Qdrant Artifacts

Pre-computed artifact package for the **Latent Assembly with CLIP + Qdrant** exercise.

## What is this?

This dataset repo stores the output of **Part A** (embedding pipeline) so that
**Part B** (multi-intent retrieval and marketplace assembly) can rebuild a Qdrant
index **without re-embedding** the images.

## Files

```shell
dataset/
├── img_vecs.npy      # (300, 512) float32 — L2-normalized CLIP image embeddings
├── payloads.json     # list of {"filename": str, "caption": str} dicts
└── meta.json         # index metadata (dataset, model, caption source, count)
```

| File | Format | Description |
| ---- | ------ | ----------- |
| `img_vecs.npy` | NumPy `.npy` | Shape `(300, 512)`, dtype `float32`. Each row is an L2-normalized CLIP image embedding. |
| `payloads.json` | JSON array | 300 entries, each with `"filename"` and `"caption"` keys. |
| `meta.json` | JSON object | Records `dataset_name`, `caption_source`, `model_name`, `embedding_dim`, `num_items`. |

## Source Dataset

- **Dataset:** [lmms-lab/COCO-Caption2017](https://huggingface.co/datasets/lmms-lab/COCO-Caption2017)
- **Split:** `val` (streamed, first 300 usable samples)
- **Caption path:** `sample['answer'][0]` (first annotator caption per image)

## Embedding Model

- **Model:** [openai/clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32)
- **Embedding dim:** 512
- **Normalization:** L2-normalized (unit vectors, suitable for cosine similarity)
- **Extraction:** `model.get_image_features(**inputs).pooler_output`

## Usage (Part B)

```python
import json
import numpy as np
from huggingface_hub import hf_hub_download

HF_USER_NAME = "vector-helix"
HF_REPO_NAME = "latent-assembly-clip-qdrant"
HF_REPO_ID = HF_USER_NAME + "/" + HF_REPO_NAME
SUBDIR  = "dataset"

# Download artifacts
for fname in ["img_vecs.npy", "payloads.json", "meta.json"]:
    hf_hub_download(repo_id=HF_REPO_ID, repo_type="dataset",
                    filename=f"{SUBDIR}/{fname}", local_dir=".")

# Load
img_vecs = np.load(f"{SUBDIR}/img_vecs.npy")
with open(f"{SUBDIR}/payloads.json") as f:
    payloads = json.load(f)
with open(f"{SUBDIR}/meta.json") as f:
    meta = json.load(f)

print(f"Loaded {img_vecs.shape[0]} vectors, dim={img_vecs.shape[1]}")
# -> Loaded 300 vectors, dim=512

# Rebuild Qdrant collection from these artifacts (no re-embedding needed)
```
