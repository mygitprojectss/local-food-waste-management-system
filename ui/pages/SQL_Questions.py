import sys
import os

# FIX IMPORT PATH
sys.path.append(
os.path.abspath(
os.path.join(
os.path.dirname(__file__),
"../../"
)
)
)

import streamlit as st
import plotly.express as px
from analysis.query_runner import run_query


st.title("📊 SQL Analysis Questions")

# ----------------------------------
# ALL PROJECT QUESTIONS
# ----------------------------------

questions={


# -------- FOOD PROVIDERS --------

"1 Providers per City":

"""
SELECT City,
COUNT(*) AS Providers
FROM providers
GROUP BY City
ORDER BY Providers DESC
""",

"2 Provider Type Contribution":

"""
SELECT Provider_Type,
COUNT(*) AS Food_Count
FROM food_listings
GROUP BY Provider_Type
ORDER BY Food_Count DESC
""",

"3 Provider Contact Information":

"""
SELECT Name,
City,
Contact
FROM providers
ORDER BY City
""",

"4 Most Active Receivers":

"""
SELECT r.Name,
COUNT(c.Claim_ID) AS Total_Claims

FROM claims c

JOIN receivers r
ON c.Receiver_ID=r.Receiver_ID

GROUP BY r.Name

ORDER BY Total_Claims DESC

LIMIT 10
""",


# -------- FOOD LISTINGS --------

"5 Total Food Quantity":

"""
SELECT SUM(Quantity) AS Total_Food
FROM food_listings
""",

"6 Highest Listings City":

"""
SELECT Location,
COUNT(*) AS Listings

FROM food_listings

GROUP BY Location

ORDER BY Listings DESC

LIMIT 10
""",

"7 Most Available Food Types":

"""
SELECT Food_Type,
COUNT(*) AS Total

FROM food_listings

GROUP BY Food_Type

ORDER BY Total DESC
""",


# -------- CLAIMS --------

"8 Claims per Food Item":

"""
SELECT Food_ID,
COUNT(*) AS Claims

FROM claims

GROUP BY Food_ID

ORDER BY Claims DESC

LIMIT 10
""",

"9 Provider Highest Claims":

"""
SELECT p.Name,
COUNT(c.Claim_ID) AS Successful_Claims

FROM providers p

JOIN food_listings f
ON p.Provider_ID=f.Provider_ID

JOIN claims c
ON f.Food_ID=c.Food_ID

GROUP BY p.Name

ORDER BY Successful_Claims DESC

LIMIT 10
""",

"10 Claim Status Percentage":

"""
SELECT Status,

COUNT(*)*100.0/
(SELECT COUNT(*) FROM claims)
AS Percentage

FROM claims

GROUP BY Status
""",


# -------- ANALYSIS --------

"11 Avg Food Claimed Receiver":

"""
SELECT r.Name,

AVG(f.Quantity) AS Avg_Claimed

FROM receivers r

JOIN claims c
ON r.Receiver_ID=c.Receiver_ID

JOIN food_listings f
ON f.Food_ID=c.Food_ID

GROUP BY r.Name

ORDER BY Avg_Claimed DESC

LIMIT 10
""",

"12 Most Claimed Meal Type":

"""
SELECT f.Meal_Type,

COUNT(c.Claim_ID) AS Claims

FROM food_listings f

JOIN claims c
ON f.Food_ID=c.Food_ID

GROUP BY f.Meal_Type

ORDER BY Claims DESC
""",

"13 Total Donation per Provider":

"""
SELECT p.Name,

SUM(f.Quantity) AS Total_Donated

FROM providers p

JOIN food_listings f
ON p.Provider_ID=f.Provider_ID

GROUP BY p.Name

ORDER BY Total_Donated DESC

LIMIT 10
"""

}


# ----------------------------------
# SELECT QUESTION
# ----------------------------------

selected=st.selectbox(

"Choose Analysis Question",

list(questions.keys())

)

query=questions[selected]


# ----------------------------------
# RUN QUERY
# ----------------------------------

df=run_query(query)


st.subheader("Result")

st.dataframe(

df,

use_container_width=True

)

csv=df.to_csv(index=False).encode("utf-8")

st.download_button(

"Download Report CSV",

csv,

"analysis_report.csv",

"text/csv"

)
# ----------------------------------
# AUTO VISUALIZATION
# ----------------------------------

if len(df.columns)>=2:

    st.subheader("Visualization")

    fig=px.bar(

        df,

        x=df.columns[0],

        y=df.columns[1],

        title=selected

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )