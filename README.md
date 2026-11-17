# CREDO

**CREDO: Contextual Reliability across Experts and Dirichlet Opinions for Speech-Based Cognitive Impairment Detection**

**Authors:** Lili Zheng, Wenxin Li, Qi Shao, Sichen Li, Yue Hua, Chen Jason Zhang, Shan Cong, Xiaohui Yao, Hong Liang, and Haoran Luo.

**Supplementary information:** [Supplementary_CREDO.pdf](Supplementary_CREDO.pdf)

## Overview

Speech-based cognitive impairment classification benefits from complementary acoustic and linguistic representations, but the reliability of pretrained experts and individual modalities can vary from one subject to another. **CREDO** models contextual reliability during expert aggregation and uses confidence estimates and joint speech–text context to guide Dirichlet evidential fusion.

## Abstract

CREDO is a contextual reliability learning framework for speech-based cognitive impairment classification. At the representation level, it estimates expert-specific reliability from learned latent variance and focal sensitivity and uses these estimates to aggregate pretrained speech and language representations. Bidirectional cross-modal attention incorporates complementary acoustic and linguistic context. At the decision level, local estimates of true-class confidence and joint speech–text contextual corrections guide the reorientation of modality-specific Dirichlet evidence while preserving total evidence strength. Multi-opinion consistency regularization encourages agreement between confidence-based and evidential reliability assessments. The framework is studied using four public benchmarks and an independent cohort, including analyses of robustness and cross-dataset generalization.

## Key Contributions

- **Reliability-aware foundation model aggregation (RAFMA):** integrates pretrained acoustic and linguistic experts using subject-specific reliability estimated from latent variance and focal sensitivity.
- **Bidirectional cross-modal attention:** refines speech and text representations through complementary expert interactions.
- **Context-aware reliability-guided evidence reorientation (CARER):** combines local confidence priors and joint-context corrections to redistribute class-wise Dirichlet evidence without changing total evidence strength.
- **Multi-opinion consistency regularization (MCR):** encourages agreement between confidence-derived and Dirichlet-derived reliability estimates in speech, text and fused opinions.

## Code Release

The complete CREDO implementation and additional reproducibility resources will be released after the paper is accepted.

## Repository Structure

```text
.
├── README.md
├── Supplementary_CREDO.pdf
├── requirements.txt
├── .gitignore
├── UPLOAD_GUIDE_CN.md
├── script/
│   ├── build_dca_moe_cached_features_v2.py
│   ├── extract_speech_layered_features_v2.py
│   ├── extract_text_layered_features_reference_only.py
│   └── prepare_v2_layered_manifest.py
└── src/
    ├── datasets/
    │   └── dca_moe_cached_dataset.py
    └── models/
        └── README.md
```

## Available Code Components

This repository includes supporting code for preparing speech–text representations used in the CREDO multi-expert framework.

| File | Description |
| --- | --- |
| `script/extract_speech_layered_features_v2.py` | Extracts layered speech representations from pretrained acoustic experts. |
| `script/extract_text_layered_features_reference_only.py` | Reference script for extracting layered text-expert features. |
| `script/prepare_v2_layered_manifest.py` | Organizes feature-path metadata for multimodal inputs. |
| `script/build_dca_moe_cached_features_v2.py` | Constructs cached speech–text feature records. |
| `src/datasets/dca_moe_cached_dataset.py` | Dataset utilities for loading cached multimodal features. |
| `src/models/README.md` | Describes the conceptual model components. |

Internal identifiers in some filenames reflect the research code's development history; the manuscript uses the module names **RAFMA**, **CARER**, and **MCR**.

## Method Modules

| Module | Purpose |
| --- | --- |
| Pretrained speech and language experts | Provide complementary acoustic and linguistic representations. |
| RAFMA | Estimates reliability-aware weights to aggregate each modality's experts. |
| Cross-modal attention | Adds complementary speech–text context to expert representations. |
| CARER | Combines local confidence and joint-context corrections to reorient modality evidence while preserving strength. |
| MCR | Encourages consistency between confidence-derived and Dirichlet-derived reliability signals. |

## Datasets

| Dataset | Language | Classification task |
| --- | --- | --- |
| ADReSS | English | NC vs. AD |
| ADReSSo | English | NC vs. AD |
| NCMMSC | Chinese | NC vs. AD |
| TAUKADIAL | English and Chinese | NC vs. MCI |
| SMU-Cog (external cohort) | Chinese | NC vs. (MCI + AD) |

The public datasets are subject to their respective access terms. The independent SMU-Cog cohort and participant-level data are not distributed in this repository.

## Environment

The accompanying scripts use Python with PyTorch, Transformers and standard audio/data-processing libraries. A dependency list is provided in [`requirements.txt`](requirements.txt). Pretrained models and datasets must be obtained through their respective authorized sources.

## Supplementary Material

[Supplementary_CREDO.pdf](Supplementary_CREDO.pdf) provides additional cohort and dataset protocol details, plus post-hoc word-masking interpretation.

## Citation

Citation details will be updated upon publication.

## Responsible Use

This research is intended for scientific investigation and benchmarking, not standalone clinical diagnosis or clinical decision-making.
