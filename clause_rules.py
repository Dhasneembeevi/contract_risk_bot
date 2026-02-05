import re

CLAUSE_KEYWORDS = {
    "Termination": ["termination", "terminate"],
    "Indemnity": ["indemnity", "indemnify"],
    "Jurisdiction": ["jurisdiction", "governing law"],
    "Confidentiality": ["confidential"],
    "Auto-Renewal": ["auto", "renew"],
}


def detect_clauses(text):
    detected = []
    blocks = re.split(r"\n?\d+\.\s+", text)
    for block in blocks:
        block_lower = block.lower()
        for clause, keywords in CLAUSE_KEYWORDS.items():
            if any(k in block_lower for k in keywords):
                detected.append({"clause_type": clause, "text": block.strip()})
                break

    return detected
