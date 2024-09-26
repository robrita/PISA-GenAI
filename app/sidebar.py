import streamlit as st


# display the sidebar
def show_sidebar(config: dict):
    st.subheader("⚙️Settings", anchor=False)

    with st.container(border=True):
        model = st.selectbox("Azure OpenAI Model Name:", (config["model"], "gpt-4o"))

    st.write(
        "This app uses the Azure OpenAI API to evaluate math problems and provide solutions."
    )

    st.subheader("🛠Technology Stack", anchor=False)
    st.write("Python, Streamlit, Azure OpenAI, Azure AI")
    st.write(
        "Check out the repo here: [Math AI](https://github.com/robrita/Azure-Math-AI)"
    )

    return model
