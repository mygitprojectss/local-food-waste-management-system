import streamlit as st
import sqlite3
import pandas as pd


st.title("🙋 Receiver Management")


# ---------------------------
# DATABASE CONNECTION
# ---------------------------

def get_connection():

    return sqlite3.connect("database/food_waste.db")


# ---------------------------
# ADD RECEIVER
# ---------------------------

st.subheader("➕ Add Receiver")

with st.form("add_receiver"):

    name = st.text_input("Name")

    rtype = st.text_input("Receiver Type")

    city = st.text_input("City")

    contact = st.text_input("Contact")

    submit = st.form_submit_button("Add Receiver")


if submit:

    conn = get_connection()

    conn.execute("""

    INSERT INTO receivers

    (Name,Type,City,Contact)

    VALUES(?,?,?,?)

    """,(name,rtype,city,contact))

    conn.commit()

    conn.close()

    st.success("✅ Receiver Added Successfully")


# ---------------------------
# VIEW RECEIVERS
# ---------------------------

st.subheader("📋 Receiver List")

conn = get_connection()

df = pd.read_sql(

"SELECT * FROM receivers",

conn

)

st.dataframe(df,use_container_width=True)

conn.close()


# ---------------------------
# UPDATE RECEIVER CONTACT
# ---------------------------

st.subheader("✏ Update Receiver Contact")

update_id = st.number_input(

"Receiver ID",

step=1,

format="%d"

)

new_contact = st.text_input("New Contact")

if st.button("Update Receiver"):

    conn = get_connection()

    conn.execute(

    "UPDATE receivers SET Contact=? WHERE Receiver_ID=?",

    (new_contact,update_id)

    )

    conn.commit()

    conn.close()

    st.success("✅ Receiver Updated Successfully")


# ---------------------------
# DELETE RECEIVER
# ---------------------------

st.subheader("🗑 Delete Receiver")

delete_id = st.number_input(

"Delete Receiver ID",

step=1,

format="%d",

key="delete_receiver"

)

if st.button("Delete Receiver"):

    conn = get_connection()

    conn.execute(

    "DELETE FROM receivers WHERE Receiver_ID=?",

    (delete_id,)

    )

    conn.commit()

    conn.close()

    st.success("🗑 Receiver Deleted Successfully")