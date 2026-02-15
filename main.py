import streamlit as st
from app.agents import victim_respond, director_update, moderator_select
from app.utils import play_audio, memory

st.set_page_config(page_title="Dynamic Scam Simulator", layout="wide")
st.title("Dynamic Scam Simulator")

if "memory" not in st.session_state:
    st.session_state.memory = memory
if "current_objective" not in st.session_state:
    st.session_state.current_objective = "Respond politely but slowly"
if "audience_constraint" not in st.session_state:
    st.session_state.audience_constraint = None

script_name = "Tech Support"

user_input = st.text_input("Scammer says:")
audience_input = st.text_area("Audience suggestions (comma separated)")

if st.button("Next Turn") and user_input:
    st.session_state.current_objective = director_update(
        user_input,
        script_name,
        st.session_state.current_objective
    )

    if audience_input:
        suggestions = [x.strip() for x in audience_input.split(",") if x.strip()]
        st.session_state.audience_constraint = moderator_select(suggestions)

    response = victim_respond(
        user_input,
        st.session_state.current_objective,
        st.session_state.audience_constraint
    )

    st.markdown("**Jeanne Dubois responds:**")
    st.markdown(f"```\n{response}\n```")

    play_audio(response)

    st.markdown("**Conversation History:**")
    st.markdown(f"```\n{st.session_state.memory.buffer}\n```")
