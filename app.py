from logging import debug
from flask import Flask, render_template, request ,flash
import utils  
from utils import preprocessdata 
app = Flask(__name__) 
app.secret_key = "abc"
@app.route('/') 
def home(): 
    return render_template('index.html') 

    
@app.route('/predict', methods=['GET', 'POST'])

def predict():  
    if request.method == 'POST': 
        Gender = request.form.get('Gender')
        Married = request.form.get('Married')
        Dependent = request.form.get('Dependent')
        Education = request.form.get('Education')
        Self_Employed = request.form.get('Self_Employed')  
        ApplicantIncome = request.form.get('ApplicantIncome')  
        CoapplicantIncome = request.form.get('CoapplicantIncome')
        LoanAmount = request.form.get('LoanAmount')
        Loan_Amount_Term = request.form.get('Loan_Amount_Term')   
        Credit_History = request.form.get('Credit_History')   
        Property_Area = request.form.get('Property_Area')
    
    if Gender == 'Male':
        Gender = int(1)
    else:
        Gender = int(0)

    if Married == 'Yes':
        Married = int(1)
    else:
        Married = int(0)

    if Education == 'Graduate':
        Education = int(1)
    else:
        Education = int(0)

    if Self_Employed == 'Yes':
        Self_Employed = int(1)
    else:
        Self_Employed = int(0)
    
    if Property_Area == 'Urban':
        Property_Area = int(1)
    elif Property_Area == 'Semiurban':
        Property_Area = int(2)
    else:
        Property_Area = int(0)
    if Dependent == '0':
        Dependent = int(0)
    elif Dependent =='1':
        Dependent = int(1)
    elif Dependent == '2':
        Dependent= int(2)
    else: 
        Dependent = int(3)       
    if Credit_History == 'Good':
        Credit_History = int(1)
    else:
        Credit_History = int(0)

    ApplicantIncome = int(ApplicantIncome)
    CoapplicantIncome = int(CoapplicantIncome)
    LoanAmount = int(LoanAmount)
    Loan_Amount_Term = int(Loan_Amount_Term)



    prediction = utils.preprocessdata(Gender, Married,Dependent, Education, Self_Employed, ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area)

    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__': 
    app.run(debug=True) 
