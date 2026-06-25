# Submitting to sindresorhus/awesome

Getting listed on the main [Awesome](https://github.com/sindresorhus/awesome)
index is the single biggest discovery driver for a list like this. This repo is
already prepared for it. Here's the exact playbook.

## Status: ready, pending the 30-day rule

The Awesome guidelines require a list to **have existed for at least ~30 days**
before submission. This repo was created today, so the submission is *staged*
but should be opened after that window. Use the time to grow entries and
gather a few stars/contributors (also looked at favorably).

## Pre-flight checklist (all currently satisfied)

- [x] Repo named `awesome-entity-extraction`
- [x] Passes `npx awesome-lint` (also enforced in CI)
- [x] Awesome badge in the heading, linking to https://awesome.re
- [x] Succinct description blockquote at the top
- [x] Table of contents
- [x] Every entry: `- [Name](link) - Factual description.`
- [x] All links verified live (CI re-checks weekly)
- [x] `LICENSE` (CC0) + license footer (no `## License` heading, per awesome-lint)
- [x] `CONTRIBUTING.md`
- [x] `CODE_OF_CONDUCT.md`
- [x] GitHub repo description + topics set (including the `awesome` topic)
- [ ] List is ~30 days old  <-- the only remaining gate
- [ ] ~60+ quality entries (we are here; more is better)

## How to submit (when the window opens)

1. Fork [sindresorhus/awesome](https://github.com/sindresorhus/awesome).
2. Add this entry in the most fitting category, alphabetically. Best fit is the
   data / machine-learning area. Use the `#readme` anchor:

   ```
   - [Entity Extraction](https://github.com/shivamnegi92/awesome-entity-extraction#readme) - Tools and models for extracting entities, relations, and structured data from text.
   ```

3. PR title: `Add Entity Extraction`.
4. Fill in their PR template honestly (it asks you to confirm each checklist item
   above and to link the `awesome-lint` pass).
5. Expect review feedback; address it quickly. Common asks: tighten
   descriptions, prove the list isn't too niche (the LLM-era framing + 60 live
   entries helps here), confirm the 30-day age.

## If they consider it too niche

Fallback discovery that does not depend on their approval:

- Submit to topical indexes (e.g. `awesome-nlp`, `awesome-machine-learning`)
  via their PR processes \u2014 these are easier and still drive traffic.
- Share in r/MachineLearning, r/LanguageTechnology, and relevant Discords.
- A short "the entity-extraction landscape in the LLM era" writeup linking back.
