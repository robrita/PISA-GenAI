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

st.title("🙋Student Portal")
subject_selected, subject = pages.select_subject()

topic = st.selectbox("Select a Topic:", options=list(utils.get_data(subject, 0)))

# PISA questions
if topic:
    with st.container(border=True):
        topic_data = utils.get_data(subject, topic)
        st.session_state.context = topic_data["context"]
        st.session_state.question = topic_data["question"]
        st.session_state.answer = topic_data["answer"]
        st.session_state.topic = topic_data["topic"]

        st.write(st.session_state.context)
        st.markdown(
            f"""<span style="color: blue;">**Question**: {st.session_state.question}</span>""",
            unsafe_allow_html=True,
        )

# st.subheader("Answer:")
st.session_state.answer1 = st.text_area(
    "Enter your answer here:",
)

# PISA evaluator
if st.button(
    "Evaluate",
    key="evaluate",
    disabled=st.session_state.answer1 == "",
):
    with st.container(border=True):
        evaluate.pisa_answer()
