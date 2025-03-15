import streamlit as st
from google import genai

# Configure the Gemini API
client = genai.Client(api_key="AIzaSyAZprP16aDfi3fxpBMurZc-iSEg5GHIopA")

# Streamlit UI setup
st.set_page_config(page_title="AI Chatbot", page_icon="💬")
st.title("🤖 AI Chatbot")
st.markdown("Type your message below and chat with AI!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask something...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get AI response
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Based on user input give me response in markdown format: "+user_input
    )   
    ai_response = response.text
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    
    with st.chat_message("assistant"):
        st.markdown(ai_response)