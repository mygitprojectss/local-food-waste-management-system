import streamlit as st
import sqlite3
import pandas as pd


st.title("🏢 Provider Management")


# ---------------------------
# DATABASE CONNECTION
# ---------------------------

def get_connection():

    return sqlite3.connect("database/food_waste.db")


# ---------------------------
# ADD PROVIDER
# ---------------------------

st.subheader("➕ Add Provider")

with st.form("add_provider"):

    name = st.text_input("Name")

    ptype = st.text_input("Provider Type")

    address = st.text_input("Address")

    city = st.text_input("City")

    contact = st.text_input("Contact")

    submit = st.form_submit_button("Add Provider")


if submit:

    conn = get_connection()

    conn.execute("""

    INSERT INTO providers
    (Name,Type,Address,City,Contact)

    VALUES(?,?,?,?,?)

    """,(name,ptype,address,city,contact))

    conn.commit()

    conn.close()

    st.success("✅ Provider Added Successfully")


# ---------------------------
# VIEW PROVIDERS
# ---------------------------

st.subheader("📋 Provider List")

conn = get_connection()

df = pd.read_sql(

"SELECT * FROM providers",

conn

)

st.dataframe(df,use_container_width=True)

conn.close()


# ---------------------------
# UPDATE PROVIDER CONTACT
# ---------------------------

st.subheader("✏ Update Provider Contact")

update_id = st.number_input(

"Provider ID",

step=1,

format="%d"

)

new_contact = st.text_input("New Contact")

if st.button("Update Provider"):

    conn = get_connection()

    conn.execute(

    "UPDATE providers SET Contact=? WHERE Provider_ID=?",

    (new_contact,update_id)

    )

    conn.commit()

    conn.close()

    st.success("✅ Provider Updated Successfully")


# ---------------------------
# CONTACT VIEW
# ---------------------------

st.subheader("📞 Contact Provider")

contact_id = st.number_input(

"Enter Provider ID",

step=1,

format="%d",

key="contact_provider"

)

if st.button("Get Contact"):

    conn = get_connection()

    result = pd.read_sql(

    "SELECT Name,City,Contact FROM providers WHERE Provider_ID=?",

    conn,

    params=(contact_id,)

    )

    conn.close()

    st.dataframe(result)


# ---------------------------
# DELETE PROVIDER
# ---------------------------

st.subheader("🗑 Delete Provider")

delete_id = st.number_input(

"Delete Provider ID",

step=1,

format="%d",

key="delete_provider"

)

if st.button("Delete Provider"):

    conn = get_connection()

    conn.execute(

    "DELETE FROM providers WHERE Provider_ID=?",

    (delete_id,)

    )

    conn.commit()

    conn.close()

    st.success("🗑 Provider Deleted Successfully")