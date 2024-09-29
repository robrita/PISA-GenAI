import json
import streamlit as st
import app.utils as utils


def pisa_answer():
    with st.spinner("Processing ..."):
        results = json.loads(pisa_evaluate())
        st.write(results)
        return results


def pisa_evaluate():
    system = [
        "You are an expert PISA exam evaluator.",
        "Your goal is to evaluate a PISA exam answer based on the given question along with it's context.",
        st.session_state.context,
        st.session_state.question,
        f"**Answer**: {st.session_state.answer}\n",
        "# Response JSON Schema and Rubrics:",
        "{",
        "accuracy: answer is correct; value between 0 and 35",
        "relevance: answer should directly address the question; value between 0 and 35",
        "clarity: answer should be clear and easy to understand, avoiding unnecessary jargon; value between 0 and 20",
        "completeness: answer should be thorough, covering all necessary aspects of the question; value between 0 and 10",
        "score: total score; value between 0 and 100",
        "assessment: explain concisely the assessment score given and provide the correct answer based on your knowledge and data given; explain step by step\n",
        "}",
        "Response should be in valid JSON format only.",
    ]

    messages = [
        {"role": "system", "content": "\n".join(system)},
    ]

    # st.write(messages)
    return utils.chat(messages, 0, 800, True, "json_object")
