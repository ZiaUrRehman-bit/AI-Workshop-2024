import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle as pk

def createModel(iris):
    x = iris.data
    y = iris.target

    # split the data
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, 
                                                    test_size=0.2, random_state=42)
    # train
    model = RandomForestClassifier()
    model.fit(xTrain, yTrain)

    # test the model
    yPred = model.predict(xTest)

    print("Accuracy:", accuracy_score(yTest, yPred))
    print("Classification Report: \n", classification_report(yTest, yPred))

    return model



def main():

    iris = datasets.load_iris()

    model = createModel(iris)

    with open('IrisModel.pkl', 'wb') as f:
        pk.dump(model, f)
        
if __name__ == '__main__':
    main()