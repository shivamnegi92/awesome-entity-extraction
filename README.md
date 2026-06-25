# Awesome Entity Extraction [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, **LLM-era** list of tools, models, libraries, and resources for
> extracting entities, relations, and structured data from unstructured text.

Most "entity extraction" lists were written for the 2018 NLP world — CRFs,
BiLSTMs, and paper dumps. The field has changed: zero-shot taggers, LLM
structured outputs, and graph extraction now do in one prompt what used to take
a labeled corpus and a training run. This list is **practitioner-first** and
**kept current**: every entry links to a real, maintained project.

*Entity extraction* here covers the whole family: Named Entity Recognition
(NER), relation/knowledge extraction, structured-data extraction from text and
documents, PII detection, and the annotation/eval tooling around it.

## Contents

- [Libraries and Frameworks](#libraries-and-frameworks)
- [LLM-Based and Structured Extraction](#llm-based-and-structured-extraction)
- [Zero-Shot and Modern NER Models](#zero-shot-and-modern-ner-models)
- [Relation and Knowledge Extraction](#relation-and-knowledge-extraction)
- [Specialized Extraction](#specialized-extraction)
- [Annotation and Evaluation Tools](#annotation-and-evaluation-tools)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Tutorials and Learning](#tutorials-and-learning)
- [Contributing](#contributing)

## Libraries and Frameworks

General-purpose NLP toolkits with strong, production-grade NER components.

- [spaCy](https://github.com/explosion/spaCy) - Industrial-strength NLP in Python; fast, trainable NER pipelines and the `spancat` component for overlapping spans.
- [Flair](https://github.com/flairNLP/flair) - Simple framework with state-of-the-art sequence taggers and contextual string embeddings.
- [Stanza](https://github.com/stanfordnlp/stanza) - Stanford NLP's neural pipeline with NER for 60+ languages.
- [Spark NLP](https://github.com/JohnSnowLabs/spark-nlp) - Scalable NLP for Apache Spark with a large catalog of pretrained NER models.
- [PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP) - Broad NLP library with information-extraction (UIE) pipelines.
- [NLTK](https://github.com/nltk/nltk) - The classic Python NLP toolkit; useful for chunking-based entity extraction and teaching.
- [nlp.js](https://github.com/axa-group/nlp.js) - NLP library for Node.js with built-in entity extraction.

## LLM-Based and Structured Extraction

The modern default: prompt a model and get back typed, validated structures.

- [LangExtract](https://github.com/google/langextract) - Google's library for extracting structured information from text with LLMs, including source grounding.
- [Instructor](https://github.com/567-labs/instructor) - Structured LLM outputs via Pydantic schemas; the de-facto way to extract typed entities.
- [Outlines](https://github.com/dottxt-ai/outlines) - Constrained/structured generation that guarantees the model emits valid schemas (great for extraction).
- [GraphRAG](https://github.com/microsoft/graphrag) - Microsoft's pipeline that extracts entities and relationships from text to build a knowledge graph for RAG.
- [Haystack](https://github.com/deepset-ai/haystack) - LLM orchestration framework with extractive components and structured-output support.
- [spacy-llm](https://github.com/explosion/spacy-llm) - Drop LLM prompts into spaCy pipelines for zero/few-shot NER with no training.
- [Zerox](https://github.com/getomni-ai/zerox) - OCR-then-LLM pipeline that turns documents (PDFs, images) into structured data.

## Zero-Shot and Modern NER Models

Tag arbitrary entity types with no task-specific training.

- [GLiNER](https://github.com/urchade/GLiNER) - Generalist, lightweight model that recognizes any entity type from a label list — zero-shot, runs on CPU.
- [UniversalNER](https://github.com/universal-ner/universal-ner) - Distilled open models targeting open-domain, instruction-following NER.
- [Zshot](https://github.com/IBM/zshot) - IBM's zero/few-shot entity and relation extraction framework that plugs into spaCy.

## Relation and Knowledge Extraction

Beyond spans: pull relationships and triples to build knowledge graphs.

- [DeepKE](https://github.com/zjunlp/DeepKE) - Knowledge-extraction toolkit for NER, relation, and attribute extraction (standard, low-resource, and document-level).
- [OpenNRE](https://github.com/thunlp/OpenNRE) - Open-source package for neural relation extraction.
- [REBEL](https://github.com/Babelscape/rebel) - Relation extraction as end-to-end seq2seq, jointly extracting entities and relations.

## Specialized Extraction

Domain- and type-specific extraction.

- [Presidio](https://github.com/microsoft/presidio) - Microsoft's PII detection and de-identification for text and images.
- [scispaCy](https://github.com/allenai/scispacy) - spaCy models for biomedical, scientific, and clinical entity extraction.
- [KeyBERT](https://github.com/MaartenGr/KeyBERT) - Keyword and keyphrase extraction using BERT embeddings.
- [pke](https://github.com/boudinfl/pke) - Python keyphrase-extraction toolkit (supervised and unsupervised).
- [Table Transformer](https://github.com/microsoft/table-transformer) - Detect and extract tables (and their structure) from documents.

## Annotation and Evaluation Tools

You still need labeled data for evaluation and fine-tuning.

- [Label Studio](https://github.com/HumanSignal/label-studio) - Multi-type data labeling platform with strong NER/span annotation.
- [doccano](https://github.com/doccano/doccano) - Open-source text annotation tool for NER, classification, and sequence labeling.
- [Argilla](https://github.com/argilla-io/argilla) - Collaboration platform for building and curating NLP/LLM datasets.
- [prodigy-recipes](https://github.com/explosion/prodigy-recipes) - Recipes and examples for Prodigy, the scriptable annotation tool from the spaCy team.

## Datasets and Benchmarks

- [IEPile](https://github.com/zjunlp/IEPile) - Large-scale, bilingual information-extraction instruction corpus for training extraction models.

## Tutorials and Learning

- [Transformers Tutorials](https://github.com/NielsRogge/Transformers-Tutorials) - Hands-on notebooks including token classification / NER with Transformers.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.
The one hard rule: **every entry must link to a real, maintained project** and
include a short, factual description. No dead links, no vaporware.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and
related or neighboring rights to this work.
