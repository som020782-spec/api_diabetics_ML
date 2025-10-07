from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()
origins=[" "]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_cerdientials=True,
   allow_method=["*"],
   headers=["*"])

class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

diabetics_model = pickle.load(open("C:\\Users\\Asus\\Downloads\\sav_file\\diabetes_model.sav", "rb"))

@app.post("/diabetes_prediction")
def diabetes_predict(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dict =json.loads(input_data)
    prg=input_dict['Pregnancies']
    gls=input_dict['Glucose']
    blp=input_dict['BloodPressure']
    skth=input_dict['SkinThickness']
    ins=input_dict['Insulin']
    bmi=input_dict['BMI']
    dpf=input_dict['DiabetesPedigreeFunction']
    age=input_dict['Age']
    
    input_list=[prg,gls,blp,skth,ins,bmi,dpf,age]
       
      
   
    prediction = diabetics_model.predict([input_list])
    if prediction[0] == 0:
        return  "The person is not diabetic"
    else:
        return  "The person is diabetic"
