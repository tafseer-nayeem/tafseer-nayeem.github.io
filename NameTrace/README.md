# NameTrace

NameTrace studies how unequal name-surface support for first names appears in
task-conditioned representation analyses. This repository includes reusable
analysis code, a runnable 200-pair sample, compact summary files, and selected
paper figures. The full data bundle is hosted as a Hugging Face dataset.

## Contents

- `src/nametrace/`: reusable analysis utilities for tokenization, pair
  selection, task-axis scoring, support-prior adjustment, and representation
  similarity.
- `scripts/`: command-line entry points for tokenizer audits, pair selection,
  and the lightweight sample analysis.
- `data/sample/`: a 200-pair atomic and short-fragmented name sample, plus
  derived inputs for the runnable scripts.
- `data/summary/`: compact aggregate result files used in the paper analyses.
- `figures/`: selected paper figures with descriptive file names.

The full first-name inventory is not included in this code repository. The
complete data is available from the public Hugging Face dataset
`tafseer-nayeem/NameTrace`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Download The Full Data

```bash
python scripts/download_full_data.py --output data/full
```

You can also pass the dataset repository directly:

```bash
python scripts/download_full_data.py \
  --repo-id tafseer-nayeem/NameTrace \
  --output data/full
```

## Run the lightweight check

```bash
python scripts/run_sample_pipeline.py
```

The script writes pair-level atomic-minus-short-fragmented gaps,
task-conditioned name-support scores, pooled task summaries, and a
support-prior adjustment check to `outputs/sample/`.

## Optional tokenizer audit

The tokenizer audit downloads public model tokenizers. It does not require
model weights.

```bash
python scripts/audit_tokenizers.py \
  --names data/sample/sample_names.csv \
  --models configs/primary_tokenizers.csv \
  --output outputs/tokenizer_audit
```

## Pair selection check

```bash
python scripts/select_pairs.py \
  --names data/sample/sample_names_for_pairing.csv \
  --per-group 2 \
  --output outputs/pair_selection
```

The 200-pair sample used in the paper-style checks is provided at
`data/sample/sample_pairs_200.csv`.

The scripts above are the quickest way to check the package. Full-scale runs
use the same file formats but require the larger name inventory and local
access to the model tokenizers or model weights.

## Included Figures

- `tokenizer_allocation_by_name_metadata.pdf`: atomic first-name access across
  audited model-associated tokenizers.
- `task_axis_accessibility_unseen_names.pdf`: pooled held-out task-axis
  accessibility gaps on unseen names.
- `cross_model_name_representation_similarity.pdf`: overall cross-model
  representation similarity over shared atomic names.
- `cross_model_cka_metadata_strata.pdf`: CKA panels within name-metadata
  strata.
- `cross_name_transfer_downstream_leverage.pdf`: cross-name transfer and
  downstream leverage.
- `support_linked_accessibility_metadata_strata.pdf`: support-linked
  accessibility across race/ethnicity--gender-associated strata.
