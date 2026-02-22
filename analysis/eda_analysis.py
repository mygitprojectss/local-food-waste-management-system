import sqlite3
import pandas as pd

# Database connect
conn = sqlite3.connect("database/food_waste.db")

# Load tables

food = pd.read_sql("SELECT * FROM food_listings", conn)

claims = pd.read_sql("SELECT * FROM claims", conn)

receivers = pd.read_sql("SELECT * FROM receivers", conn)

print("Food Listings:", food.shape)
print("Claims:", claims.shape)
print("Receivers:", receivers.shape)

# conn.close()

print("\nFood Columns:")
print(food.columns)

print("\nClaims Columns:")
print(claims.columns)

print("\nReceivers Columns:")
print(receivers.columns)

providers = pd.read_sql("SELECT * FROM providers", conn)

city_analysis = providers.groupby("City").size().sort_values(ascending=False)

print("\nTop Cities Providers Count:\n")

print(city_analysis.head(10))

conn.close()