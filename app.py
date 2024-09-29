import streamlit as st
import app.pages as pages
import app.generate as generate
import app.evaluate as evaluate
import app.utils as utils

from dotenv import load_dotenv

load_dotenv()

# App title
pages.show_home()
pages.show_sidebar()

subjects = {
    "Science": "science",
    "Mathematics": "math",
    "Reading": "reading",
    "Financial literacy": "financial_literacy",
    "Creative Thinking": "creative_thinking",
    "Global competence": "global_competence",
    "Collaborative problem solving": "problem_solving",
}

subject_selected = st.selectbox("Select a Subject:", options=list(subjects.keys()))
subject = subjects[subject_selected]

# st.subheader("Seed Question:")
seed = st.selectbox(
    "Select a Seed Question:", options=list(utils.get_seed(subject, 0).keys())
)

if "context_question" not in st.session_state:
    st.session_state.context_question = ""
if "context" not in st.session_state:
    st.session_state.context = ""
if "question" not in st.session_state:
    st.session_state.question = ""
if "answer" not in st.session_state:
    st.session_state.answer = ""

# st.subheader("New Question:")
# PISA generator
button_generate = st.button("Generate New Question", key="generate")
if button_generate:
    st.session_state.context_question = generate.pisa_question(subject_selected, seed)

if st.session_state.context or st.session_state.question:
    with st.container(border=True):
        st.write(st.session_state.context)
        st.write(st.session_state.question)

# st.subheader("Answer:")
if "context_question" in st.session_state:
    st.session_state.answer = st.text_area(
        "Enter your answer here:",
    )

# PISA evaluator
button_evaluate = st.button(
    "Evaluate",
    key="evaluate",
    disabled=st.session_state.answer == "" or st.session_state.context == "",
)
if button_evaluate:
    with st.container(border=True):
        evaluate.pisa_answer()
