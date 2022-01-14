import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm


def predict(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age):
    # Loading the dataset to a pandas dataframe
    diabetes_data = pd.read_csv('/Users/jeffshen/Desktop/Diabetes_Prediction/diabetes.csv')

    # Separate data and label
    x = diabetes_data.drop(columns="Outcome", axis=1)
    y = diabetes_data["Outcome"]

    # Data Standardization
    scaler = StandardScaler()
    scaler.fit(x)
    sdata = scaler.transform(x)
    x = sdata

    # Train-Test Split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)
    classifier = svm.SVC(kernel="linear")
    # fit training model to svm classifier
    classifier.fit(x_train, y_train)

    # convert input to numpy array
    data = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age)
    input_array = np.asarray(data)

    # reshape numpy array to predict for one instance
    input_reshape = input_array.reshape(1, -1)
    standard_data = scaler.transform(input_reshape)
    prediction = classifier.predict(standard_data)[0]
    if prediction == 1:
        return "You have Diabetes"
    else:
        return "You don't have Diabetes"
