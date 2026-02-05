RISK_VALUES = {"Low": 1, "Medium": 2, "High": 3}


def assess_risk(clause_type, text):
    t = text.lower()

    if clause_type == "Termination":
        if "without notice" in t or "any time" in t:
            return "High", "Allows termination at any time without notice"
        return "Medium", "Termination clause favors one party"

    if clause_type == "Indemnity":
        if "without limitation" in t or "all losses" in t:
            return "High", "Unlimited indemnity obligation"
        return "Medium", "Broad indemnity obligation"

    if clause_type == "Jurisdiction":
        if "india" not in t:
            return "Medium", "Jurisdiction outside India"
        return "Low", "India-based jurisdiction"

    if clause_type == "Auto-Renewal":
        return "Medium", "Automatically renews unless terminated"

    return "Low", "Standard clause"


def calculate_overall_risk(clauses):
    if not clauses:
        return "Low", 0

    avg = sum(RISK_VALUES[c["risk"]] for c in clauses) / len(clauses)

    if avg >= 2.5:
        return "High", avg
    elif avg >= 1.5:
        return "Medium", avg
    return "Low", avg
