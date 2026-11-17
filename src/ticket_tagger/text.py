def clean_text(text: str) -> str:
    lower_strip = text.lower().strip()
    clean_text = " ".join(lower_strip.split())
    return clean_text
