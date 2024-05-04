import streamlit as st
import pandas as pd
import pickle as pk

diabetesData = pd.read_csv("diabetes.csv")

st.write("""
# Diabetes Prediction Application

This app predicts **Diabetes**!
         """)

imageURL = "https://sa1s3optim.patientpop.com/assets/images/provider/photos/2421932.jpg"
st.image(imageURL, caption="Diabetes", use_column_width=True)

st.sidebar.header('User Input Parameter')


def userInputFeatures():
    Pregnancies = st.sidebar.slider('Pregnancies', min(diabetesData['Pregnancies']), max(diabetesData['Pregnancies']), 2)
    Glucose = st.sidebar.slider('Glucose', min(diabetesData['Glucose']), max(diabetesData['Glucose']), 148)
    BloodPressure = st.sidebar.slider('BloodPressure', min(diabetesData['BloodPressure']), max(diabetesData['BloodPressure']), 72)
    SkinThickness = st.sidebar.slider('SkinThickness', min(diabetesData['SkinThickness']), max(diabetesData['SkinThickness']), 35)
    Insulin = st.sidebar.slider('Insulin', min(diabetesData['Insulin']), max(diabetesData['Insulin']), 0)
    BMI = st.sidebar.slider('BMI', min(diabetesData['BMI']), max(diabetesData['BMI']), 33.6)
    DiabetesPedigreeFunction = st.sidebar.slider('DiabetesPedigreeFunction', min(diabetesData['DiabetesPedigreeFunction']), max(diabetesData['DiabetesPedigreeFunction']), 0.627)
    Age = st.sidebar.slider('Age', min(diabetesData['Age']), max(diabetesData['Age']), 50)
    data = {'Pregnancies': Pregnancies,
            'Glucose': Glucose,
            'BloodPressure': BloodPressure,
            'SkinThickness': SkinThickness,
            'Insulin': Insulin,
            'BMI': BMI,
            'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
            'Age': Age,}
    features = pd.DataFrame(data, index=[0])
    return features

def Predistions(inputData):
    model = pk.load(open("DiabetesModel.pkl", "rb"))

    prediction = model.predict(inputData)
    # prediction_proba = model.predict_proba(inputData)

    return prediction

df = userInputFeatures()

GIFImage = 'https://www.rafflesmedicalgroup.com/wp-content/uploads/2023/08/Understanding-Controlling-and-Preventing-diabetes.jpg'
st.sidebar.image(GIFImage, caption="Diabetes", use_column_width=True)

st.subheader('Class labels and their corresponding index number')
st.write(diabetesData.columns)

st.subheader('User Input parameters')
st.write(df)

prediction = Predistions(df)

st.subheader('Prediction')
if prediction == 1:
    st.write("Positive.... You must consult to a doctor")
elif prediction == 0:
    st.write("Negative.... ")
#st.write(prediction)

# st.subheader('Prediction Probability')
# st.write(predictionProb)

st.markdown(
        '''
            # About Me \n
              Hey! this is Engineer **Zia Ur Rehman**.

              If you are interested in building more **AI, Computer Vision and Machine Learning** projects, then visit my GitHub account. You can find a lot of projects with python code.

              - [GitHub](https://github.com/ZiaUrRehman-bit)
              - [LinkedIn](https://www.linkedin.com/in/zia-ur-rehman-217a6212b/) 
              - [Curriculum vitae](https://github.com/ZiaUrRehman-bit/ZiaUrRehman-bit/blob/main/A2023Updated.pdf)
              - [Breast Cancer Predictor Web Application based upon Machine Learning Algorithm](https://breast-cancer-prediction-app-application-yg8ruznblwreqrx293uz4.streamlit.app/)
              
              For any query, You can email me.
              *Email:* engrziaurrehman.kicsit@gmail.com
        '''
    )