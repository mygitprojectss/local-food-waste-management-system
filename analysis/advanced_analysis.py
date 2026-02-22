import sqlite3
import pandas as pd


# Connect DB
conn = sqlite3.connect("database/food_waste.db")


food = pd.read_sql("SELECT * FROM food_listings", conn)

claims = pd.read_sql("SELECT * FROM claims", conn)

providers = pd.read_sql("SELECT * FROM providers", conn)

receivers = pd.read_sql("SELECT * FROM receivers", conn)



# -----------------------------------
# 1 Provider Food Contribution
# -----------------------------------

provider_food = food.groupby("Provider_ID")["Quantity"].sum().sort_values(ascending=False)

print("\nTop Food Contributors:\n")

print(provider_food.head(10))



# -----------------------------------
# 2 Claim Status Analysis
# -----------------------------------

claim_status = claims["Status"].value_counts()

print("\nClaim Status Summary:\n")

print(claim_status)



conn.close()