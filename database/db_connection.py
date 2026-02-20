from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///food_waste.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)