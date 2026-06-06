import streamlit as st

from core.splitter import split_text
from core.vectorstore import create_store

from agents.log_agent import analyze_logs
from agents.rca_agent import find_rca
from agents.code_agent import correlate_code
from agents.fix_agent import suggest_fix
from agents.report_agent import generate_report

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="IncidentIQ",
    page_icon="🧠",
    layout="wide",
)

# -----------------------------
# CUSTOM CSS (SOC / Cisco style)
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #00d4ff;
        text-align: center;
        margin-bottom: 10px;
    }

    .sub-title {
        text-align: center;
        color: #a6b1c2;
        margin-bottom: 30px;
    }

    .card {
        background-color: #111827;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
        margin-bottom: 15px;
    }

    .section-title {
        color: #00d4ff;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="main-title">🧠 IncidentIQ</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-Powered Incident Intelligence for Network Security & SRE Teams</div>', unsafe_allow_html=True)

# -----------------------------
# SIDEBAR (CONTROL PANEL)
# -----------------------------
st.sidebar.title("⚙️ Control Panel")

uploaded_file = st.sidebar.file_uploader("📁 Upload Logs / Ticket / Code", accept_multiple_files=True)

query = st.sidebar.text_area("🧾 Incident Description")

run = st.sidebar.button("🚀 Run RCA Analysis")

st.sidebar.markdown("---")
st.sidebar.markdown("🔐 Secure AI Debugging System")
st.sidebar.markdown("🛰️ SOC / NOC Intelligence Layer")

# -----------------------------
# MAIN EXECUTION
# -----------------------------
if run:

    st.markdown("## 🔍 Incident Analysis Pipeline")

    # Step 1: Ingestion
    with st.spinner("📥 Processing incident data..."):
        if uploaded_file:
            all_text = ""

            for file in uploaded_file:
                content = file.read().decode("utf-8")
                all_text += "\n" + content
            chunks = split_text(all_text)
            create_store(chunks)

    st.success("✔ Data ingestion completed")

    # Step 2: Log Analysis
    st.markdown("### 📊 Log Intelligence Engine")
    with st.spinner("Analyzing logs for anomalies..."):
        logs = analyze_logs(query)
    st.markdown(f'<div class="card">{logs}</div>', unsafe_allow_html=True)

    # Step 3: RCA
    st.markdown("### 🧠 Root Cause Analysis Engine")
    with st.spinner("Identifying root cause..."):
        rca = find_rca(query)
    st.markdown(f'<div class="card">{rca}</div>', unsafe_allow_html=True)

    # Step 4: Code Correlation
    st.markdown("### 💻 Code Intelligence Engine")
    with st.spinner("Mapping logs to codebase..."):
        code = correlate_code(query)
    st.markdown(f'<div class="card">{code}</div>', unsafe_allow_html=True)

    # Step 5: Fix Suggestion
    st.markdown("### 🛠 Remediation Engine")
    with st.spinner("Generating fix recommendations..."):
        fix = suggest_fix(rca, code)
    st.markdown(f'<div class="card">{fix}</div>', unsafe_allow_html=True)

    # Step 6: Final Report
    st.markdown("### 📄 Incident Report Generator")
    with st.spinner("Generating final RCA report..."):
        report = generate_report(rca, fix, logs)
    st.markdown(f'<div class="card">{report}</div>', unsafe_allow_html=True)

    st.success("🎯 RCA Analysis Completed Successfully")