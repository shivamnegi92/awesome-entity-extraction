# Contributing to Awesome Entity Extraction

Thanks for helping keep this the most current entity-extraction list on GitHub.

## The rules

1. **It must be real and maintained.** Link to a live project, model, dataset,
   or resource. Dead links and abandoned-years-ago repos get rejected. CI runs
   a link check on every PR.
2. **One line, factual.** Describe what it *does*, not marketing fluff. Format:
   `` - [Name](https://link) - What it does. ``
3. **Right section.** Put it where a reader would look for it. If it spans
   several, pick the primary one.
4. **Keep it relevant.** This list is about extracting entities, relations, and
   structured data from text/documents. General LLM frameworks only belong here
   if extraction is a first-class use case.
5. **Alphabetical-ish / by relevance** within a section. Don't worry about exact
   ordering; a maintainer will tidy it.

## How to add an entry

1. Fork and edit `README.md`.
2. Add your one-line entry under the right heading.
3. Run the link check locally if you can: `python3 scripts/check-links.py`.
4. Open a PR. Briefly say why it belongs.

## What gets rejected

- Dead links, 404s, or repos with no commits in a long time.
- Pure paper dumps with no usable tool/code (this is a practitioner list).
- Self-promotion with no real adoption or usefulness.

That's it. Quality over quantity.
