import streamlit as st

def producer_dashboard():
    st.set_page_config(
        page_title="Météo Producer",
        page_icon="🌦️",
        layout="wide",
    )

    st.title("Météo Producer")

    st.write("This is a producer dashboard")

def consumer_dashboard():
    st.set_page_config(
        page_title="Météo Consumer",
        page_icon="🌦️",
        layout="wide",
    )

    st.title("Météo Consumer")

    st.write("This is a consumer dashboard")