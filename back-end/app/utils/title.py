import re


def clean_title(title: str) -> str:
    title = re.sub(r"[^a-zA-Z0-9@&()*\"?.~'!#%]+", " ", title)
    return title.strip().lower()
