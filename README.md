# 📄 Contract Analysis & Risk Assessment Bot

## 🚀 Problem Statement
Small and medium enterprises (SMEs) often struggle to understand complex legal contracts.  
Hidden clauses, unfair terms, and legal jargon can expose businesses to financial and legal risks.

There is a need for a simple, reliable system that can:
- Identify risky clauses
- Explain them in simple language
- Suggest safer alternatives
- Help SMEs make informed decisions quickly

---

## 💡 Solution
The **Contract Analysis & Risk Assessment Bot** is a GenAI-powered web application that analyzes contract documents and highlights potential risks.

It allows users to:
- Upload a contract (PDF)
- Automatically detect key legal clauses
- Assess risk levels (Low / Medium / High)
- Understand clauses in simple English (and Hindi)
- Receive SME-friendly safer alternatives

The system also includes a **Demo / Mock Mode** to ensure stability when API credits are unavailable.

---

## ✨ Key Features
- 📂 Upload contract documents (PDF)
- 🔍 Clause detection (Termination, Indemnity, Jurisdiction, Confidentiality, etc.)
- ⚠️ Risk classification (Low / Medium / High)
- 📊 Overall contract risk score
- 🗣 Plain-English explanations for non-legal users
- 🇮🇳 Hindi explanation support
- 🛡 Safe fallback mode when API credits are exhausted
- 🌐 Live deployed web application

---

## 🧠 How It Works
1. User uploads a contract PDF
2. Text is extracted and processed
3. Key clauses are detected using rule-based logic
4. Each clause is evaluated for risk
5. GenAI (or demo logic) generates explanations and safer alternatives
6. An overall contract risk score is calculated

---

## 🛠 Tech Stack
- **Frontend & UI:** Streamlit
- **Backend:** Python
- **LLMs:** OpenAI / Claude (optional)
- **PDF Processing:** pdfplumber
- **Deployment:** Streamlit Cloud
- **Version Control:** Git & GitHub

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Dhasneembeevi/contract_risk_bot.git
cd contract_risk_bot
