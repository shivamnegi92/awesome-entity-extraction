# Awesome Entity Extraction [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A practitioner-first field guide to entity, relation, and structured-data
> extraction: find a tool by task, run a standalone example, and understand
> trade-offs before choosing.

[![awesome-lint](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/awesome-lint.yml/badge.svg)](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/awesome-lint.yml)
[![links](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/links.yml/badge.svg)](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/links.yml)
[![examples](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/examples.yml/badge.svg)](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/examples.yml)
[![field guide](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/pages.yml/badge.svg)](https://github.com/shivamnegi92/awesome-entity-extraction/actions/workflows/pages.yml)

![Entity extraction: text in, structured entities out](assets/demo.gif)

A curated map of maintained tools, models, libraries, datasets, and learning
resources for extracting entities, relations, and structured data from text and
documents. Includes ten isolated examples and an evidence-aware chooser.

**Start with a task:** use the Quick Start below, browse the catalog, or open the
standalone example index. Recommendations are starting points—not endorsements
or universal rankings. The Field Guide's two synthetic task cards each have one
recorded, reproducible run with its misses written up; six-case fixtures
describe behaviour, and this repository makes no benchmark claims.

**Quick Start: choose by constraint**

- **Common English person/company/place spans:** start with spaCy's small English model. Its label set is fixed; domain recall varies.
- **Custom labels without task-specific training:** try GLiNER. It downloads a model; scores are not calibrated probabilities.
- **Local PII detection/redaction:** try Presidio with configured local recognizers. Missed PII remains possible; this is not a compliance guarantee.
- **Typed fields from messy text, hosted API allowed:** try Instructor with an approved provider. It needs credentials and may cost money; valid schema is not factual correctness.
- **Selectable-text PDF with known layout:** try pdfplumber plus explicit rules. Scanned pages need OCR; layout rules require validation.
- **Scanned/layout-heavy documents:** compare catalogued OCR/layout tools on representative documents; OCR errors propagate to extraction.

See the Field Guide and per-example READMEs for setup, caveats, and requirements.

## Contents

- [🧰 Libraries and Frameworks](#-libraries-and-frameworks)
- [☁️ Cloud and Commercial APIs](#-cloud-and-commercial-apis)
- [🤖 LLM-Based and Structured Extraction](#-llm-based-and-structured-extraction)
- [🎯 Zero-Shot and Modern NER Models](#-zero-shot-and-modern-ner-models)
- [🤗 Ready-to-Use Models (Hugging Face)](#-ready-to-use-models-hugging-face)
- [🔗 Relation and Knowledge Extraction](#-relation-and-knowledge-extraction)
- [🪪 Entity Linking](#-entity-linking)
- [🌍 Multilingual Extraction](#-multilingual-extraction)
- [📄 Document and Layout Extraction](#-document-and-layout-extraction)
- [📅 Temporal, Numeric, and Pattern Extraction](#-temporal-numeric-and-pattern-extraction)
- [🔬 Specialized Extraction](#-specialized-extraction)
- [🏷️ Annotation and Evaluation Tools](#-annotation-and-evaluation-tools)
- [📏 Evaluation, Metrics, and Visualization](#-evaluation-metrics-and-visualization)
- [📊 Datasets and Benchmarks](#-datasets-and-benchmarks)
- [🔗 Related Awesome Lists](#-related-awesome-lists)
- [📚 Tutorials and Learning](#-tutorials-and-learning)
- [Runnable Examples](#runnable-examples)
- [Extraction Field Guide](#extraction-field-guide)
- [Contribute](#contribute)
- [Contributing history](#contributing-history)

## 🧰 Libraries and Frameworks

General-purpose NLP toolkits with strong, production-grade NER components.

- [spaCy](https://github.com/explosion/spaCy) - Industrial-strength NLP in Python; fast, trainable NER pipelines and the `spancat` component for overlapping spans.
- [Hugging Face Transformers](https://github.com/huggingface/transformers) - The model hub and library behind most modern token-classification (NER) models.
- [Flair](https://github.com/flairNLP/flair) - Simple framework with state-of-the-art sequence taggers and contextual string embeddings.
- [Stanza](https://github.com/stanfordnlp/stanza) - Stanford NLP's neural pipeline with NER for 60+ languages.
- [Stanford CoreNLP](https://github.com/stanfordnlp/CoreNLP) - The long-standing Java NLP suite with rule-based and statistical NER.
- [Spark NLP](https://github.com/JohnSnowLabs/spark-nlp) - Scalable NLP for Apache Spark with a large catalog of pretrained NER models.
- [NLTK](https://github.com/nltk/nltk) - The classic Python NLP toolkit; useful for chunking-based entity extraction and teaching.
- [nlp.js](https://github.com/axa-group/nlp.js) - NLP library for Node.js with built-in entity extraction.

## ☁️ Cloud and Commercial APIs

Managed services for teams that want extraction without hosting models.

- [Amazon Comprehend](https://aws.amazon.com/comprehend/) - AWS managed NLP with entity, PII, and key-phrase detection.
- [Google Cloud Natural Language](https://cloud.google.com/natural-language) - Entity, sentiment, and syntax analysis API.
- [Azure AI Language](https://azure.microsoft.com/en-us/products/ai-foundry/tools/language) - Microsoft's NER, PII, and entity-linking service.
- [IBM Watson NLU](https://www.ibm.com/products/natural-language-understanding) - Entity, relation, and keyword extraction API.

## 🤖 LLM-Based and Structured Extraction

The modern default: prompt a model and get back typed, validated structures.

![Structured extraction: prompt and schema produce typed JSON](assets/structured.gif)

- [LangExtract](https://github.com/google/langextract) - Google's library for extracting structured information from text with LLMs, including source grounding.
- [Instructor](https://github.com/567-labs/instructor) - Structured LLM outputs via Pydantic schemas; the de-facto way to extract typed entities.
- [Outlines](https://github.com/dottxt-ai/outlines) - Constrained/structured generation that guarantees the model emits valid schemas.
- [GraphRAG](https://github.com/microsoft/graphrag) - Microsoft's pipeline that extracts entities and relationships from text to build a knowledge graph for RAG.
- [Guidance](https://github.com/guidance-ai/guidance) - Programming paradigm for steering LLMs, including constrained output for reliable extraction.
- [Guardrails](https://github.com/guardrails-ai/guardrails) - Adds structure, type, and quality guarantees to LLM outputs.
- [BAML](https://github.com/BoundaryML/baml) - A language for writing typed LLM functions; strong for schema-first extraction.
- [Marvin](https://github.com/PrefectHQ/marvin) - AI toolkit that turns text into structured Python objects with minimal code.
- [Haystack](https://github.com/deepset-ai/haystack) - LLM orchestration framework with extractive components and structured-output support.
- [kor](https://github.com/eyurtsev/kor) - Prompt-based structured extraction helper for LLMs (LangChain-friendly).
- [spacy-llm](https://github.com/explosion/spacy-llm) - Drop LLM prompts into spaCy pipelines for zero/few-shot NER with no training.
- [Zerox](https://github.com/getomni-ai/zerox) - OCR-then-LLM pipeline that turns documents (PDFs, images) into structured data.
- [jsonformer](https://github.com/1rgs/jsonformer) - Generate guaranteed-valid JSON from LLMs by only sampling the schema's content tokens.
- [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) - Enforce JSON Schema / regex output formats during generation.

## 🎯 Zero-Shot and Modern NER Models

Tag arbitrary entity types with little or no task-specific training.

- [GLiNER](https://github.com/urchade/GLiNER) - Generalist, lightweight model that recognizes any entity type from a label list — zero-shot, runs on CPU.
- [UniversalNER](https://github.com/universal-ner/universal-ner) - Distilled open models targeting open-domain, instruction-following NER.
- [SpanMarker](https://github.com/tomaarsen/SpanMarkerNER) - Framework for training strong span-marker NER models on top of any encoder.
- [GoLLIE](https://github.com/hitz-zentroa/GoLLIE) - Code-LLM that performs zero-shot extraction by following annotation guidelines.
- [Zshot](https://github.com/IBM/zshot) - IBM's zero/few-shot entity and relation extraction framework that plugs into spaCy.

**Choosing an approach** — a quick, opinionated map (not a benchmark — pick by fit):

| Approach                        | Zero-shot | Training needed | Best for                                   |
| ------------------------------- | --------- | --------------- | ------------------------------------------ |
| **GLiNER**                      | Yes       | No              | Fast custom entity types, on-device / CPU  |
| **SpanMarker**                  | No        | Yes (fine-tune) | High accuracy on a fixed, known schema     |
| **UniversalNER / GoLLIE**       | Yes       | No              | Open-domain or guideline-driven extraction |
| **spaCy (trainable)**           | No        | Yes             | Production pipelines with your own labels  |
| **LLM + Instructor / Outlines** | Yes       | No              | Arbitrary structured fields, messy inputs  |

## 🤗 Ready-to-Use Models (Hugging Face)

Pretrained checkpoints you can `pip install transformers` and run today. Pick by
entity types, language, and size.

- [🤗 GLiNER multi v2.1](https://huggingface.co/urchade/gliner_multi-v2.1) - Multilingual zero-shot GLiNER; name any entity types at inference time.
- [🤗 GLiNER large v2.1](https://huggingface.co/urchade/gliner_large-v2.1) - Larger English-focused GLiNER for higher zero-shot accuracy.
- [🤗 UniNER-7B-all](https://huggingface.co/Universal-NER/UniNER-7B-all) - UniversalNER 7B instruction model for open-domain zero-shot NER.
- [🤗 GoLLIE-7B](https://huggingface.co/HiTZ/GoLLIE-7B) - Guideline-following extraction model based on Code-LLaMA.
- [🤗 NuExtract 1.5](https://huggingface.co/numind/NuExtract-1.5) - Small, fine-tunable model for template-based structured extraction.
- [🤗 NuNER Zero](https://huggingface.co/numind/NuNER_Zero) - Compact zero-shot token-classification NER model.
- [🤗 bert-base-NER](https://huggingface.co/dslim/bert-base-NER) - Classic, reliable English NER baseline (CoNLL-03 types).
- [🤗 bert-large-NER](https://huggingface.co/dslim/bert-large-NER) - Larger variant of the classic English NER baseline.
- [🤗 roberta-large-ner-english](https://huggingface.co/Jean-Baptiste/roberta-large-ner-english) - Strong English NER fine-tuned on RoBERTa-large.
- [🤗 flair/ner-english-large](https://huggingface.co/flair/ner-english-large) - High-accuracy English NER from the Flair team.
- [🤗 gliner_large v2.5 (community)](https://huggingface.co/gliner-community/gliner_large-v2.5) - Apache-2.0 community GLiNER with strong zero-shot accuracy.
- [🤗 gliner_small v2.1](https://huggingface.co/urchade/gliner_small-v2.1) - Tiny GLiNER for edge / low-latency zero-shot NER.
- [🤗 en_core_web_trf](https://huggingface.co/spacy/en_core_web_trf) - spaCy's transformer English pipeline (incl. NER) on the Hub.

## 🔗 Relation and Knowledge Extraction

Beyond spans: pull relationships and triples to build knowledge graphs.

![Relation extraction: subject, relation, object triples](assets/relations.gif)

- [DeepKE](https://github.com/zjunlp/DeepKE) - Knowledge-extraction toolkit for NER, relation, and attribute extraction (standard, low-resource, document-level).
- [OpenNRE](https://github.com/thunlp/OpenNRE) - Open-source package for neural relation extraction.
- [REBEL](https://github.com/Babelscape/rebel) - Relation extraction as end-to-end seq2seq, jointly extracting entities and relations.
- [🤗 rebel-large (model)](https://huggingface.co/Babelscape/rebel-large) - Ready-to-run REBEL checkpoint for end-to-end relation extraction.

## 🪪 Entity Linking

Resolve mentions to canonical knowledge-base entries (e.g. Wikidata).

![Entity linking: a mention resolved to a knowledge-base entry](assets/linking.gif)

- [BLINK](https://github.com/facebookresearch/BLINK) - Entity linking over Wikipedia using a bi-encoder + cross-encoder architecture.
- [GENRE](https://github.com/facebookresearch/GENRE) - Autoregressive entity retrieval/linking that generates the entity name.
- [ReFinED](https://github.com/amazon-science/ReFinED) - Fast, end-to-end entity linking that resolves and types mentions in one pass.

## 🌍 Multilingual Extraction

Entity extraction beyond English.

- [T-NER](https://github.com/asahi417/tner) - Python library and model zoo for multilingual NER with Transformers.
- [WikiNEuRal](https://github.com/Babelscape/wikineural) - Multilingual NER dataset and models combining neural and knowledge-based silver data.
- [🤗 xlm-roberta-base-ner-hrl (model)](https://huggingface.co/Davlan/xlm-roberta-base-ner-hrl) - NER across 10 high-resource languages on XLM-RoBERTa.
- [🤗 wikineural-multilingual-ner (model)](https://huggingface.co/Babelscape/wikineural-multilingual-ner) - Multilingual NER model covering nine languages.
- [🤗 bert-base-multilingual-cased-ner-hrl (model)](https://huggingface.co/Davlan/bert-base-multilingual-cased-ner-hrl) - Multilingual BERT NER across 10 high-resource languages.
- [🤗 camembert-ner (model)](https://huggingface.co/Jean-Baptiste/camembert-ner) - Strong French NER built on CamemBERT.
- [🤗 flair/ner-multi (model)](https://huggingface.co/flair/ner-multi) - Flair multilingual NER across four languages.

## 📄 Document and Layout Extraction

Get entities and structured data out of PDFs, scans, and complex layouts.
See the [six-entry scope and freshness audit](audits/document-layout-2026-10-22.md) for input types and OCR/layout boundaries (checked 2026-10-22).

![Document layout extraction: typed regions detected on a page](assets/layout.gif)

- [Docling](https://github.com/docling-project/docling) - Parse PDFs, DOCX, and more into structured, AI-ready document representations.
- [Marker](https://github.com/datalab-to/marker) - Convert PDFs and documents to clean Markdown/JSON with high fidelity.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Pre-processing library that extracts text and elements from many document types.
- [Surya](https://github.com/datalab-to/surya) - OCR, layout, reading-order, and table recognition across 90+ languages.
- [Nougat](https://github.com/facebookresearch/nougat) - Transformer model that converts scientific PDFs (incl. math) to markup.
- [LayoutParser](https://github.com/Layout-Parser/layout-parser) - Document image layout analysis toolkit with optional OCR agents.
- [Donut](https://github.com/clovaai/donut) - OCR-free document understanding transformer for parsing and extraction.
- [Table Transformer](https://github.com/microsoft/table-transformer) - Detect and extract tables (and their structure) from documents.
- [pdfplumber](https://github.com/jsvine/pdfplumber) - Extract text, tables, and shapes from PDFs; works best on machine-generated PDFs and does not provide OCR.
- [Camelot](https://github.com/camelot-dev/camelot) - Extract tables from text-based PDFs into DataFrames.
- [spacy-layout](https://github.com/explosion/spacy-layout) - Bring Docling-parsed document layout into spaCy pipelines.

## 📅 Temporal, Numeric, and Pattern Extraction

Extract dates, times, quantities, and rule-based patterns.

- [dateparser](https://github.com/scrapinghub/dateparser) - Parse dates and times from human-readable text in many languages.
- [Duckling](https://github.com/facebook/duckling) - Facebook's rule-based parser for dates, times, numbers, amounts, and durations.
- [quantulum3](https://github.com/nielstron/quantulum3) - Extract quantities, units, and measurements from unstructured text.
- [HeidelTime](https://github.com/HeidelTime/heideltime) - Multilingual, cross-domain temporal tagger for normalized time expressions.

## 🔬 Specialized Extraction

Domain- and type-specific extraction.

- [Presidio](https://github.com/microsoft/presidio) - Microsoft's PII detection and de-identification for text and images.
- [scispaCy](https://github.com/allenai/scispacy) - spaCy models for biomedical, scientific, and clinical entity extraction.
- [medspaCy](https://github.com/medspacy/medspacy) - Clinical NLP with spaCy, including context and section detection.
- [KeyBERT](https://github.com/MaartenGr/KeyBERT) - Keyword and keyphrase extraction using BERT embeddings.
- [pke](https://github.com/boudinfl/pke) - Python keyphrase-extraction toolkit (supervised and unsupervised).
- [🤗 biomedical-ner-all (model)](https://huggingface.co/d4data/biomedical-ner-all) - Recognizes 100+ biomedical entity types out of the box.
- [🤗 Medical-NER (model)](https://huggingface.co/blaze999/Medical-NER) - DeBERTa-based clinical NER covering a wide range of medical entities.
- [🤗 gliner_large_bio (model)](https://huggingface.co/urchade/gliner_large_bio-v0.1) - Zero-shot GLiNER tuned for biomedical entities.
- [🤗 gliner_multi_pii (model)](https://huggingface.co/urchade/gliner_multi_pii-v1) - Zero-shot GLiNER specialized for detecting PII entity types.
- [🤗 deberta_finetuned_pii (model)](https://huggingface.co/lakshyakh93/deberta_finetuned_pii) - DeBERTa model fine-tuned to detect a broad set of PII fields.
- [🤗 stanford-deidentifier (model)](https://huggingface.co/StanfordAIMI/stanford-deidentifier-base) - Clinical de-identification model for removing PHI from medical text.
- [🤗 deid_roberta_i2b2 (model)](https://huggingface.co/obi/deid_roberta_i2b2) - RoBERTa model for de-identifying protected health information.
- [🤗 biobert_diseases_ner (model)](https://huggingface.co/alvaroalon2/biobert_diseases_ner) - BioBERT fine-tuned to tag disease mentions.

## 🏷️ Annotation and Evaluation Tools

You still need labeled data for evaluation and fine-tuning.

- [Label Studio](https://github.com/HumanSignal/label-studio) - Multi-type data labeling platform with strong NER/span annotation.
- [doccano](https://github.com/doccano/doccano) - Open-source text annotation tool for NER, classification, and sequence labeling.
- [Argilla](https://github.com/argilla-io/argilla) - Collaboration platform for building and curating NLP/LLM datasets.
- [prodigy-recipes](https://github.com/explosion/prodigy-recipes) - Recipes and examples for Prodigy, the scriptable annotation tool from the spaCy team.
- [brat](https://github.com/nlplab/brat) - Classic web-based tool for rich text annotation, widely used for NER/relations.
- [INCEpTION](https://github.com/inception-project/inception) - Semantic annotation platform with active learning and knowledge-base linking.

## 📏 Evaluation, Metrics, and Visualization

Score your extractor and inspect its output.

- [seqeval](https://github.com/chakki-works/seqeval) - Standard framework for sequence-labeling (NER) evaluation with entity-level F1.
- [nervaluate](https://github.com/MantisAI/nervaluate) - Nuanced NER evaluation (partial, exact, type) following the SemEval scheme.
- [spacy-streamlit](https://github.com/explosion/spacy-streamlit) - Streamlit components to visualize spaCy pipelines and entities.

## 📊 Datasets and Benchmarks

- [IEPile](https://github.com/zjunlp/IEPile) - Large-scale, bilingual information-extraction instruction corpus for training extraction models.
- [Few-NERD](https://github.com/thunlp/Few-NERD) - Large, fine-grained NER dataset with 66 entity types for few-shot evaluation.
- [🤗 CoNLL-2003 (dataset)](https://huggingface.co/datasets/eriktks/conll2003) - The canonical English NER benchmark (PER, ORG, LOC, MISC).
- [🤗 Few-NERD (dataset)](https://huggingface.co/datasets/DFKI-SLT/few-nerd) - Ready-to-load Few-NERD splits on the Hugging Face Hub.
- [entity-recognition-datasets](https://github.com/juand-r/entity-recognition-datasets) - A large, organized index of NER datasets across domains and languages.
- [NLP-progress: NER](https://github.com/sebastianruder/NLP-progress) - A maintained, living leaderboard of state-of-the-art NER results.
- [🤗 MultiNERD](https://huggingface.co/datasets/Babelscape/multinerd) - Multilingual, multi-genre NER dataset spanning 10 languages.
- [🤗 WikiANN](https://huggingface.co/datasets/unimelb-nlp/wikiann) - Cross-lingual NER over 176 languages built from Wikipedia.
- [🤗 OntoNotes 5 (dataset)](https://huggingface.co/datasets/tner/ontonotes5) - Large multi-domain NER dataset with 18 entity types.
- [🤗 MultiCoNER v2](https://huggingface.co/datasets/MultiCoNER/multiconer_v2) - Complex, fine-grained multilingual NER benchmark.
- [🤗 WNUT-17 (dataset)](https://huggingface.co/datasets/leondz/wnut_17) - Emerging and rare entity recognition on noisy user text.
- [🤗 BC5CDR (dataset)](https://huggingface.co/datasets/tner/bc5cdr) - Biomedical chemical and disease NER corpus.
- [🤗 BioNLP 2004 (dataset)](https://huggingface.co/datasets/tner/bionlp2004) - Molecular-biology NER benchmark.
- [🤗 FIN (dataset)](https://huggingface.co/datasets/tner/fin) - Financial-domain NER dataset.
- [🤗 MIT Movie (dataset)](https://huggingface.co/datasets/tner/mit_movie_trivia) - Slot-filling / NER over movie queries.

## 🔗 Related Awesome Lists

- [Awesome Multimodal Extraction](https://github.com/shivamnegi92/awesome-multimodal-extraction) - The multimodal sibling: extracting entities from images + text (VLMs, document AI).
- [Awesome VLM Architectures](https://github.com/gokayfem/awesome-vlm-architectures) - Deep dive on vision-language model architectures.

## 📚 Tutorials and Learning

- [Transformers Tutorials](https://github.com/NielsRogge/Transformers-Tutorials) - Hands-on notebooks including token classification / NER with Transformers.

## Runnable Examples

Ten independent, end-to-end demos cover general and zero-shot NER, structured
LLM extraction, PII redaction, relation triples, PDF invoice fields, multilingual
NER, temporal/quantity parsing, biomedical entities, and entity linking. Each
example has its own setup guide and dependencies.

See the [examples index](examples/README.md) to choose a use case and run it.

## Extraction Field Guide

Need a shortlist rather than another taxonomy? Read the [Field Guide](field_guide/README.md)
for task/constraint recommendations, two synthetic task cards, and clear run-status
caveats. The [static chooser](field_guide/site/index.html) needs no backend. The
task cards have one recorded run each (spaCy on custom NER, Presidio on PII),
with per-case misses. They are tiny synthetic fixtures, not benchmarks.

## Contribute

The [open-source roadmap](OPEN_SOURCE_ROADMAP.md) lists this month's scoped tasks: [good first issues](https://github.com/shivamnegi92/awesome-entity-extraction/issues?q=is%3Aissue+is%3Aopen+label%3Agood-first-issue), [task-card work](https://github.com/shivamnegi92/awesome-entity-extraction/issues?q=is%3Aissue+is%3Aopen+label%3Atask-card), [resource suggestions](https://github.com/shivamnegi92/awesome-entity-extraction/issues/new/choose), and [Discussions](https://github.com/shivamnegi92/awesome-entity-extraction/discussions). You may also [open a PR directly](https://github.com/shivamnegi92/awesome-entity-extraction/compare); issues are optional. See [CONTRIBUTING.md](CONTRIBUTING.md). Use synthetic or redistributable data only.

## Contributing history

See [CONTRIBUTION_HISTORY.md](CONTRIBUTION_HISTORY.md) for project milestones and
community contributions.




To the extent possible under law, the contributors have waived all copyright and
related or neighboring rights to this work.
