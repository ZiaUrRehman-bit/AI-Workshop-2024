import numpy as np
import pandas as pd
import pickle as pk
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report

def createModel(data):
    x = data.drop(['Outcome'], axis=1)
    y = data['Outcome']

    # split the data
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, 
                                                    test_size=0.2)
    # train
    model = svm.SVC(kernel='rbf')
    model.fit(xTrain, yTrain)

    # test the model
    yPred = model.predict(xTest)

    print("Accuracy:", accuracy_score(yTest, yPred)*100)
    print("Classification Report: \n", classification_report(yTest, yPred))

    return model



def main():

    data = pd.read_csv("diabetes.csv")

    model = createModel(data)

    with open('DiabetesModel.pkl', 'wb') as f:
        pk.dump(model, f)
        
if __name__ == '__main__':
    main()