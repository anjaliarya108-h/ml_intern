import streamlit as st
from graph import process_message

st.title("AutoStream AI Agent")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:")

if user_input:
    response = process_message(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

for role, msg in st.session_state.chat:
    st.write(f"**{role}:** {msg}")