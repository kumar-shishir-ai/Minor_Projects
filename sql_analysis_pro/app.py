import mysql.connector
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import json
import pathlib

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shishir@098",
    database="tool",
    port=3306
)
mycursor = mydb.cursor()
# Load lottie image _______________
def load_lottie_file(filepath:str):
    with open(filepath,"rb") as f:
        return json.load(f)
data_lottie = load_lottie_file("database.json")

st.set_page_config(page_title="",layout='wide',page_icon="")
# access css file ______________
def css_file(file_path):
    with open(file_path)as f:
        st.html(f"<style>{f.read()}</style>")

filepath = pathlib.Path("sql.css")
css_file(filepath)

st.markdown("""
<h1 style="color:white;text-align:center;">🗄️ SQL Database Management App</h1>
""",unsafe_allow_html=True)
st.info("This app lets you manage your database records without writing SQL queries manually. Basically Perform Insert ➕, Read 👁️, Update ✏️, Delete 🗑️ operations easily")
option = st.sidebar.selectbox("Select an Operation",("Insert","Read","Update","Delete"))
col = st.columns(2)
with col[0]:
    st_lottie(data_lottie,height=400,width=None)
with col[1]:
    if option == "Insert":
        st.markdown("""
        <h4 style="color:white;text-align:center;border-bottom:1px solid white">Insert a Record</h4>
        """,unsafe_allow_html=True)
        name = st.text_input("**Enter Name**")
        email = st.text_input("**Enter Email**")
        if st.button("📥 Insert",key="insert"):
            sql = "insert into users(name,email)values(%s,%s)"
            val = (name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Insert Successfully ✅")

    elif option == "Read":
        st.markdown("""
            <h4 style="color:white;text-align:center;border-bottom:1px solid white">Read Records</h4>
            """, unsafe_allow_html=True)
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        show = pd.DataFrame(result,columns=["id","name","email"])
        show


    elif option == "Update":
        st.markdown("""
            <h4 style="color:white;text-align:center;border-bottom:1px solid white">Update a Record</h4>
            """, unsafe_allow_html=True)
        emp_id = st.number_input("**Enter ID**",min_value=1)
        name = st.text_input("**Enter new name**")
        email = st.text_input("**Enter new email**")
        if st.button("✏️ Update",key="update"):
            try:
                sql = "update users set name=%s, email=%s where id=%s"
                val = (name,email,emp_id)
                mycursor.execute(sql,val)
                mydb.commit()
                st.success("Record Updated Successfully ✅")
            except Exception as e:
                st.error(e)

    elif option == "Delete":
        st.markdown("""
            <h4 style="color:white;text-align:center;border-bottom:1px solid white">Delete a Record</h4>
            """, unsafe_allow_html=True)
        e_id = st.number_input("**Enter ID**", min_value=1)

        if st.button("🗑️ Delete",key="delete"):
            try:
                sql = "DELETE FROM users WHERE id = %s"
                val = (e_id,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Delete Successfully ✅")
            except Exception as e:
                st.error(e)

st.markdown("---")
st.markdown("""
    <h4 style="color:white;text-align:center;">DataBase All Information</h4>
    """,unsafe_allow_html=True)
c = st.columns(3)
with c[0]:
    with st.expander("**Table Info**"):
        mycursor.execute("describe users")
        result = mycursor.fetchall()
        df = pd.DataFrame(result, columns=["Field", "Type", "Null", "Key", "Default", "Extra"])
        st.dataframe(df)

with c[1]:
    with st.expander("**Construct Table**"):
        mycursor.execute("show create table users")
        re = mycursor.fetchall()
        df = pd.DataFrame(re,columns=["table","construct"])
        df
with c[2]:
    with st.expander("**Counts**"):
        mycursor.execute("select count(*) from users")
        result = mycursor.fetchone()
        st.write(result)
cl = st.columns(3)
with cl[0]:
    with st.expander("**Tables**"):
        mycursor.execute("SHOW TABLES")
        re = mycursor.fetchall()
        df = pd.DataFrame(re)
        df
with cl[1]:
    with st.expander("**DataBases**"):
        mycursor.execute("SHOW DATABASES")
        re = mycursor.fetchall()
        df = pd.DataFrame(re)
        df
with cl[2]:
    with st.expander("**Table Index**"):
        mycursor.execute("SHOW INDEX FROM users")
        re = mycursor.fetchall()
        df = pd.DataFrame(re)
        df

