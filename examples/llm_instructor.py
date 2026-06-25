"""Schema-driven extraction with an LLM via Instructor (typed, validated output).

Setup:
    pip install instructor openai
    export OPENAI_API_KEY=...
"""
from typing import Optional

import instructor
from openai import OpenAI
from pydantic import BaseModel


class Entities(BaseModel):
    person: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    amount_usd: Optional[float] = None


client = instructor.from_openai(OpenAI())

result = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=Entities,
    messages=[
        {
            "role": "user",
            "content": "Tim Cook said Apple will invest $2 billion in Paris.",
        }
    ],
)

print(result.model_dump())
# {'person': 'Tim Cook', 'company': 'Apple', 'location': 'Paris', 'amount_usd': 2000000000.0}
