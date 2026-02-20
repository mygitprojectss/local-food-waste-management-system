from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date, DateTime, ForeignKey
from db_connection import engine

metadata = MetaData()

providers = Table(
    "providers",
    metadata,

    Column("Provider_ID", Integer, primary_key=True),
    Column("Name", String),
    Column("Type", String),
    Column("Address", String),
    Column("City", String),
    Column("Contact", String)
)

receivers = Table(

    "receivers",
    metadata,

    Column("Receiver_ID", Integer, primary_key=True),
    Column("Name", String),
    Column("Type", String),
    Column("City", String),
    Column("Contact", String)
)

food_listings = Table(

    "food_listings",
    metadata,

    Column("Food_ID", Integer, primary_key=True),

    Column("Food_Name", String),
    Column("Quantity", Integer),
    Column("Expiry_Date", Date),

    Column(
        "Provider_ID",
        Integer,
        ForeignKey("providers.Provider_ID")
    ),

    Column("Provider_Type", String),
    Column("Location", String),
    Column("Food_Type", String),
    Column("Meal_Type", String)
)

claims = Table(

    "claims",
    metadata,

    Column("Claim_ID", Integer, primary_key=True),

    Column(
        "Food_ID",
        Integer,
        ForeignKey("food_listings.Food_ID")
    ),

    Column(
        "Receiver_ID",
        Integer,
        ForeignKey("receivers.Receiver_ID")
    ),

    Column("Status", String),
    Column("Timestamp", DateTime)
)

metadata.create_all(engine)

print("Tables Created Successfully ✅")