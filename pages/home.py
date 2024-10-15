import streamlit as st
from streamlit.logger import get_logger

# LOGGER = get_logger(__name__)


def home_page():

    # giving the webpage a title 
    st.sidebar.title("Introduction")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
# 🌺 Iris Flower Classifier App 🌺

This Streamlit app helps you predict the species of an Iris flower 💐 based on its measurements! 📏

## Features ✨

* **Easy to Use Interface:**  Input flower measurements with simple sliders 🎚️.
* **Accurate Predictions:**  Powered by a trained machine learning model 🧠 for reliable results.
* **Clear Results:**  See the predicted species along with your input measurements 📊.

## How to Run 🚀

1. **Install the Essentials:**
   ```bash
   pip install -r reqiurments.txt
   ```

2. **Start the App:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage 

1. Open the app in your web browser 🌐.
2. Adjust the sliders to enter the sepal and petal measurements.
3. Click "Predict" to see the magic! 🪄
4. The predicted Iris species will be displayed.

## Built With 🛠️

* **Streamlit:**  For building the interactive web app ✨.
* **Scikit-learn:**  For training the machine learning model 🧠.
* **Pandas:**  For handling the Iris dataset 📊.

## Contributing 🤝

Want to help improve the app?  Feel free to open an issue or submit a pull request! 🎉
"""
    )

home_page()
# if __name__ == "__main__":
#     run()
