import streamlit as st
import pdfplumber
from clause_rules import detect_clauses
from risk_engine import assess_risk, calculate_overall_risk
from prompts import explanation_prompt, suggestion_prompt
from sample_contracts import SAMPLE_CONTRACTS
from llm_client import call_llm

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.caption("GenAI-powered legal assistant for Indian SMEs")

st.sidebar.header("⚙️ Settings")

llm_provider = st.sidebar.selectbox("LLM Provider", ["OpenAI", "Claude"])

demo_mode = st.sidebar.toggle("Demo / Mock Mode (No API Calls)", value=False)

language = st.sidebar.selectbox("Explanation Language", ["English", "Hindi"])

st.sidebar.header("📑 Sample Contracts")
sample_choice = st.sidebar.selectbox(
    "Choose sample contract", ["None"] + list(SAMPLE_CONTRACTS.keys())
)
uploaded_file = st.file_uploader("Upload Contract (PDF)", type=["pdf"])


# Text Exaction
def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                # text += page.extract_text() + "\n"
                raw = page.extract_text()
                if raw:
                    raw = raw.replace("\n", " ")
                    text += raw + "\n"
    return text


# Input
contract_text = ""

if sample_choice != "None":
    contract_text = SAMPLE_CONTRACTS[sample_choice]
    st.info(f"Using sample contract: {sample_choice}")

elif uploaded_file:
    contract_text = extract_text(uploaded_file)

# Analysis
if contract_text:
    with st.spinner("Analyzing contract..."):
        detected = detect_clauses(contract_text)

        results = []
        for c in detected:
            risk, reason = assess_risk(c["clause_type"], c["text"])
            results.append(
                {
                    "clause_type": c["clause_type"],
                    "text": c["text"],
                    "risk": risk,
                    "reason": reason,
                }
            )

    overall_risk, score = calculate_overall_risk(results)

    # Risk
    st.subheader("📊 Overall Contract Risk")

    if overall_risk == "High":
        st.error(f"High Risk ⚠️ (Score: {round(score,2)})")
    elif overall_risk == "Medium":
        st.warning(f"Medium Risk ⚠️ (Score: {round(score,2)})")
    else:
        st.success(f"Low Risk ✅ (Score: {round(score,2)})")

    st.subheader("📌 Clause Analysis")

    for r in results:
        icon = "🟢"
        if r["risk"] == "High":
            icon = "🔴"
        elif r["risk"] == "Medium":
            icon = "🟠"

        with st.expander(f"{icon} {r['clause_type']} | Risk: {r['risk']}"):
            st.write("**Original Clause:**")
            st.write(r["text"])

            st.write("**Why Risky:**", r["reason"])

            explanation = call_llm(
                explanation_prompt(r["text"], language),
                provider=llm_provider,
                demo_mode=demo_mode,
                task="explain",
            )

            st.write(f"**Explanation ({language}):**")
            st.write(explanation)

            suggestion = call_llm(
                suggestion_prompt(r["text"]),
                provider=llm_provider,
                demo_mode=demo_mode,
                task="suggest",
            )

            st.write("**Safer Alternative:**")
            st.write(suggestion)
