import streamlit as st
from openai import OpenAI
import anthropic


def get_secret(key):
    try:
        return st.secrets[key]
    except Exception:
        return None


def mock_explanation(prompt):
    p = prompt.lower()

    if "termination" in p:
        return (
            "This clause allows the company to end the contract at any time "
            "without giving advance notice, which can be risky for the service provider."
        )
    if "indemnity" in p:
        return (
            "This clause makes one party responsible for all losses and damages "
            "without any financial limit."
        )
    if "jurisdiction" in p:
        return (
            "This clause decides which country’s courts will handle disputes. "
            "Since it is outside India, legal costs may increase."
        )
    if "confidential" in p:
        return (
            "This clause requires both parties to protect sensitive information "
            "and not share it with others."
        )
    return "This clause explains obligations between the parties."


def mock_suggestion(prompt):
    p = prompt.lower()

    if "termination" in p:
        return (
            "Both parties should be allowed to terminate the agreement "
            "with at least 30 days written notice."
        )

    if "indemnity" in p:
        return (
            "Indemnity obligations should be limited in scope and "
            "capped to a reasonable amount."
        )

    if "jurisdiction" in p:
        return (
            "The agreement should be governed by Indian law with "
            "jurisdiction in Indian courts."
        )

    if "confidential" in p:
        return "Confidentiality obligations should apply equally to both parties."

    return "The clause should be revised to ensure fairness and mutual responsibility."


# OpenAI
def call_openai(prompt, task="explain"):
    api_key = get_secret("OPENAI_API_KEY")
    if not api_key:
        return (
            mock_explanation(prompt) if task == "explain" else mock_suggestion(prompt)
        )

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content

    except Exception:
        return (
            mock_explanation(prompt) if task == "explain" else mock_suggestion(prompt)
        )


# Claude
def call_claude(prompt, task="explain"):
    api_key = get_secret("CLAUDE_API_KEY")
    if not api_key:
        return (
            mock_explanation(prompt) if task == "explain" else mock_suggestion(prompt)
        )

    try:
        client = anthropic.Anthropic(api_key=api_key)

        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text

    except Exception:
        return (
            mock_explanation(prompt) if task == "explain" else mock_suggestion(prompt)
        )


# Router
def call_llm(prompt, provider="OpenAI", demo_mode=False, task="explain"):
    if demo_mode:
        return (
            mock_explanation(prompt) if task == "explain" else mock_suggestion(prompt)
        )
    if provider == "Claude":
        return call_claude(prompt, task=task)
    return call_openai(prompt, task=task)
