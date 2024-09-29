import streamlit as st


def show_home():
    st.set_page_config(
        page_title="PISA GenAI",
        page_icon="📝",
        layout="wide",
        # initial_sidebar_state="collapsed",
    )
    st.logo(
        "https://azure.microsoft.com/svghandler/ai-studio/?width=600&height=315",
        link="https://ai.azure.com/",
    )
    st.title("📝PISA GenAI - Admin Tooling / Student Portal")

    st.markdown(
        """
        <style>
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
        st.image(
            "https://github.com/robrita/PISA-GenAI/blob/main/img/pisa-card.jpeg?raw=true",
        )
        st.write(
            "**PISA GenAI** - A tool for generating and evaluating PISA mock exam using LLM."
        )

        st.subheader("🛠Technology Stack", anchor=False)
        st.write("Python, Streamlit, Azure OpenAI")
