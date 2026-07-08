
# 🚀 Transformer From Scratch

> **Implementing *Implementaion of influential papers related to transformers from scratch ising python, numpy, Fastapi.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Latest-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

This repository is a **learning-first implementation** of the original Transformer architecture proposed in the paper:

> **Attention Is All You Need**
> Ashish Vaswani et al., 2017

The objective is **not** to build the fastest or most optimized Transformer.

Instead, the goal is to understand **every mathematical operation**, **every tensor shape**, and **every architectural component** by implementing everything manually.

This project intentionally avoids high-level Transformer libraries.

---

# 🎯 Learning Objectives

By completing this project you will understand:

* Token Embeddings
* Positional Encoding
* Scaled Dot-Product Attention
* Multi-Head Attention
* Feed Forward Networks
* Residual Connections
* Layer Normalization
* Encoder Architecture
* Decoder Architecture
* Attention Masks
* Cross Entropy Loss
* Teacher Forcing
* Greedy Decoding
* Beam Search (optional)
* Training Loop
* Inference Pipeline

---

# ❌ What This Project Does NOT Use

To maximize learning, the following are intentionally **not used**:

* ❌ `torch.nn.Transformer`
* ❌ Hugging Face Transformers
* ❌ PyTorch Lightning
* ❌ Trainer APIs
* ❌ Third-party Transformer implementations
* ❌ Copied source code

Everything is implemented manually using only:

* Python
* numpy
* pandas


---

# 🧠 Learning Philosophy

The implementation follows a simple cycle:

```
Read Paper
      ↓
Understand Mathematics
      ↓
Implement
      ↓
Visualize
      ↓
Test
      ↓
Train
      ↓
Repeat
```

Every module should be implemented from scratch before moving to the next one.

---

# 📚 Paper Roadmap

| Section | Topic                        | Status |
| ------- | ---------------------------- | ------ |
| 3.1     | Encoder–Decoder Architecture | ⬜      |
| 3.2     | Scaled Dot Product Attention | ⬜      |
| 3.2.2   | Multi-Head Attention         | ⬜      |
| 3.3     | Feed Forward Network         | ⬜      |
| 3.4     | Embeddings                   | ⬜      |
| 3.5     | Positional Encoding          | ⬜      |
| 5       | Training                     | ⬜      |
| 6       | Results                      | ⬜      |

---

# 🏗 Project Structure

```text
papers-from-scratch/
│
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
                  
│
├── app/
|    ├── main.py   # FastAPI entrypoint
│   ├── api/
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── logger.py
│   │   └── utils.py
│   │
│   ├── data/
│   │   ├── datasets/
│   │   ├── dataloaders/
│   │   ├── tokenizers/
│   │   ├── transforms/
│   │   └── preprocessing/
│   │
│   ├── training/
│   │   ├── trainer.py
│   │   ├── evaluator.py
│   │   ├── losses.py
│   │   ├── optimizers.py
│   │   ├── schedulers.py
│   │   ├── metrics.py
│   │   └── checkpoint.py
│   │
│   ├── inference/
│   │   ├── predictor.py
│   │   ├── decoding.py
│   │   └── visualization.py
│   │
│   ├── shared/
│   │   ├── layers/
│   │   ├── activations/
│   │   ├── normalization/
│   │   ├── attention/
│   │   └── embeddings/
│   │
│   └── papers/
│       │
│       ├── attention_is_all_you_need/
│       │   ├── README.md
│       │   ├── config.py
│       │   ├── model.py
│       │   ├── encoder.py
│       │   ├── decoder.py
│       │   ├── attention.py
│       │   ├── train.py
│       │   ├── inference.py
│       │   └── tests/
│       │
│       ├── bert/
│       │   ├── README.md
│       │   ├── config.py
│       │   ├── model.py
│       │   └── ...
│       │
│       ├── gpt/
│       │   ├── README.md
│       │   ├── config.py
│       │   ├── model.py
│       │   └── ...
│       │
│       ├── vision_transformer/
│       │   └── ...
│       │
│       ├── swin_transformer/
│       │   └── ...
│       │
│       ├── flash_attention/
│       │   └── ...
│       │
│       ├── performer/
│       │   └── ...
│       │
│       ├── linformer/
│       │   └── ...
│       │
│       ├── reformer/
│       │   └── ...
│       │
│       ├── longformer/
│       │   └── ...
│       │
│       ├── llama/
│       │   └── ...
│       │
│       └── template/
│           ├── README.md
│           ├── config.py
│           ├── model.py
│           ├── train.py
│           ├── inference.py
│           └── tests/
│
├── checkpoints/
│   ├── attention_is_all_you_need/
│   ├── bert/
│   ├── gpt/
│   └── ...
│
├── datasets/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── attention_is_all_you_need/
│   ├── bert/
│   ├── gpt/
│   └── ...
│
├── outputs/
│   ├── figures/
│   ├── logs/
│   ├── predictions/
│   └── benchmarks/
│
├── scripts/
│   ├── train.py
│   ├── evaluate.py
│   ├── benchmark.py
│   ├── predict.py
│   └── download_data.py
│
└── docs/
    ├── paper_notes/
    ├── implementation_notes/
    ├── math/
    └── experiments/
```


```

---

# 📦 Transformer Components

The implementation is divided into independent modules.

```
Transformer

├── Embeddings
├── Positional Encoding
├── Scaled Dot Product Attention
├── Multi Head Attention
├── Feed Forward Network
├── Layer Normalization
├── Residual Connection
├── Encoder Layer
├── Encoder Stack
├── Decoder Layer
├── Decoder Stack
├── Masks
└── Transformer
```

---

# 🗓 Learning Roadmap

## Day 1

* Embeddings
* Vocabulary
* Tokenizer
* Cross Entropy Loss

---

## Day 2

* Query
* Key
* Value
* Scaled Dot Product Attention

---

## Day 3

* Multi-Head Attention

---

## Day 4

* Positional Encoding
* Feed Forward Network

---

## Day 5

* Encoder

---

## Day 6

* Decoder

---

## Day 7

* Complete Transformer
* Training Loop
* Tiny Translation Demo

---

# 🌐 FastAPI Endpoints

| Method | Endpoint      | Description                       |
| ------ | ------------- | --------------------------------- |
| GET    | `/health`     | Health Check                      |
| GET    | `/config`     | Model Configuration               |
| POST   | `/tokenize`   | Tokenize Sentence                 |
| POST   | `/embedding`  | Embedding Output                  |
| POST   | `/attention`  | Attention Visualization           |
| POST   | `/encoder`    | Encoder Forward Pass              |
| POST   | `/decoder`    | Decoder Forward Pass              |
| POST   | `/forward`    | Complete Transformer Forward Pass |
| POST   | `/train-step` | Execute One Training Step         |
| POST   | `/predict`    | Greedy Decoding                   |

---

# 🧩 Implementation Checklist

## Data

* [ ] Vocabulary
* [ ] Tokenizer
* [ ] Dataset
* [ ] Dataloader

---

## Embeddings

* [ ] Token Embedding
* [ ] Positional Encoding

---

## Attention

* [ ] Scaled Dot Product Attention
* [ ] Multi Head Attention
* [ ] Attention Masks

---

## Network

* [ ] Feed Forward Network
* [ ] Layer Normalization
* [ ] Residual Connections

---

## Encoder

* [ ] Encoder Layer
* [ ] Encoder Stack

---

## Decoder

* [ ] Decoder Layer
* [ ] Decoder Stack

---

## Training

* [ ] Loss Function
* [ ] Optimizer
* [ ] Scheduler
* [ ] Training Loop
* [ ] Checkpoint Saving

---

## Inference

* [ ] Greedy Decoding
* [ ] Beam Search (Optional)

---

# 📈 Development Workflow

```
Read Paper
      ↓
Implement Module
      ↓
Unit Test
      ↓
Visualize Tensor Shapes
      ↓
Train on Toy Dataset
      ↓
Verify Loss
      ↓
Continue
```

---

# 📖 References

## Primary Paper

* *Attention Is All You Need* (2017)

## Recommended Reading

* The Annotated Transformer
* Dive into Deep Learning
* PyTorch Documentation

---

# 🎓 Learning Outcomes

By the end of this project you should be able to:

* Explain every equation in the paper.
* Implement a Transformer without high-level APIs.
* Train a Transformer on a toy sequence-to-sequence task.
* Visualize attention weights.
* Debug tensor shape mismatches confidently.
* Extend the architecture with your own ideas.

---

# 🚧 Future Improvements

After reproducing the original paper:

* Beam Search
* Label Smoothing
* Learning Rate Warmup
* Mixed Precision Training
* Flash Attention
* KV Cache
* Rotary Positional Embeddings (RoPE)
* Grouped Query Attention (GQA)
* Multi Query Attention (MQA)
* Sparse Attention
* Sliding Window Attention
* Transformer Variants
* Efficient Transformers
* LLM Inference Optimizations

---

# ⭐ Project Goal

> **Don't just use Transformers. Understand them well enough to build one from a blank file.**
