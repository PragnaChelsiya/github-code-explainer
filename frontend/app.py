import streamlit as st
import requests

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Repository Code Explainer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #070b14;
    color: #f5f7ff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b1120;
    border-right: 1px solid #202a3d;
}

section[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.5rem;
}

/* Main content */
.main .block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

/* Text */
h1, h2, h3 {
    color: #f5f7ff !important;
}

p, label {
    color: #aeb8cc !important;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #151936, #1b1d42);
    border: 1px solid #30376b;
    border-radius: 24px;
    padding: 42px;
    margin-bottom: 35px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.25);
}

.badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    background: #17283a;
    border: 1px solid #2c6075;
    color: #8ee8f4;
    font-weight: 700;
    font-size: 13px;
    letter-spacing: 1px;
}

.local-badge {
    margin-top: 12px;
    color: #b7a9ff;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero h1 {
    font-size: 52px;
    font-weight: 800;
    margin: 28px 0 12px 0;
    letter-spacing: -2px;
}

.hero p {
    font-size: 18px;
    color: #b8c2d9 !important;
}

/* Cards */
.card {
    background: #101827;
    border: 1px solid #26334a;
    border-radius: 18px;
    padding: 25px;
    margin: 18px 0;
}

/* Section title */
.section-title {
    font-size: 28px;
    font-weight: 750;
    margin-top: 30px;
    margin-bottom: 10px;
}

/* Status badges */
.status {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 18px;
    font-size: 13px;
    font-weight: 700;
    background: #15251d;
    border: 1px solid #315e43;
    color: #7ce0a1;
}

.engine {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 18px;
    font-size: 13px;
    font-weight: 700;
    background: #171b30;
    border: 1px solid #3d4775;
    color: #b8bfff;
}

/* Input */
.stTextInput input {
    background: #101827 !important;
    color: white !important;
    border: 1px solid #33415c !important;
    border-radius: 12px !important;
    padding: 14px !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background: #151b28;
    color: #f5f7ff;
    border: 1px solid #36445c;
    border-radius: 10px;
    padding: 12px 20px;
    font-weight: 650;
}

.stButton > button:hover {
    border-color: #7282ff;
    color: white;
}

/* Primary button */
button[kind="primary"] {
    background: #4f67e8 !important;
    border: none !important;
    color: white !important;
}

/* Slider */
.stSlider {
    padding: 0 8px;
}

/* Divider */
hr {
    border-color: #253047 !important;
}

/* Code */
code {
    color: #8ee8f4 !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: #101827 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "repository_analyzed" not in st.session_state:
    st.session_state["repository_analyzed"] = False

if "repository_code" not in st.session_state:
    st.session_state["repository_code"] = ""

if "files_analyzed" not in st.session_state:
    st.session_state["files_analyzed"] = []

if "explanation" not in st.session_state:
    st.session_state["explanation"] = ""

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🧠 About This Project")

    st.write(
        "This application analyzes public GitHub repositories "
        "and uses a locally running Qwen model through Ollama "
        "to generate a structured explanation of the repository."
    )

    st.markdown("### Technology Stack")

    st.markdown("""
    <span class="status">Python</span>
    <span class="status">FastAPI</span>
    <span class="status">GitPython</span>
    <span class="status">Ollama</span>
    <span class="status">Qwen 2.5 3B</span>
    <span class="status">Streamlit</span>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("## 🔒 Local AI")

    st.write(
        "Repository analysis and AI generation are performed "
        "locally. Public GitHub content is cloned locally and "
        "processed using Ollama."
    )

    st.write(
        "The application reads repository files and does not "
        "execute the repository's code."
    )

# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<span class="badge">● LOCAL AI · OLLAMA · QWEN</span>

<div class="local-badge">🧠 LOCAL GITHUB</div>

<h1>REPOSITORY CODE EXPLAINER</h1>

<p>
Understand any public GitHub repository with AI-powered
code analysis running entirely on your machine.
</p>

</div>
""", unsafe_allow_html=True)

# ============================================================
# STATUS
# ============================================================

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        '<span class="status">🟢 Local Analysis Ready</span>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<span class="engine">⚡ Engine: Qwen 2.5 3B · Ollama</span>',
        unsafe_allow_html=True
    )

# ============================================================
# REPOSITORY INPUT
# ============================================================

st.markdown(
    '<div class="section-title">GitHub Repository URL</div>',
    unsafe_allow_html=True
)

st.caption(
    "Enter a public GitHub repository URL. No GitHub credentials are required."
)

github_url = st.text_input(
    "Repository URL",
    placeholder="https://github.com/username/repository",
    label_visibility="collapsed"
)

if st.button("🚀 Analyze Repository", type="primary"):

    if not github_url:
        st.warning("Please enter a GitHub repository URL.")

    elif not github_url.startswith("https://github.com/"):
        st.error("Please enter a valid public GitHub repository URL.")

    else:

        with st.spinner(
            "Cloning repository and generating AI explanation..."
        ):

            try:

                response = requests.post(
                    "http://127.0.0.1:8001/explain",
                    json={
                        "github_url": github_url,
                        "temperature": 0.7,
                        "top_k": 40,
                        "top_p": 0.9
                    },
                    timeout=300
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state["repository_code"] = data[
                        "repository_code"
                    ]

                    st.session_state["files_analyzed"] = data[
                        "files_analyzed"
                    ]

                    st.session_state["explanation"] = data[
                        "explanation"
                    ]

                    st.session_state["repository_analyzed"] = True

                    st.success(
                        "Repository analyzed successfully!"
                    )

                else:

                    st.error(
                        f"Backend error: {response.text}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to FastAPI. "
                    "Make sure the backend is running on port 8000."
                )

            except Exception as e:

                st.error(f"Error: {e}")

# ============================================================
# GENERATION PARAMETERS
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">⚙️ LLM Generation Parameters</div>',
    unsafe_allow_html=True
)

st.caption(
    "Experiment with Temperature, Top-k and Top-p to observe "
    "how generation settings affect the model output."
)

col1, col2, col3 = st.columns(3)

with col1:

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.7,
        0.1
    )

with col2:

    top_k = st.slider(
        "Top-k",
        1,
        100,
        40,
        1
    )

with col3:

    top_p = st.slider(
        "Top-p",
        0.1,
        1.0,
        0.9,
        0.1
    )

st.caption(
    f"Current settings → Temperature: {temperature} | "
    f"Top-k: {top_k} | Top-p: {top_p}"
)

# ============================================================
# REGENERATE WITH SETTINGS
# ============================================================

if st.session_state["repository_analyzed"]:

    if st.button("🔄 Regenerate Explanation with Current Settings"):

        with st.spinner("Generating explanation with new parameters..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8001/explain",
                    json={
                        "github_url": github_url,
                        "temperature": temperature,
                        "top_k": top_k,
                        "top_p": top_p
                    },
                    timeout=300
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state["explanation"] = data[
                        "explanation"
                    ]

                    st.session_state["repository_code"] = data[
                        "repository_code"
                    ]

                    st.session_state["files_analyzed"] = data[
                        "files_analyzed"
                    ]

                    st.success(
                        "Explanation regenerated with the selected parameters."
                    )

                else:

                    st.error(f"Backend error: {response.text}")

            except Exception as e:

                st.error(f"Error: {e}")

# ============================================================
# EXPLANATION
# ============================================================

if st.session_state["repository_analyzed"]:

    st.divider()

    st.markdown(
        '<div class="section-title">📊 Structured Repository Explanation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state["explanation"]
    )

    # ========================================================
    # FILES
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">📁 Repository Files Analyzed</div>',
        unsafe_allow_html=True
    )

    st.caption(
        f"{len(st.session_state['files_analyzed'])} relevant files found."
    )

    with st.expander("View analyzed files"):

        for file in st.session_state["files_analyzed"]:
            st.code(file)

    # ========================================================
    # FOLLOW-UP
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">💬 Ask About This Repository</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Ask questions about the repository and get answers based "
        "on its source code."
    )

    question = st.text_input(
        "Your question",
        placeholder="Example: Which file handles the backend API?",
        key="followup_question"
    )

    if st.button("🔎 Ask Question"):

        if not question:

            st.warning("Please enter a question.")

        else:

            with st.spinner("Analyzing repository..."):

                try:

                    response = requests.post(
                        "http://127.0.0.1:8001/followup",
                        json={
                            "repository_code": st.session_state[
                                "repository_code"
                            ],
                            "files": st.session_state[
                                "files_analyzed"
                            ],
                            "question": question,
                            "temperature": temperature,
                            "top_k": top_k,
                            "top_p": top_p
                        },
                        timeout=300
                    )

                    if response.status_code == 200:

                        data = response.json()

                        st.markdown("### 🤖 Answer")

                        st.markdown(data["answer"])

                    else:

                        st.error(
                            f"Backend error: {response.text}"
                        )

                except Exception as e:

                    st.error(f"Error: {e}")

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Repository Code Explainer · Built with Python, FastAPI, "
    "GitPython, Streamlit and Ollama · Local GenAI"
)
