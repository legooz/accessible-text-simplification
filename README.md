# Accessible Text Simplification

Research connecting lexical-complexity information with text simplification, including work motivated by accessibility for deaf and hard-of-hearing readers.

**Stack:** pandas, NLTK, Hugging Face Datasets/Transformers, PyTorch, PEFT.  
**Status:** experimental notebooks; no validated accessibility improvement or production-readiness claim.

## Workflows

- [`bart_wikilarge_simplification.ipynb`](notebooks/bart_wikilarge_simplification.ipynb): prepare lexical simplification examples and fine-tune `facebook/bart-base` on WikiLarge.
- [`dhh_lexical_lora_experiment.ipynb`](notebooks/dhh_lexical_lora_experiment.ipynb): inspect lexical-complexity scores and explore Llama/LoRA training with a custom simplicity-oriented trainer.

## Setup

```bash
python -m venv .venv
# Activate .venv, then:
python -m pip install -r requirements.txt
python -m jupyter lab
```

GPU acceleration is useful for training. Gated Llama models require account access and `HF_TOKEN` in the environment. The BART and Llama workflows have different model requirements.

## Data

The BART notebook uses [WikiLarge on Hugging Face](https://huggingface.co/datasets/bogdancazan/wikilarge-text-simplification). The original lexical-complexity TSV files and reader-related data are not distributed. Early cells expect `General Lexicon DHH Annotations.tsv` or `GeneralLexiconLinguisticCharacteristics.tsv`; inspect their schema and configure `PROJECT_DATA_DIR` before running.

Generated files include `prepared_data/dhh_lexicon_clean.csv`, `prepared_data/complexity_dict.pkl`, and `prepared_data/train_auto_sft.jsonl`. Generate these from appropriately sourced inputs. Prepared data and trained checkpoints are ignored by Git.

## Evaluation and limitations

Simpler vocabulary alone does not prove meaning preservation or suitability for a reader population. A full evaluation should compare generated/reference text, check semantics, and include an appropriate reader-informed assessment. No freshly reproduced benchmark is reported here.

Saved outputs and embedded credentials were removed from the upload copy. Requirements are a starting environment, not a historical lock. CI validates notebook format and syntax, not training. See [NOTICE.md](NOTICE.md).
