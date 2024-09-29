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
        "Your goal is to evaluate the User Answer based on the Given Answer and Question along with it's Context.",
        f"Context: {st.session_state.context}\n",
        f"Question: {st.session_state.question}\n",
        f"Given Answer: {st.session_state.answer}\n",
        f"User Answer: {st.session_state.answer1}\n",
        "# Response JSON Schema and Rubrics:",
        "{",
        "accuracy: The User Answer is correct; value between 0 and 35",
        "relevance: The User Answer should directly address the question; value between 0 and 35",
        "clarity: The User Answer should be clear and easy to understand, avoiding unnecessary jargon; value between 0 and 20",
        "completeness: The User Answer should be thorough, covering all necessary aspects of the question; value between 0 and 10",
        "score: The total score; value between 0 and 100",
        "assessment: Explain concisely the assessment score given; explain step by step",
        "}\n",
        "Response should be in valid JSON format only.",
    ]

    messages = [
        {"role": "system", "content": "\n".join(system)},
    ]

    # st.write(messages)
    return utils.chat(messages, 0, 800, True, "json_object")
