import streamlit as st
import app.utils as utils


def show_home():
    st.set_page_config(
        page_title="PISA GenAI",
        page_icon="📝",
        layout="wide",
        # initial_sidebar_state="collapsed",
    )
    st.logo(
        "https://logolook.net/wp-content/uploads/2021/06/DepEd-Logo.svg",
        link="https://ai.azure.com/",
    )
    # Initial states
    if "context" not in st.session_state:
        st.session_state.context = ""
    if "question" not in st.session_state:
        st.session_state.question = ""
    if "answer" not in st.session_state:
        st.session_state.answer = ""
    if "topic" not in st.session_state:
        st.session_state.topic = ""

    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1rem;
            # padding-bottom: 1rem;
            # padding-left: 1rem;
            # padding-right: 1rem;
        }
        .stAppDeployButton {
            display: none;
        }
        .st-emotion-cache-15ecox0 {
            display: none;
        }
        .viewerBadge_container__r5tak {
            display: none;
        }
        .styles_viewerBadge__CvC9N {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# display the sidebar
def show_sidebar():
    with st.sidebar:
        with st.container(border=True):
            st.page_link("app.py", label="Home", icon="🏠")
            st.page_link("pages/user.py", label="Student Portal", icon="🙋")
            st.page_link("pages/admin.py", label="Admin Tooling", icon="🛡️")

        st.image(
            "https://github.com/robrita/PISA-GenAI/blob/main/img/poster.jpeg?raw=true",
        )
        st.write(
            "**PISA GenAI** - A tool for generating and evaluating PISA mock exam using LLM."
        )

        st.image(
            "https://depedtambayan.gumlet.io/wp-content/uploads/2019/09/Slide1.png",
        )

        st.subheader("🛠Technology Stack", anchor=False)
        st.write("Python, Streamlit, Azure OpenAI")


# select subject from dropdown
def select_subject():
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
    return subject_selected, subject
