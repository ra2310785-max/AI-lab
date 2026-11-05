import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
   
]
for text in samples:
    whitespace = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)

    print("Original:", repr(text))
    print("Whitespace:", whitespace, len(whitespace))
    print("Word-like:", words, len(words))
    print()
try:
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2", device="cpu")

    for text in samples[:2]:
        print(text, model.tokenizer.tokenize(text))

except Exception:
    print("Model tokenizer is not available.")