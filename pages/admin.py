import streamlit as st
import app.pages as pages
import app.generate as generate
import app.utils as utils

# App title
pages.show_home()
pages.show_sidebar()

st.title("🛡️Admin Tooling")
subject_selected, subject = pages.select_subject()

# check for topic
if st.session_state.topic in utils.get_data(subject, 0):
    st.session_state.context = ""
    st.session_state.question = ""
    st.session_state.answer = ""
    st.session_state.topic = ""

# st.subheader("Seed Question:")
seed = st.selectbox(
    "Select a Seed Question:", options=list(utils.get_seed(subject, 0).keys())
)

# st.subheader("New Question:")
# PISA generator
if st.button(":blue[Generate New Data]", key="generate"):
    generate.pisa_question(subject_selected, seed)

if st.session_state.context or st.session_state.question:
    with st.container(border=True):
        st.write(st.session_state.context)
        st.write(f"**Question**: {st.session_state.question}")
        st.markdown(
            f"""<span style="color: blue;">**Answer**: {st.session_state.answer}</span>""",
            unsafe_allow_html=True,
        )

st.subheader("Approve or Reject:")
# Create two columns
col1, col2 = st.columns(2)

# Add a button to each column
with col1:
    if st.button(
        ":blue[Approve]",
        key="approve",
        disabled=st.session_state.answer == "" or st.session_state.context == "",
        use_container_width=True,
    ):
        st.write("Saved to database!")
        utils.save_data(subject)

with col2:
    if st.button(
        ":red[Reject]",
        key="reject",
        disabled=st.session_state.answer == "" or st.session_state.context == "",
        use_container_width=True,
    ):
        st.write("Rejected!")
