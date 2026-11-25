
import joblib
import streamlit as st
from urllib.parse import urlparse

st.set_page_config(
    page_title="URL Phishing Detection",
    page_icon="🔐",
    layout="wide"
)

model_info = joblib.load("model_info.pkl")
vectorizer = joblib.load("vectorizer.pkl")

model = model_info["model"]
model_name = model_info["model_name"]

TRUSTED_DOMAINS = {
    "google.com",
    "wikipedia.org",
    "microsoft.com",
    "apple.com",
    "github.com",
    "youtube.com",
    "amazon.com",
    "linkedin.com",
    "facebook.com",
    "instagram.com",
    "example.com"
}


def normalize_url(url):
    url = url.strip()

    if not url.lower().startswith(("http://", "https://")):
        url = "https://" + url

    return url


def extract_domain(url):
    return (urlparse(url).hostname or "").lower().rstrip(".")


def is_trusted_domain(domain):
    return any(
        domain == trusted or domain.endswith("." + trusted)
        for trusted in TRUSTED_DOMAINS
    )


def clear_url():
    st.session_state.url_input = ""
    st.session_state.prediction_result = None


st.session_state.setdefault("prediction_result", None)

st.markdown("""
<style>

.stApp {
    background: #050816 !important;
    color: #f1f5f9 !important;
}

[data-testid="stHeader"] {
    background: #050816 !important;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    color: #ffffff !important;
    font-weight: 900 !important;
}

p, label, span, li {
    color: #f1f5f9;
}

strong, b {
    color: #ffffff !important;
    font-weight: 900 !important;
}

.hero {
    text-align: center;
    padding: 25px 10px 35px;
}

.hero h1 {
    font-size: 44px !important;
    font-weight: 900 !important;
}

.hero h1 span {
    color: #22d3ee !important;
}

.hero p {
    color: #cbd5e1 !important;
    font-size: 20px;
    font-weight: 700;
}

.small-text {
    color: #67e8f9 !important;
    font-size: 16px;
    font-weight: 800;
}

.stTextInput input {
    background: #020617 !important;
    color: #ffffff !important;
    border: 2px solid #38bdf8 !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    min-height: 48px;
}

.stTextInput input::placeholder {
    color: #94a3b8 !important;
}

.stButton > button {
    background: #0f172a !important;
    color: #ffffff !important;
    border: 2px solid #22d3ee !important;
    border-radius: 12px !important;
    min-height: 48px;
    font-weight: 900 !important;
}

.stButton > button p,
.stButton > button span {
    color: #ffffff !important;
    font-weight: 900 !important;
}

.stButton > button:hover {
    background: #164e63 !important;
    border: 2px solid #67e8f9 !important;
}

.feature-card {
    background: #111827;
    border: 2px solid #334155;
    border-radius: 14px;
    height: 125px;
    box-sizing: border-box;
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #ffffff;
    font-weight: 900;
    gap: 10px;
}

.stProgress > div > div > div {
    background: #22d3ee !important;
}

[data-testid="stAlert"] {
    background: #111827 !important;
    border: 1px solid #475569 !important;
}

[data-testid="stAlert"] p {
    color: #ffffff !important;
    font-weight: 800 !important;

}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🔐 URL <span>Phishing</span> Detection System</h1>
    <p>STAY SAFE. BROWSE SMART.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div class="small-text" style="text-align:center;">'
    f'🟢 MODEL: {model_name}</div>',
    unsafe_allow_html=True
)

st.subheader("🔗 ENTER A WEBSITE URL")

col1, col2, col3 = st.columns([6, 1.5, 1])

with col1:
    url = st.text_input(
        "Website URL",
        placeholder="https://example.com",
        key="url_input",
        label_visibility="collapsed"
    )

with col2:
    check_clicked = st.button(
        "🔍 CHECK URL",
        use_container_width=True
    )

with col3:
    st.button(
        "🗑️ CLEAR",
        use_container_width=True,
        on_click=clear_url
    )

if check_clicked:

    if not url.strip():
        st.warning("Please enter a URL.")

    else:
        input_url = normalize_url(url)
        domain = extract_domain(input_url)

        if not domain:
            st.error("Invalid URL. Please enter a valid website address.")

        else:

            if is_trusted_domain(domain):
                prediction = 0
                legitimate_probability = 1.0
                phishing_probability = 0.0

                reason = "Domain matches trusted-domain list."
                source = "Trusted-domain rule"

            else:
                input_data = vectorizer.transform([input_url])

                prediction = model.predict(input_data)[0]
                probabilities = model.predict_proba(input_data)[0]

                classes = list(model.classes_)

                legitimate_index = classes.index(0)
                phishing_index = classes.index(1)

                legitimate_probability = probabilities[legitimate_index]
                phishing_probability = probabilities[phishing_index]

                reason = "Prediction generated using URL patterns."
                source = "Machine Learning Model"

            st.session_state.prediction_result = {
                "prediction": int(prediction),
                "legitimate": float(legitimate_probability),
                "phishing": float(phishing_probability),
                "domain": domain,
                "reason": reason,
                "source": source
            }

result = st.session_state.prediction_result

if result:

    if result["prediction"] == 0:

        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#064e3b,#065f46);
            border:2px solid #34d399;
            border-radius:22px;
            padding:35px;
            text-align:center;
            margin-top:30px;
            box-shadow:0 0 25px rgba(16,185,129,0.15);
        ">
            <div style="font-size:55px;">🛡️</div>
            <div style="
                color:#ffffff;
                font-size:36px;
                font-weight:900;
                margin:12px 0;
            ">LEGITIMATE</div>
            <div style="
                color:#d1fae5;
                font-size:18px;
                font-weight:700;
            ">This URL is likely legitimate</div>
            <div style="
                color:#a7f3d0;
                font-size:14px;
                margin-top:12px;
            ">Domain: {result["domain"]}</div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#7f1d1d,#991b1b);
            border:2px solid #f87171;
            border-radius:22px;
            padding:35px;
            text-align:center;
            margin-top:30px;
            box-shadow:0 0 25px rgba(239,68,68,0.15);
        ">
            <div style="font-size:55px;">⚠️</div>
            <div style="
                color:#ffffff;
                font-size:36px;
                font-weight:900;
                margin:12px 0;
            ">PHISHING DETECTED</div>
            <div style="
                color:#fee2e2;
                font-size:18px;
                font-weight:700;
            ">This URL may be unsafe</div>
            <div style="
                color:#fecaca;
                font-size:14px;
                margin-top:12px;
            ">Domain: {result["domain"]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 PROBABILITY ANALYSIS")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**LEGITIMATE PROBABILITY**")
        st.markdown(
            f"<h2 style='color:#34d399;font-weight:900;'>"
            f"{result['legitimate'] * 100:.2f}%</h2>",
            unsafe_allow_html=True
        )
        st.progress(result["legitimate"])

    with col2:
        st.markdown("**PHISHING PROBABILITY**")
        st.markdown(
            f"<h2 style='color:#f87171;font-weight:900;'>"
            f"{result['phishing'] * 100:.2f}%</h2>",
            unsafe_allow_html=True
        )
        st.progress(result["phishing"])

    st.markdown(f"""
    <div style="
        background:#111827;
        border:1px solid #334155;
        border-radius:14px;
        padding:18px;
        margin-top:15px;
        color:#e2e8f0;
        font-weight:700;
    ">
        <span style="color:#38bdf8;">Detection Method:</span>
        {result["source"]}
        <br><br>
        <span style="color:#38bdf8;">Analysis:</span>
        {result["reason"]}
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 🧠 SYSTEM FEATURES")

features = [
    ("⚡", "FAST PREDICTIONS"),
    ("🛡️", "TRUSTED DOMAINS"),
    ("🤖", "ML DETECTION"),
    ("🔒", "SECURITY ANALYSIS")
]

cols = st.columns(4)

for col, (emoji, title) in zip(cols, features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <div style="font-size:24px;">{emoji}</div>
                <div style="font-size:16px;">{title}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

st.caption(
    "Predictions are based on URL patterns and trusted-domain matching. "
    "They are not a guarantee of website safety."
)
