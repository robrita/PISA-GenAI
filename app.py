import streamlit as st
import app.pages as pages
from dotenv import load_dotenv

load_dotenv()

# App title
pages.show_home()
pages.show_sidebar()

# Home page
st.title("✨Welcome to PISA GenAI")
st.image(
    "https://github.com/robrita/PISA-GenAI/blob/main/img/banner.png?raw=true",
    use_column_width=True,
)
st.write(
    "The **PISA Programme for International Student Assessment (PISA)** is an international exam organized by the Organisation for Economic Co-operation and Development (OECD). It assesses the abilities of 15-year-old students in reading, mathematics, and science to gauge how well they can apply their knowledge to real-life situations"
)

st.write(
    "PISA is conducted every three years and aims to provide comparable data to help countries improve their education policies and outcomes2. The results are used to identify strengths and weaknesses in different education systems worldwide"
)
