import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Maven Cafe",
    page_icon="☕",
)



st.title("Maven Rewards Challenge")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/54c48388-2fa8-4e3b-ba5c-19a93e9bbe7f/0V6Js4r23V.json")

with st.container():  
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
       st.markdown("""
    <div style="text-align: justify; font-size:24px;">
    This project focuses on analyzing customer data for a cafe business, aiming to extract valuable insights 
    that can improve marketing efforts, customer engagement, and overall business performance. 
    The Cafe business offers various types of deals and promotions to their customers through different channels.
    </div>
""", unsafe_allow_html=True)

    with right_column:
        st_lottie(lottie_coding, height=350, key="coding")