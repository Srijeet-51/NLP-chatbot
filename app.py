import streamlit as st
from chatbot import chatbot_response

# Streamlit page setup
st.set_page_config(page_title="AI Support Chatbot", page_icon="🤖")
st.title("🤖 Customer Support Chatbot")
st.markdown("Type your query below and get real-time support!")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submit = st.form_submit_button("Send")

if submit and user_input:
    # Get bot response
    bot_reply = chatbot_response(user_input)

    # Update session history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑‍💼 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
