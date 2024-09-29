import json
import streamlit as st
import app.utils as utils


def pisa_question(subject, seed):
    with st.spinner("Processing ..."):
        results = json.loads(pisa_generate(subject, seed))
        st.session_state.context = f"**Context**: {results["Context"]}"
        st.session_state.question = f"**Question**: {results["Question"]}"


def pisa_generate(subject, seed):
    system = [
        "You are an expert PISA exam generator.",
        f"Your goal is to generate a PISA exam question along with it's context for {subject} category.",
        "Response should be in valid JSON format only.",
        "# Response JSON Schema",
        "{",
        "Context: The context of the question",
        "Question: The question",
        "}",
        "Generate PISA exam question NOT related to the following topics: ['photosynthesis']"
    ]

    prompt = [
        {"role": "system", "content": "\n".join(system)},
        {
            "role": "user",
            "content": f"Give me a sample PISA question along with context related to {subject}.",
        },
        {"role": "assistant", "content": "\n".join(utils.get_seed(subject, seed))},
    ]

    user = [
        {
            "role": "user",
            "content": f"More practice PISA question related to {subject}.",
        },
    ]

    messages = prompt + user
    st.write(messages)
    return utils.chat(messages, 0.7, 800, True, "json_object")
    
