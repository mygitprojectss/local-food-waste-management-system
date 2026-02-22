import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# DB connect
conn = sqlite3.connect("database/food_waste.db")


# Load tables
food = pd.read_sql("SELECT * FROM food_listings", conn)

claims = pd.read_sql("SELECT * FROM claims", conn)

providers = pd.read_sql("SELECT * FROM providers", conn)



# -------------------------------
# 1 Food Type Distribution
# -------------------------------

plt.figure()

food["Food_Type"].value_counts().plot(kind="bar")

plt.title("Food Type Distribution")

plt.xticks(rotation=45)

plt.savefig("visuals/food_type.png")



# -------------------------------
# 2 Claim Status Analysis
# -------------------------------

plt.figure()

claims["Status"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.title("Claim Status Distribution")

plt.savefig("visuals/Claim_Status.png")



# -------------------------------
# 3 Providers per City
# -------------------------------

plt.figure()

providers["City"].value_counts().head(10).plot(kind="bar")

plt.title("Top Provider Cities")

plt.xticks(rotation=45)

# plt.show()
plt.savefig("visuals/City_Provider.png")



conn.close()