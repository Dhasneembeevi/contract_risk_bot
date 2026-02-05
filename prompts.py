def explanation_prompt(clause_text, language="English"):
    if language == "Hindi":
        return f"""
नीचे दिए गए अनुबंध क्लॉज़ को सरल व्यावसायिक हिंदी में समझाइए:

क्लॉज़:
{clause_text}
"""
    return f"""
Explain the following contract clause in simple business English:

Clause:
{clause_text}
"""


def suggestion_prompt(clause_text):
    return f"""
Suggest a safer, SME-friendly alternative for the following contract clause:

Clause:
{clause_text}
"""
