import streamlit as st


def show_home():
    st.set_page_config(
        page_title="PISA GenAI",
        page_icon="📝",
        # initial_sidebar_state="collapsed",
    )
    st.logo(
        "https://azure.microsoft.com/svghandler/ai-studio/?width=600&height=315",
        link="https://ai.azure.com/",
    )
    st.title("📝PISA GenAI")

    # question items
    st.subheader("Question:")

    QUESTIONS = {
        "Problem #1": prob1,
        "Problem #2": prob2,
        "Problem #3": prob3,
    }

    page = st.selectbox("Select your question.", options=list(QUESTIONS.keys()))
    return QUESTIONS[page]()


def prob1():
    return st.text_area(
        "1.)",
        "Solve for m: \n3 - 2(9 + 2m) = m",
        height=200,
    )


# https://tutorial.math.lamar.edu/problems/calci/areabetweencurves.aspx
def prob2():
    return st.text_area(
        "2.)",
        "Determine the area below f(x) = 3 + 2x - x^2 and above the x-axis.",
        height=200,
    )


# https://tutorial.math.lamar.edu/classes/de/laplacetransforms.aspx
def prob3():
    return st.text_area(
        "3.)",
        "Find the Laplace transforms of the given function. \nf(t) = 6e^-5t + e^3t + 5t^3 - 9",
        height=200,
    )
