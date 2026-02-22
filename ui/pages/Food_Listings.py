import streamlit as st
import sqlite3
import pandas as pd


st.title("🍱 Food Listings Management")


def db():

    return sqlite3.connect("database/food_waste.db")


# ADD FOOD

st.subheader("Add Food Listing")

with st.form("add_food"):

    fname=st.text_input("Food Name")

    qty=st.number_input("Quantity",step=1)

    provider=st.number_input("Provider ID",step=1)

    location=st.text_input("Location")

    food_type=st.text_input("Food Type")

    meal=st.selectbox(

    "Meal",

    ["Breakfast","Lunch","Dinner","Snacks"]

    )

    submit=st.form_submit_button("Add")


if submit:

    c=db()

    cur=c.cursor()

    cur.execute("""

    INSERT INTO food_listings

    (Food_Name,Quantity,

    Provider_ID,Location,

    Food_Type,Meal_Type)

    VALUES(?,?,?,?,?,?)

    """,

    (fname,qty,provider,

    location,food_type,meal)

    )

    c.commit()

    c.close()

    st.success("Food Added")


# VIEW

st.subheader("Food Listings")

c=db()

df=pd.read_sql(

"SELECT * FROM food_listings",

c

)

st.dataframe(df,use_container_width=True)


# DELETE

delete_id=st.number_input(

"Food ID",

step=1,

format="%d"

)

if st.button("Delete Food"):

    c=db()

    c.execute(

    "DELETE FROM food_listings WHERE Food_ID=?",

    (delete_id,)

    )

    c.commit()

    c.close()

    st.success("Deleted")