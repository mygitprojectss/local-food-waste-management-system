import pandas as pd

from sqlalchemy import create_engine


engine = create_engine(
   "sqlite:///database/food_waste.db"
)


# ---------------------
# LOAD PROVIDERS
# ---------------------

providers = pd.read_csv(
    "data/providers_data.csv"
)

providers.to_sql(

    "providers",
    engine,
    if_exists="append",
    index=False
)

print("Providers Loaded ✅")


# ---------------------
# LOAD RECEIVERS
# ---------------------

receivers = pd.read_csv(

    "data/receivers_data.csv"
)

receivers.to_sql(

    "receivers",
    engine,
    if_exists="append",
    index=False
)

print("Receivers Loaded ✅")


# ---------------------
# LOAD FOOD LISTINGS
# ---------------------

food = pd.read_csv(

    "data/food_listings_data.csv"
)

food["Expiry_Date"] = pd.to_datetime(

    food["Expiry_Date"]
).dt.date


food.to_sql(

    "food_listings",
    engine,
    if_exists="append",
    index=False
)

print("Food Listings Loaded ✅")


# ---------------------
# LOAD CLAIMS
# ---------------------

claims = pd.read_csv(

    "data/claims_data.csv"
)

claims["Timestamp"] = pd.to_datetime(

    claims["Timestamp"]
)

claims.to_sql(

    "claims",
    engine,
    if_exists="append",
    index=False
)

print("Claims Loaded ✅")