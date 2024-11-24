import streamlit as st 
import requests 
from streamlit_lottie import st_lottie




st.set_page_config(page_title="IEEE hackerthon", page_icon=":tada:",layout = "wide")

def load_lottie(url):
     r=requests.get(url)
     if r.status_code!=200:
          return None
     return r.json()

lottie_coding = load_lottie("https://lottie.host/c05053b9-6eee-4e13-8c8d-fd000792df56/pUuy1Rbss7.json")

st.subheader("hii! This is our project :wave:")
st.title(" WE are gonna explore Machine Learning")

st.write("we are passionate about ai and ml")
st.write("[View on Gihub>] (https://github.com/AbhishekO27)")

with st.container():
    st.write("---")
    left_column , right_column =st.columns(2)
    with left_column:
          st.header("WE are working on heart disease detecter")
          st.write("##")



with right_column:
        if lottie_coding:  # Check if Lottie animation is loaded
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Failed to load animation. Please check the URL.")


