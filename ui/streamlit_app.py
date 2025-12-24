import streamlit as st
import requests
import pdfplumber

# =========================
# CONFIG
# =========================
API_URL = "https://resume-ai-saas.onrender.com/analyze"

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide",
    page_icon="🤖"
)

# =========================
# CSS (Layout + Contrast)
# =========================
st.markdown("""
<style>
.metric-box {
    background: linear-gradient(135deg, #4f8bf9, #6fb1fc);
    padding: 26px;
    border-radius: 16px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}
.metric-box h1 {
    color: white !important;
    margin: 0;
}
.chip {
    display: inline-block;
    padding: 6px 14px;
    margin: 6px 6px 0 0;
    background-color: #eef3ff;
    color: #1f2937;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 500;
    border: 1px solid #c7d2fe;
}
@media (prefers-color-scheme: dark) {
    .chip {
        background-color: #1f2937;
        color: #e5e7eb;
        border: 1px solid #374151;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# Helpers
# =========================
def extract_text_from_pdf(uploaded_file):
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        return "\n".join([p for p in pages if p])
    except Exception:
        return None

# =========================
# HEADER
# =========================
st.title("🤖 AI Resume Analyzer")
st.caption("Analyze your resume against a job description using AI")

# =========================
# SIDEBAR (AUTH + MODEL)
# =========================
with st.sidebar:
    st.header("🔐 Configuration")

    api_key = st.text_input(
        "App API Key",
        type="password",
        placeholder="free-key-123"
    )

    llm_api_key = st.text_input(
        "LLM API Key (Groq / OpenAI)",
        type="password"
    )

    provider = st.selectbox(
        "LLM Provider",
        ["groq", "openai"]
    )

    model = st.text_input(
        "Model Name",
        value="llama-3.1-8b-instant" if provider == "groq" else "gpt-4o-mini"
    )

    st.subheader("🔑 Get an LLM API Key")

    st.markdown(
        """
    **Groq (Free & Fast – Recommended)**  
    👉 [Create Groq API Key](https://console.groq.com/keys)
    
    **OpenAI**  
    👉 [Create OpenAI API Key](https://platform.openai.com/api-keys)
    
    ℹ️ Your LLM API key is used **only for this request** and is **never stored**.
    """
    )

    st.markdown("---")
    st.caption("🔒 Keys are never stored")

# =========================
# INPUT SECTION (2 COLUMNS)
# =========================
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("📄 Resume Upload")
    uploaded_resume = st.file_uploader(
        "Upload Resume (PDF only)",
        type=["pdf"]
    )

    resume_text = ""
    if uploaded_resume:
        with st.spinner("Extracting resume text..."):
            extracted = extract_text_from_pdf(uploaded_resume)
            if extracted:
                resume_text = extracted
                st.success("Resume extracted successfully")
                with st.expander("Preview resume text"):
                    st.text_area("", resume_text, height=260)
            else:
                st.error("Failed to extract text")

with right_col:
    st.subheader("🧾 Job Description")
    job_desc_input = st.text_area(
        "Paste job description here",
        height=360
    )

st.divider()

# =========================
# ANALYZE BUTTON
# =========================
analyze_clicked = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

# =========================
# RESULTS SECTION
# =========================
if analyze_clicked:

    if not api_key or not llm_api_key:
        st.error("Please provide API keys in the sidebar.")
    elif not resume_text or not job_desc_input.strip():
        st.error("Resume and Job Description are required.")
    else:
        with st.spinner("Analyzing with AI… ⏳"):

            payload = {
                "resume": resume_text,
                "job_description": job_desc_input,
                "provider": provider,
                "model": model,
                "llm_api_key": llm_api_key
            }

            headers = {"X-API-Key": api_key}

            response = requests.post(
                API_URL,
                json=payload,
                headers=headers,
                timeout=60
            )

        if response.status_code != 200:
            st.error(f"API Error {response.status_code}:\n{response.text}")
        else:
            result = response.json()

            st.success("✅ Analysis completed")

            # =========================
            # MATCH SCORE
            # =========================
            st.subheader("📊 Match Score")
            score = result["match_score"]
            st.progress(score / 100)
            st.markdown(
                f"<div class='metric-box'><h1>{score}%</h1></div>",
                unsafe_allow_html=True
            )

            # =========================
            # STRENGTHS & WEAKNESSES
            # =========================
            sw_col1, sw_col2 = st.columns(2)

            with sw_col1:
                st.subheader("💪 Strengths")
                for s in result["strengths"]:
                    st.success(s)

            with sw_col2:
                st.subheader("⚠️ Weaknesses")
                for w in result["weaknesses"]:
                    st.warning(w)

            # =========================
            # IMPROVEMENTS
            # =========================
            st.subheader("🛠 Improvement Suggestions")
            for s in result["improvement_suggestions"]:
                st.info(s)

            # =========================
            # RESUME IMPROVEMENTS
            # =========================
            ri = result["resume_improvements"]

            st.subheader("📈 Resume Improvements")

            st.markdown("### 🔑 Missing Keywords")
            for kw in ri["missing_keywords"]:
                st.markdown(f"<span class='chip'>{kw}</span>", unsafe_allow_html=True)

            st.markdown("### ✍️ Improved Summary")
            st.write(ri["summary_improvements"])

            st.markdown("### 📐 Quantifiable Metrics")
            for q in ri["quantifiable_metrics"]:
                st.markdown(f"• **{q}**")

            st.markdown("### 🤖 ATS Optimization Tips")
            for tip in ri["ats_optimization"]:
                st.markdown(f"• **{tip}**")

# =========================
# FOOTER
# =========================
st.divider()
st.markdown(
    """
**👨‍💻 Built by:** Gaurav Kumar Pandey  
📧 **Contact:** [gauravpandeygarg123@gmail.com](mailto:gauravpandeygarg123@gmail.com)

Built with ❤️ using **Streamlit + FastAPI + Groq/OpenAI**
"""
)
