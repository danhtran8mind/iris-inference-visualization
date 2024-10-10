import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
  
# loading in the model to predict on the data 
model_file = open('rf_clf.pkl', 'rb') 
scaler_file = open('scaler.pkl', 'rb') 

classifier = pickle.load(model_file)
scaler = pickle.load(scaler_file)

def welcome(): 
    return 'welcome all'
  
# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(sepal_length, sepal_width, petal_length, petal_width):   
    X_infer = scaler.transform([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = classifier.predict( 
        X_infer) 
    print(prediction) 
    return prediction 
      
  
# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    st.title("IRIS Classifier") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit IRIS Classifier ML App </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction

    # sepal_length,	sepal_width, petal_length, petal_width
    sepal_length = st.text_input("Sepal length", placeholder="Type Sepal length here") 
    sepal_width = st.text_input("Sepal width", placeholder="Type Sepal width here") 
    petal_length = st.text_input("Petal length", placeholder="Type Petal length here") 
    petal_width = st.text_input("Petal width", placeholder="Type Petal width here") 
    # abc = st.sidebar
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(sepal_length, sepal_width, petal_length, petal_width)
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 