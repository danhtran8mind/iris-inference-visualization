import os
import pandas as pd 
import numpy as np 
import joblib 
import streamlit as st
from pages.ml_inference import MLInference
from pages.visualize import DatasetVisualize
from utils import show_code

st.set_page_config(page_title="Iris Demonstration", page_icon="🌸")
tab1, tab2 = st.tabs(["Machine Learning Model", "Visualization"])

with tab1:
    # st.set_page_config(page_title="Model Inference", page_icon="🧠")
    ml_infertab = MLInference()
    ml_infertab.ml_inference()
    # show_code(ml_infertab.ml_inference)

with tab2:
    # st.set_page_config(page_title="Iris Visualization", page_icon="📈")
    visual_tab = DatasetVisualize()
    visual_tab.visualize()
    # show_code(visual_tab.visualize)