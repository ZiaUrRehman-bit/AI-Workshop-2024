import pandas as pd
import pickle as pk
import numpy as np

def Predictions(inputData):
    model = pk.load(open("DiabetesModel.pkl", "rb"))

    prediction = model.predict(inputData)

    return prediction

data = pd.read_csv("diabetes.csv")
x = data.drop(['Outcome'], axis=1)

prediction = Predictions(x[0:1])

if prediction == 1:
    print("Diabetic!!!")
elif prediction == 0:
    print("Not Diabetic...") 