# Diabetes Prediction Using SVM

I explore a diabetes prediction algorithm using a [Diabetes dataset](https://www.dropbox.com/s/uh7o7uyeghqkhoy/diabetes.csv?dl=0). Using a Support Vector Machine for my prediction algorithm, I intend on predicting whether an individual has diabetes or not based on certain attributes provided within the dataset headers. 
> This table is taken from [kaggle](https://www.kaggle.com/) and contains data specifying diabetes data from a particular group, which may create difficulty in generalization.

>> "This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to predict based on diagnostic measurements whether a patient has diabetes. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage."

## Overview

With Diabetes becoming a growing health issue in society, I would like to be able to predict to a certain accuracy the probability of an individual being diagnosed with diabetes given certain health attributes. The objective of this project aims to predict whether the person in question has Diabetes or not based on the below elements: 

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree
- Age 

## Workflow

For the purposes of this notebook, I will use a subset of the Diabetes dataset provided by the [following](https://www.dropbox.com/s/uh7o7uyeghqkhoy/diabetes.csv?dl=0). 

1. Begin by collecting Diabetes data and understanding the content of the dataset
2. Preprocess data
3. Train - Test data split
4. Feed a SVM model after determining data subset to be satisfactory
