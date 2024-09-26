import json
import time
import os
import streamlit as st


def show_describe(config: dict, api_key: str, client: object, question: str):
    answer = st.text_area(
        "Enter your answer here.",
        "",
        height=200,
    )

    # Start LLM process
    start_button = st.button("Validate", key="button_text_start", disabled=answer == "")
    st.subheader("Solution:")

    if answer != "" and api_key and start_button:
        with st.spinner("Processing ..."):
            messages = [
                {
                    "role": "system",
                    "content": f"""Solve the following math problem and then evaluate the user input if correct or not.
                    <problem>
                    {question}
                    </problem>
                    Take a deep breath and solve the problem step by step.""",
                },
                {"role": "user", "content": answer},
            ]

        try:
            # Response generation
            full_response = ""
            message_placeholder = st.empty()

            for completion in client.chat.completions.create(
                model=config["model"],
                messages=messages,
                temperature=0,
                max_tokens=1280,
                stream=True,
            ):

                if (
                    completion.choices
                    and completion.choices[0].delta.content is not None
                ):
                    full_response += completion.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

            # Clear results
            if st.button(":red[Clear]", key="button_text_clear"):
                message_placeholder = st.empty()

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        if not answer and start_button:
            st.warning("Please provide your text prompt.")
        if not api_key:
            st.warning("Please provide your OpenAI API key.")
