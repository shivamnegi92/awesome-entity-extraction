# Runnable Examples

Minimal, copy-paste starting points for the main entity-extraction approaches.
Each file lists its own `pip install` line at the top.

| File | Approach | What it shows |
|------|----------|---------------|
| [spacy_ner.py](spacy_ner.py) | Trained pipeline | Classic NER with a pretrained spaCy model |
| [gliner_zeroshot.py](gliner_zeroshot.py) | Zero-shot | Name your own entity types, no training |
| [llm_instructor.py](llm_instructor.py) | LLM + schema | Typed, validated extraction with Pydantic |
| [presidio_pii.py](presidio_pii.py) | PII | Detect and anonymize personal data |

These are intentionally tiny. For the full catalog of tools, models, and
datasets, see the [main list](../README.md).
