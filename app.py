import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
my_api_key = "AIzaSyC7a8mfgLZAIJFq_xf87KAH9Th1PyfcJIo"

# Configure the generative AI client
genai.configure(api_key=my_api_key)

# Initialize the generative model
llm = genai.GenerativeModel("models/gemini-1.5-flash")

# Start the Streamlit app
st.title("Welcome to the Ai Chatbot")

# Display AI's welcome message
st.chat_message("ai").write("Hi there! I am a helpful AI Assistant. How can I help you today?")

# Capture human input

human_prompt = st.chat_input("Say Something...")

if human_prompt:
    #response = llm.generate_content(text=human_prompt)
    response = llm.generate_content(human_prompt)

    # Display human message
    st.chat_message("human").write(human_prompt)
    
    # Get response from the model
    
    
    st.chat_message("ai").write(response.text)


