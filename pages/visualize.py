import pandas as pd
import streamlit as st
import plotly.express as px
from matplotlib import pyplot as plt
from urllib.error import URLError
from utils.code_utils import show_code
# class DatasetVisualize:
    
def visualize():

    df = pd.read_csv("dataset/iris.csv")

    contact_options = ["Sepal", "Petal", "Length", "Width"]
    contact_selected = st.selectbox("Select a Iris value", contact_options)

    if contact_selected == "Sepal":
        inform = f"Iris {contact_selected} Plot:"
        fig = px.scatter(df, x="sepal.length", y="sepal.width", title=inform, color="variety")
        st.plotly_chart(fig, use_container_width=True)
        # st.write(f"Result of {contact_selected}")

    elif contact_selected == "Petal":
        inform = f"Iris {contact_selected} Plot:"
        fig = px.scatter(df, x="petal.length", y="petal.width", title=inform, color="variety")
        st.plotly_chart(fig, use_container_width=True)
        # st.write(f"Result of {contact_selected}")

    elif contact_selected == "Length":
        inform = f"Iris {contact_selected} Plot:"
        fig = px.scatter(df, x="sepal.length", y="petal.length", title=inform, color="variety")
        st.plotly_chart(fig, use_container_width=True)
        # st.write(f"Result of {contact_selected}")

    elif contact_selected == "Width":
        inform = f"Iris {contact_selected} Plot:"
        fig = px.scatter(df, x="sepal.width", y="petal.width", title=inform, color="variety")
        st.plotly_chart(fig, use_container_width=True)
        # st.write(f"Result of {contact_selected}")

visualize()

show_code(visualize)
    # if __name__ == "__main__":
    #     aa= DatasetVisualize()
    #     aa.visualize()