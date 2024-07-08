import streamlit as st

def producer_dashboard():
    st.set_page_config(
        page_title="Météo consumer",
        page_icon="🌦️",
        layout="wide",
    )

    st.title("Météo consumer")

    st.write("This is a consumer dashboard")