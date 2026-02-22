import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

st.title("🍲 Local Food Waste Management Dashboard")


# -----------------------
# DB CONNECT
# -----------------------

conn = sqlite3.connect("database/food_waste.db")

food = pd.read_sql("SELECT * FROM food_listings", conn)

claims = pd.read_sql("SELECT * FROM claims", conn)

receivers = pd.read_sql("SELECT * FROM receivers", conn)


# -----------------------
# SIDEBAR FILTER
# -----------------------

st.sidebar.header("Filters")


cities = receivers["City"].unique()

selected_city = st.sidebar.selectbox(

"Select Receiver City",

["All"] + list(cities)

)


if selected_city != "All":

    filtered_receivers = receivers[receivers["City"] == selected_city]

else:

    filtered_receivers = receivers



# -----------------------
# KPI SECTION
# -----------------------

st.header("Overview")

col1,col2,col3 = st.columns(3)

col1.metric("Total Food Listings", len(food))

col2.metric("Total Claims", len(claims))

col3.metric("Total Receivers", len(filtered_receivers))



# -----------------------
# CLAIM STATUS CHART
# -----------------------

st.header("Claim Status")

fig,ax = plt.subplots()

claims["Status"].value_counts().plot(

kind="bar",

ax=ax

)

st.pyplot(fig)



# -----------------------
# FOOD TYPE CHART
# -----------------------

st.header("Food Type Distribution")

fig2,ax2 = plt.subplots()

food["Food_Type"].value_counts().plot(

kind="bar",

ax=ax2

)

plt.xticks(rotation=45)

st.pyplot(fig2)



# -----------------------
# TOP RECEIVERS TABLE
# -----------------------

st.header("Top Receivers")

receiver_claims = pd.read_sql("""

SELECT r.Name,

COUNT(c.Claim_ID) AS Total_Claims

FROM claims c

JOIN receivers r

ON c.Receiver_ID=r.Receiver_ID

GROUP BY r.Receiver_ID

ORDER BY Total_Claims DESC

LIMIT 10

""",conn)

st.dataframe(receiver_claims)



conn.close()