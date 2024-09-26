import streamlit as st
import os
import app.pages
import app.sidebar
import app.describe
import app.upload

from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    # App title
    question = app.pages.show_home()

    # create a config dictionary
    config = {
        "endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
        "api_key": os.environ["AZURE_OPENAI_KEY"],
        "api_version": os.environ["AZURE_OPENAI_API_VERSION"],
        "model": os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
    }

    # Initialize OpenAI client with API key
    api_key = config["api_key"]

    client = AzureOpenAI(
        azure_endpoint=config["endpoint"],
        api_version=config["api_version"],
        api_key=api_key,
    )

    # app sidebar
    with st.sidebar:
        config["model"] = app.sidebar.show_sidebar(config)

    st.subheader("Answer:")
    tab1, tab2 = st.tabs(["✍️Write", "📷Upload"])

    # type the math formula on canvas
    with tab1:
        app.describe.show_describe(config, api_key, client, question)

    # Upload a picture of a math formula
    with tab2:
        app.upload.show_upload(config, api_key, client, question)
