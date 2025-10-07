

import json
import requests


url="http://127.0.0.1:8000/diabetes_prediction"




pregnancies=int(input("number of pregnancies: "))
glucose=int(input("your glucose levels: "))
bloodpressure=int(input("enter your bloodpressure levels: "))
skinthickness=int(input("enter your skin thickness: "))
insulin=int(input("enter your insulin: "))
bmi=float(input("enter your bmi: "))
DiabetesPedigreeFunction=float(input("enter your DiabetesPedigreeFunction: "))
age=float(input("enter your age: "))





input_data_for_model={
    "Pregnancies":pregnancies,
    "Glucose":glucose,
    "BloodPressure":bloodpressure,
    "SkinThickness":skinthickness,
    "Insulin":insulin,
    "BMI":bmi,
    "DiabetesPedigreeFunction":DiabetesPedigreeFunction,
    "Age":age
    }





input_json=json.dumps(input_data_for_model)
response=requests.post(url,data=input_json)
print(response.text)
