import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
  {"role": "system", "content": "you are a trip adviser"}
]

def communicate():
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    bot_message = response.choices[0].message
    messages.append(bot_message)

    st.session_state["user_input"] = ""

#user interface
st.title ("Trip adviser AI")
st.write ("Utilizing the chatGPT API, this chatbot offers advanced conversational capabilities.")

user_input = st.text_input("please enter a message here.", key = "user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        if isinstance(message, dict):
            speaker = "😎" if message["role"] == "user" else "🤖"
            st.write (speaker + ": " + message["content"])
        else:
            st.write("🤖: " + message.content)
