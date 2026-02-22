import streamlit as st
import sqlite3
import pandas as pd

st.markdown("""

<style>

.metric-card{

background:#020617;

padding:20px;

border-radius:12px;

text-align:center;

box-shadow:0px 0px 12px rgba(56,189,248,0.4);

transition:0.3s;

}

.metric-card:hover{

transform:scale(1.05);

}

</style>

""",unsafe_allow_html=True)


st.image("assets/logo.png",width=140)

st.title("🏠 Dashboard Home")

conn=sqlite3.connect("database/food_waste.db")

food=pd.read_sql("SELECT * FROM food_listings",conn)

claims=pd.read_sql("SELECT * FROM claims",conn)

providers=pd.read_sql("SELECT * FROM providers",conn)

receivers=pd.read_sql("SELECT * FROM receivers",conn)


st.markdown("## Overview")


# c1,c2,c3,c4=st.columns(4)

# c1.metric("🍱 Food Listings",len(food))

# c2.metric("📦 Claims",len(claims))

# c3.metric("🏢 Providers",len(providers))

# c4.metric("🙋 Receivers",len(receivers))

c1,c2,c3,c4=st.columns(4)

c1.markdown(f"""

<div class="metric-card">

<h3>Food Listings</h3>

<h1>{len(food)}</h1>

</div>

""",unsafe_allow_html=True)


c2.markdown(f"""

<div class="metric-card">

<h3>Claims</h3>

<h1>{len(claims)}</h1>

</div>

""",unsafe_allow_html=True)


c3.markdown(f"""

<div class="metric-card">

<h3>Providers</h3>

<h1>{len(providers)}</h1>

</div>

""",unsafe_allow_html=True)


c4.markdown(f"""

<div class="metric-card">

<h3>Receivers</h3>

<h1>{len(receivers)}</h1>

</div>

""",unsafe_allow_html=True)

st.markdown("---")


st.subheader("Application Goal")

st.info("""

Reduce Food Waste.

Connect NGOs and Providers.

Track expiry risk.

Improve distribution success.

""")


conn.close()