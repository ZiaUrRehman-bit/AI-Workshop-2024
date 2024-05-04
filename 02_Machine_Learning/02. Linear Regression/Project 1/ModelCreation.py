import numpy as np
import pandas as pd
import pickle as pk
from sklearn import linear_model

def createModel(data):

    # Here, you are extracting the 'x' and 'y' columns from the DataFrame data. 
    # In machine learning, 'x' typically represents the input features (independent variable), 
    # and 'y' represents the target variable (dependent variable). 
    x = data['x']
    y = data['y']

    # After extracting the 'x' and 'y' columns, you convert them into NumPy arrays. This step is 
    # important because many machine learning libraries, including scikit-learn (which is used in this script), 
    # expect input data to be in the form of NumPy arrays or similar data structures.

    x = np.array([x]).reshape(-1,1) # The -1 in the first dimension allows NumPy to automatically calculate the 
                                    # number of rows needed to maintain all the elements from the original array.
    y = np.array([y]).reshape(-1,1)

    # The reshape(-1, 1) part is used to reshape the 1-dimensional arrays into column vectors. In scikit-learn, 
    # the input features (x) are expected to be a 2D array, where each row represents a sample, and each column 
    # represents a feature. Reshaping ensures that your 'x' and 'y' arrays are formatted correctly for use with 
    # scikit-learn's LinearRegression model.
    
    # train
    model = linear_model.LinearRegression()
    model.fit(x, y)

    return model

def main():

    data = pd.read_csv("example1.csv")

    model = createModel(data)

    with open('model.pkl', 'wb') as f:
        pk.dump(model, f)
        
if __name__ == '__main__':
    main()