import pandas as pd
import pickle as pk
import numpy as np

def Predictions(inputData):
    model = pk.load(open("model.pkl", "rb"))

    prediction = model.predict(inputData)

    return prediction

prediction1 = Predictions([[6]])
prediction2 = Predictions([[7]])
prediction3 = Predictions([[8]])

print(f"Value of y when x = 6: {prediction1}\nValue of y when x = 7: {prediction2}\nValue of y when x = 8: {prediction3}")

data = pd.read_csv("example1.csv")
x = np.array(data['x']).reshape(-1,1)

predVal = Predictions(x)
print(f"Actutal Value of y:\n{data['y']}\nPredicted values of y:\n{predVal}")