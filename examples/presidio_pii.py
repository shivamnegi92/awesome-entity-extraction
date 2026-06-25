"""PII detection and anonymization with Microsoft Presidio.

Setup:
    pip install presidio-analyzer presidio-anonymizer
    python -m spacy download en_core_web_lg
"""
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

text = "Call Jane Doe at 555-123-4567 or jane@example.com."

analyzer = AnalyzerEngine()
results = analyzer.analyze(text=text, language="en")

anonymizer = AnonymizerEngine()
clean = anonymizer.anonymize(text=text, analyzer_results=results)

print(clean.text)
# Call <PERSON> at <PHONE_NUMBER> or <EMAIL_ADDRESS>.
