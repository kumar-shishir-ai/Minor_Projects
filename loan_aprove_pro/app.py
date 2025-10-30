import pickle
import numpy as np
import pandas as pd
import streamlit as st
import time
import pathlib
import base64

model = pickle.load(open("pipe.pkl","rb"))

columns = [
    'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
    'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
    'Credit_History', 'Property_Area'
]
def data_predict(input_data):
    input_df = pd.DataFrame([input_data], columns=columns)
    result = model.predict(input_df)

    if result[0] == 1:
        return "✅ Congratulations! Based on your details, this loan application is approved by the company."
    else:
        return "❌ Unfortunately, this loan application is not approved by the company."

def main():
    st.title("🏦 Loan Status Prediction App")
    st.info("Welcome to the Loan Status Prediction System!  This app predicts whether a loan application will be *Approved* ✅ or *Rejected* ❌  based on applicant details.")

    # access css file ______________
    def css_file(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    filepath = pathlib.Path("loan.css")
    css_file(filepath)
    with st.sidebar:
        st.title("**Instructions**")
        st.markdown("---")
        Gender = st.selectbox("**Select Gender**",("Male","Female"))
        Married = st.selectbox("**Married**",("Yes","No"))
        Dependents = st.slider("**Dependents**",0,4)
        Education = st.selectbox("**Education**",("Graduate","Not Graduate"))
        Self_Employed = st.selectbox("**Self Employee**",("Yes","No"))
        ApplicantIncome = st.number_input("**Applicant Income**",150,81000,50000)
        CoapplicantIncome = st.number_input("**Coapplicant Income**",0,34000,17000)
        LoanAmount = st.number_input("**Loan Amount**",0,600,200)
        Loan_Amount_Term = st.number_input("**Loan Amount Term**",35,500,150)
        Credit_History = st.slider("**Credit History**",0,1)
        Property_Area = st.selectbox("**Property Area**",("Semiurban","Urban","Rural"))

    if st.button("Predict Now",key='predict'):
        input_features = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome, CoapplicantIncome,LoanAmount, Loan_Amount_Term,Credit_History,Property_Area]

        diagnosis = data_predict(input_features)
        with st.spinner("just wait"):
            time.sleep(2)
        st.success(diagnosis)
if __name__ == '__main__':
    main()