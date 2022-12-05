import numpy as np 
import joblib 
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocessdata(Gender, Married, Dependent, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Property_Area):

   test_data = [[Gender, Married, Dependent, Education, Self_Employed, ApplicantIncome,
        CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area]]
   trained_model = joblib.load("model.pkl")
   prediction = trained_model.predict(test_data)

   if prediction == 'Y':
      return "Yes"
   else: return "No" 
