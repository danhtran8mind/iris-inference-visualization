import os
import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st
import st_pages
from utils.code_utils import show_code
from urllib.error import URLError


def prediction(scaler, classifier, sepal_length, sepal_width, petal_length, petal_width):   
    X_infer = scaler.transform([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = classifier.predict(X_infer) 
    prob_pre = np.max(classifier.predict_proba(X_infer),axis=1)
    return prediction[0], f"{(prob_pre[0] * 100):.2f} %" # str({(prob_pre[0] * 100):.2f}) + "%"

def load_models():
    model_file = open('saved_models/rf_clf.pkl', 'rb') 
    scaler_file = open('saved_models/scaler.pkl', 'rb') 

    classifier = pickle.load(model_file)
    scaler = pickle.load(scaler_file)

    return scaler, classifier

def update_slider(*pass_key):
        st.session_state[pass_key[0]] = float(st.session_state[pass_key[1]])

def update_numin(*pass_key):
        st.session_state[pass_key[1]] = str(st.session_state[pass_key[0]])  

def ml_inference():
    
    st.title("Model Inference")
    classifier, scaler = load_models()
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit IRIS Classifier ML App </h1> 
    </div> 
    """
    
    # this line allows us to display the front end aspects we have  
    # defined in the above code 

    # loading in the model to predict on the data 
    st.markdown(html_temp, unsafe_allow_html = True) 

    
    sepal_length_s = st.slider(label=f"**Sepal length**",
                            key = 'sepal_length_s', on_change=update_numin, 
                            args=('sepal_length_s','sepal_length'),
                            min_value=4.3, max_value=7.9, value=5.4, step=0.05)
    sepal_length = st.text_input(label="Sepal length i", label_visibility="hidden", key = 'sepal_length',
                                value=5.4, placeholder="Type Sepal length here",
                                on_change = update_slider, args=('sepal_length_s','sepal_length'))

    sepal_width_s = st.slider(label=f"**Sepal width**", key = 'sepal_width_s', on_change= update_numin,
                            args=('sepal_width_s','sepal_width'),
                            min_value=2.0, max_value=4.4, value=3.4, step=0.05)
    sepal_width = st.text_input(label="Sepal width i", label_visibility="hidden", key = 'sepal_width',
                                value=3.4, placeholder="Type Sepal width here",
                                on_change = update_slider, args=('sepal_width_s','sepal_width'))

    petal_length_s = st.slider(label=f"**Petal length**", key = 'petal_length_s', on_change= update_numin,
                            args=('petal_length_s','petal_length'),
                            min_value=1.0, max_value=6.9, value=3.4, step=0.1)
    petal_length = st.text_input(label="Petal length i", label_visibility="hidden", key = 'petal_length',
                                value=3.4, placeholder="Type Petal length here",
                                on_change = update_slider, args=('petal_length_s','petal_length'))

    petal_width_s = st.slider(label=f"**Petal width**", key = 'petal_width_s', on_change= update_numin,
                            args=('petal_width_s','petal_width'),
                            min_value=0.1, max_value=2.5, value=1.4, step=0.1)
    petal_width = st.text_input(label="Petal width i", label_visibility="hidden", key = 'petal_width',
                                value=1.4, placeholder="Type Petal width here",
                                on_change = update_slider, args=('petal_width_s','petal_width'))

    result ="" 
    
    if st.button("Predict"): 
        scaler, classifier = load_models()
        pre, prob = prediction(scaler, classifier, sepal_length, sepal_width, petal_length, petal_width)
        st.success(f'The output is {pre} with confidence is {prob}')   


ml_inference()

show_code(ml_inference)

# if __name__=='__main__':
#     aa = MLInference()
#     aa.ml_inference()