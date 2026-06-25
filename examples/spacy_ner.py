"""Named Entity Recognition with spaCy (trained pipeline).

Setup:
    pip install spacy
    python -m spacy download en_core_web_sm
"""
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Tim Cook said Apple will open a store in Paris on March 3, 2026.")

for ent in doc.ents:
    print(f"{ent.text:20} {ent.label_}")
