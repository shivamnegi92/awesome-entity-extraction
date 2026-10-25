# Document and Layout freshness audit

Checked: **2026-10-22**. Scope: six existing entries from the README's Document and Layout Extraction section, for issue #10. No entries added or removed.

`live` means the canonical README was retrieved successfully, its scope was inspected, and GitHub reported `archived: false` on this date. It does **not** certify maintenance responsiveness, model accuracy, dependency compatibility or successful inference. `bot-blocked`, `stale` and `unclear` are reserved for unresolved access, obsolete references and ambiguous evidence respectively; none was needed for these six sources.

## Source and freshness receipt

| Entry | Canonical source snapshot | Checked | Status | Visible release / repository signal |
| --- | --- | --- | --- | --- |
| Docling | [Canonical README](https://github.com/docling-project/docling/blob/main/README.md) ([content snapshot](https://api.github.com/repos/docling-project/docling/git/blobs/3297b7881575dc853facc5add4cc4c8dccc12f14)) | 2026-10-22 | live | Not archived; latest listed release `v2.142.0`. |
| Unstructured | [Canonical README](https://github.com/Unstructured-IO/unstructured/blob/main/README.md) ([content snapshot](https://api.github.com/repos/Unstructured-IO/unstructured/git/blobs/3a6f34957c17d2e065c0ad1e58072cfc2aee4d5d)) | 2026-10-22 | live | Not archived; latest listed release `0.27.33`. |
| Surya | [Canonical README](https://github.com/datalab-to/surya/blob/master/README.md) ([content snapshot](https://api.github.com/repos/datalab-to/surya/git/blobs/861b31625eb6213b41204c0d14d067ab7458cbec)) | 2026-10-22 | live | Not archived; latest listed release `v0.22.1`. |
| pdfplumber | [Canonical README](https://github.com/jsvine/pdfplumber/blob/stable/README.md) ([content snapshot](https://api.github.com/repos/jsvine/pdfplumber/git/blobs/f6f1ce3e0e546b854787aff946601af44fcc6f69)) | 2026-10-22 | live | Not archived; latest listed release `v0.11.10`. |
| LayoutParser | [Canonical README](https://github.com/Layout-Parser/layout-parser/blob/main/README.md) ([content snapshot](https://api.github.com/repos/Layout-Parser/layout-parser/git/blobs/67194e45e70bded6dbb10ed290b5ea904cf490dd)) | 2026-10-22 | live | Not archived; latest listed release `v0.3.4`. |
| Donut | [Canonical README](https://github.com/clovaai/donut/blob/master/README.md) ([content snapshot](https://api.github.com/repos/clovaai/donut/git/blobs/58f3e9fb12c15758d824b106d9c570bc40eacdaa)) | 2026-10-22 | live | Not archived; latest listed release `1.0.9`. |

The six GitHub repository pages and README API responses were accessible. No rename, archive or deprecation banner was visible in the inspected READMEs; this is not an exhaustive support-policy audit. Latest listed release tags are observations, not a freshness ranking. No failure of a HEAD request was used as evidence to delete anything. A future DNS/TLS timeout or bot denial should be recorded as an access limitation and retried with GET/canonical documentation before calling a URL dead.

## Input and extraction boundaries

| Entry | Inputs checked in the source | OCR / layout / table boundary |
| --- | --- | --- |
| Docling | PDF, DOCX, PPTX, XLSX, HTML and images; see the format matrix. | Scanned-input OCR, page layout, reading order and table structure. |
| Unstructured | PDF, images, text, email and other formats via partition functions. | PDF/image processing depends on optional system dependencies; strategies differ. Partitioned elements are not a promise that every table is reconstructed. |
| Surya | Images, PDFs and folders of either. | OCR, reading order and table recognition. Layout/table/OCR use an inference backend; table geometry alone is not cell text extraction. |
| pdfplumber | PDF. | Text/geometry inspection and table extraction; best on machine-generated PDFs. Does not provide OCR. |
| LayoutParser | Document images; also serialized layout data and PDF loading. | Layout detection; OCR is an optional separate agent, e.g. Tesseract. Table OCR is demonstrated, not a universal table parser. |
| Donut | Document images and task-specific training/inference datasets. | OCR-free image-to-structured-output model. No external OCR engine is required; this is not a drop-in generic PDF parser. |

## Resulting catalog corrections

Keep all six entries and their existing canonical project links. Clarify that pdfplumber supplies no OCR, Surya's table component recognizes structure, and LayoutParser's OCR is an optional agent. These distinctions help readers avoid treating a text parser, layout detector and OCR-free trained model as interchangeable. No performance, language-quality or production-readiness claims were evaluated.

This was a source/documentation audit, **not a model run**: no models were downloaded, no hosted inference was called and no extraction output was benchmarked.
