"""Zero-shot NER with GLiNER -- name your own entity types, no training needed.

Setup:
    pip install gliner
"""
from gliner import GLiNER

model = GLiNER.from_pretrained("urchade/gliner_multi-v2.1")

text = "Tim Cook said Apple will invest $2 billion in Paris by 2026."
labels = ["person", "company", "money", "location", "date"]

for ent in model.predict_entities(text, labels):
    print(f"{ent['text']:18} {ent['label']:10} {ent['score']:.2f}")
