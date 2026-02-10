import spacy # type: ignore
import re

# Load English language model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """
    Cleans and preprocesses raw text using spaCy.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Process text with spaCy
    doc = nlp(text)

    # Remove stopwords and lemmatize
    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_space
    ]

    return " ".join(tokens)
