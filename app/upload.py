import os
import base64
import streamlit as st

from tempfile import NamedTemporaryFile


def show_upload(config: dict, api_key: str, client: object, question: str):
    image_upload = st.file_uploader("Upload an image.", type=["png", "jpg", "jpeg"])

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    if image_upload:
        st.image(image_upload, use_column_width=True)
        bytes_data = image_upload.read()

        with NamedTemporaryFile(delete=False) as tmp:
            tmp.write(bytes_data)

    # Start LLM process
    start_button = st.button(
        "Validate", key="button_image_start", disabled=image_upload is None
    )
    st.subheader("Solution:")

    if image_upload is not None and api_key and start_button:
        with st.spinner("Processing ..."):
            base64_image = encode_image(tmp.name)

            messages = [
                {
                    "role": "system",
                    "content": f"""Solve the following math problem and then evaluate the user input if correct or not.
                    <problem>
                    {question}
                    </problem>
                    Take a deep breath and solve the problem step by step.""",
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "This image contains the answer from the user.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                },
            ]

            try:
                # Response generation
                full_response = ""
                message_placeholder = st.empty()

                for completion in client.chat.completions.create(
                    model=config["model"],
                    messages=messages,
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
                if st.button(":red[Clear]", key="button_image_clear"):
                    os.remove(tmp.name)

            except Exception as e:
                st.error(f"An error occurred: {e}")

    else:
        if not image_upload and start_button:
            # if not image_upload and not img and start_button:
            st.warning("Please upload your answer.")
        if not api_key:
            st.warning("Please provide your OpenAI API key.")
