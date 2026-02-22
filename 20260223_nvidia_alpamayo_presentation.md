# NVIDIA Alpamayo
## Autonomous Vehicles That Think

*Presented February 2026*

---

## Agenda

1. What is Alpamayo?
2. The Problem It Solves
3. Core Components
4. Alpamayo 1: The Model
5. Physical AI Dataset
6. AlpaSim: The Simulator
7. Technical Specifications
8. Deployment Architecture
9. Key Differentiators
10. Road Ahead

---

## 1. What is NVIDIA Alpamayo?

> *"Our vision is that someday, every single car, every single truck, will be autonomous."*
> — Jensen Huang, CES 2026

**Alpamayo** is NVIDIA's open portfolio of AI models, simulation frameworks, and physical AI datasets designed to accelerate the development of safe, transparent, and reasoning-based autonomous vehicles.

Announced at **CES 2026**, Alpamayo represents NVIDIA's most comprehensive push yet into **Level 4 autonomy** — enabling vehicles to not just perceive the world, but to **reason, act, and explain** their decisions.

---

## 2. The Problem It Solves: The Long Tail

Traditional autonomous driving systems struggle with **long-tail events** — rare, unpredictable edge cases that don't appear often in training data but can be critical or fatal in the real world.

**Examples of long-tail scenarios:**
- Unexpected road debris
- Unusual pedestrian behaviour
- Rare weather or lighting conditions
- Abnormal vehicle behaviour from other drivers

**The old approach:** Perception pipelines that *see → plan → execute*, with no explanation of *why* a decision was made.

**The Alpamayo approach:** Systems that reason step-by-step, like a human driver, and can articulate their logic — enabling safety validation, regulatory compliance, and trust.

---

## 3. Core Components

Alpamayo is a **three-pillar platform**, designed to work together as a complete, open toolchain:

| Component | Description |
|---|---|
| **Alpamayo 1** | 10B-parameter Vision-Language-Action (VLA) reasoning model |
| **Physical AI AV Dataset** | 1,727 hours of real-world multi-sensor driving data |
| **AlpaSim** | Open-source, closed-loop autonomous driving simulator |

All three components are **open and available** on GitHub and Hugging Face for research and non-commercial use.

---

## 4. Alpamayo 1: The Model

### What it is
Alpamayo 1 is a **10-billion parameter Vision-Language-Action (VLA) model** — the first open, industry-scale reasoning model for autonomous driving. It bridges interpretable chain-of-thought reasoning with precise vehicle control.

### Architecture
- **Backbone:** 8.2B-parameter Cosmos Reason (NVIDIA's foundational physical AI model)
- **Action Expert:** 2.3B-parameter diffusion-based trajectory decoder
- **Inputs:** Multi-camera video + egomotion history (360° coverage)
- **Outputs:** Predicted trajectory + human-readable reasoning trace

### Chain-of-Causation Reasoning
Alpamayo 1 doesn't just predict where to go — it generates a **natural language explanation** of *why* it made that decision. This "Chain-of-Causation" approach makes the model's decisions **interpretable, auditable, and regulatory-friendly**.

### Training Data
- Over **1 billion images** from 80,000 hours of multi-camera driving data
- Mix of Chain-of-Causation reasoning traces, Cosmos-Reason Physical AI datasets, and NVIDIA proprietary AV data

---

## 5. Physical AI AV Dataset

### Scale & Diversity
One of the **largest and most geographically diverse** open autonomous vehicle datasets ever released.

| Metric | Detail |
|---|---|
| Total Duration | 1,727 hours of driving data |
| Data Volume | ~100 TB |
| Countries Covered | 25 countries |
| Cities Covered | 2,500+ cities |
| Camera Coverage | 360° from 7 synchronized cameras |
| Additional Sensors | LiDAR + up to 10 radars |

### Why It Matters
This dataset is approximately **3× the size of Waymo's public dataset**, providing unprecedented diversity of traffic patterns, road conditions, and driving cultures across the globe. It is specifically curated to address **long-tail scenarios** that are underrepresented in typical AV training data.

---

## 6. AlpaSim: The Open-Source Simulator

AlpaSim is a **complete Python-based testbed** for evaluating autonomous driving policies in a reactive, closed-loop environment — where the AI's decisions directly influence what happens next.

### Key Capabilities
- **Closed-loop testing:** AI decisions affect the simulation, creating realistic feedback loops
- **Diverse scenarios:** Varied traffic, weather conditions, and edge cases at scale
- **Microservice architecture:** Modular design with gRPC APIs allows easy integration of custom policies
- **Pipeline parallelism:** Efficient multi-GPU evaluation for high throughput testing

### Services in AlpaSim
Driver · Renderer · TrafficSim · Controller · Physics — each running as an independent process, assignable to different GPUs.

---

## 7. Technical Specifications

### Model Requirements
| Parameter | Specification |
|---|---|
| Model Parameters | 10 billion |
| Minimum VRAM | 24 GB (tested on RTX 3090, A100, H100) |
| Fine-tuning Cluster | 8 GPUs with 24GB+ VRAM each |
| Inference Latency Target | 99ms (10Hz decision rate) |
| Model Weights | ~22 GB (safetensors format) |
| License | Non-commercial (weights) / Apache 2.0 (inference code) |

### Training Infrastructure (Full Training from Scratch)
- GPU cluster with NVLink/NVSwitch interconnects
- High-bandwidth storage (100+ GB/s aggregate)
- 10+ PB storage capacity
- Estimated training cost: $500K–$2M

---

## 8. Deployment Architecture

Alpamayo is a **teacher system**, not a vehicle runtime model. Its role is to train, test, and harden autonomous stacks *before* they reach the road.

```
[ Data Center Training ]       [ Edge Deployment ]
  GPU Cluster (H100/A100)  →   DRIVE Orin (254 TOPS / 65–70W)
  Alpamayo 1 (teacher)     →   DRIVE Thor (1,000+ TOPS / ~100W)
  AlpaSim (evaluation)     →   Jetson AGX Orin (275 TOPS / 15–60W)
```

### Deployment Targets
| Platform | Performance | Power | Use Case |
|---|---|---|---|
| DRIVE Orin | 254 TOPS | 65–70W | Production vehicles |
| DRIVE Thor | 1,000+ TOPS | ~100W | Next-gen L4 systems |
| Jetson AGX Orin | 275 TOPS | 15–60W | Development / robotics |

Knowledge is **distilled** from the large teacher model into smaller, runtime-capable models deployable at the edge.

---

## 9. Key Differentiators

### Open & Transparent
Unlike closed, proprietary AV stacks, Alpamayo is **fully open** — models, simulation tools, and datasets are publicly accessible. Developers can inspect, extend, and fine-tune for specific regional safety and regulatory requirements.

### Explainable AI
Alpamayo moves beyond "black-box" path planning. By generating **human-readable reasoning traces**, it supports interpretable, auditable autonomy — a prerequisite for regulatory approval in many markets.

### Industry-First Scale
NVIDIA describes Alpamayo as the **first comprehensive open-source suite** of AI models, simulation tools, and datasets designed specifically to tackle long-tail autonomous driving challenges.

### Ecosystem Integration
Alpamayo integrates seamlessly with the full NVIDIA DRIVE stack — from training and simulation all the way to in-vehicle deployment — reducing development time for OEMs, Tier 1 suppliers, startups, and researchers.

---

## 10. Road Ahead

### Current Status (Early 2026)
- Alpamayo 1 (10B model) available on GitHub and Hugging Face
- Physical AI AV Dataset publicly released
- AlpaSim open-sourced
- Partnership with **Mercedes-Benz** announced at CES 2026
- Autonomous vehicles using NVIDIA technology expected in the U.S. **within months**

### What's Coming
- **RL post-training:** Reinforcement learning stages (described in the research paper) not yet included in the released model — future releases planned
- **Route conditioning:** Navigation/waypoint inputs are in experimentation; not yet released
- **Meta-actions & VQA:** General visual question answering capabilities under development
- Smaller, **distilled runtime models** optimised for edge deployment

### The Bigger Picture
Alpamayo sits at the intersection of NVIDIA's AI factory strategy and the physical world. As Jensen Huang put it at CES 2026:

> *"The inflection point of going from non-autonomous vehicles to autonomous is fully here."*

---

## Summary

| | |
|---|---|
| **Platform** | Open AI models, datasets & simulator for Level 4 AV development |
| **Flagship Model** | Alpamayo 1 — 10B VLA reasoning model |
| **Key Innovation** | Chain-of-Causation reasoning: vehicles that explain *why* they act |
| **Dataset** | 1,727 hours, 25 countries, 100 TB of real-world sensor data |
| **Simulator** | AlpaSim — open-source, closed-loop, microservice-based |
| **Availability** | Open for research (non-commercial) on GitHub & Hugging Face |
| **Announced** | CES 2026 |

---

*Sources: NVIDIA Developer Blog, Hugging Face Model Card, NVIDIA CES 2026 Keynote, arXiv:2511.00088*
