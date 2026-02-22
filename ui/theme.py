import streamlit as st

def apply_theme():

    st.markdown("""

    <style>

    .stApp{

        background-color:#0f172a;
        color:white;

    }

    section[data-testid="stSidebar"]{

        background:#020617;

    }

    h1,h2,h3,h4{

        color:#38bdf8;

    }

    .metric-card{

        background:#020617;

        padding:20px;

        border-radius:12px;

        box-shadow:0 0 12px rgba(56,189,248,0.2);

        text-align:center;

    }

    </style>

    """,

    unsafe_allow_html=True)
