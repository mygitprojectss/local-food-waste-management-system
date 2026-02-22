import streamlit as st
from theme import apply_theme


st.set_page_config(

page_title="Food Waste Management",

layout="wide",

initial_sidebar_state="expanded"

)

apply_theme()


st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.sidebar.title("Navigation")


st.title("🍲 Local Food Waste Management System")

st.markdown("""

Welcome Admin.

Manage food donations, receivers,

analysis and SQL insights.

""")