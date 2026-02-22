import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

st.title("🍲 Local Food Waste Management Dashboard")


# -----------------------------
# DATABASE
# -----------------------------

conn = sqlite3.connect("database/food_waste.db")

food = pd.read_sql("SELECT * FROM food_listings",conn)

claims = pd.read_sql("SELECT * FROM claims",conn)

receivers = pd.read_sql("SELECT * FROM receivers",conn)

providers = pd.read_sql("SELECT * FROM providers",conn)



# -----------------------------
# SIDEBAR FILTERS
# -----------------------------

st.sidebar.header("Filters")


city_list = receivers["City"].dropna().unique()

selected_city = st.sidebar.selectbox(

"Receiver City",

["All"]+list(city_list)

)


food_types = food["Food_Type"].dropna().unique()

selected_food = st.sidebar.selectbox(

"Food Type",

["All"]+list(food_types)

)



# Apply Filter

if selected_city!="All":

    receivers=receivers[receivers["City"]==selected_city]


if selected_food!="All":

    food=food[food["Food_Type"]==selected_food]



# -----------------------------
# KPIs
# -----------------------------

st.header("Overview")

c1,c2,c3,c4=st.columns(4)

c1.metric("Food Listings",len(food))

c2.metric("Claims",len(claims))

c3.metric("Receivers",len(receivers))

c4.metric("Providers",len(providers))



# -----------------------------
# TABS
# -----------------------------

tab1,tab2,tab3,tab4,tab5 = st.tabs([

"Overview",

"Providers",

"Receivers",

"Claims",

"Expiry Risk"

])

# --------------------------------
# TAB 1 OVERVIEW
# --------------------------------

with tab1:

    st.subheader("Food Type Distribution")

    food_counts = food["Food_Type"].value_counts().reset_index()

    food_counts.columns = ["Food_Type","Count"]


    fig = px.bar(

        food_counts,

        x="Food_Type",

        y="Count",

        title="Food Type Distribution"

    )

    st.plotly_chart(fig,use_container_width=True)


# --------------------------------
# TAB 2 PROVIDER ANALYSIS
# --------------------------------

with tab2:

    st.subheader("Top Providers Contribution")

    provider_analysis=pd.read_sql("""

    SELECT p.Name,

    SUM(f.Quantity) as Total_Quantity

    FROM food_listings f

    JOIN providers p

    ON f.Provider_ID=p.Provider_ID

    GROUP BY p.Provider_ID

    ORDER BY Total_Quantity DESC

    LIMIT 10

    """,conn)


    st.dataframe(provider_analysis)



# --------------------------------
# TAB 3 RECEIVER ANALYSIS
# --------------------------------

with tab3:

    st.subheader("Most Active Receivers")

    receiver_claims=pd.read_sql("""

    SELECT r.Name,

    r.City,

    COUNT(c.Claim_ID) as Claims

    FROM claims c

    JOIN receivers r

    ON c.Receiver_ID=r.Receiver_ID

    GROUP BY r.Receiver_ID

    ORDER BY Claims DESC

    LIMIT 10

    """,conn)


    st.dataframe(receiver_claims)



# --------------------------------
# TAB 4 CLAIM ANALYSIS
# --------------------------------

with tab4:

    st.subheader("Claim Status Distribution")

    fig2=px.pie(

        claims,

        names="Status",

        title="Claim Status"

    )

    st.plotly_chart(fig2,use_container_width=True)



# --------------------------------
# TAB 5 EXPIRY RISK
# --------------------------------

with tab5:

    st.subheader("Expiry Risk Food")

    expiry=pd.read_sql("""

    SELECT Food_Type,

    COUNT(*) as Expiring_Items

    FROM food_listings

    GROUP BY Food_Type

    ORDER BY Expiring_Items DESC

    """,conn)


    fig3=px.bar(

        expiry,

        x="Food_Type",

        y="Expiring_Items"

    )

    st.plotly_chart(fig3,use_container_width=True)



conn.close()