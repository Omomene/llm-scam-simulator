import streamlit as st
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    input_key="input",
    output_key="text",
    return_messages=False
)

def play_audio(effect_text):
    if "[SOUND_EFFECT: DOG_BARKING]" in effect_text:
        st.audio("audio/dog_bark.mp3")

    if "[SOUND_EFFECT: DOORBELL]" in effect_text:
        st.audio("audio/doorbell.mp3")

    if "[SOUND_EFFECT: COUGHING]" in effect_text:
        st.audio("audio/coughing.mp3")

    if "[SOUND_EFFECT: TV_BACKGROUND]" in effect_text:
        st.audio("audio/tv_background.mp3")


def get_audience_winner(suggestions):
    return suggestions[0] if suggestions else None
