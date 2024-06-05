import time
import random
import requests
import streamlit as st
import streamlit.components.v1 as components
from conversation import conversation, conversation_hector, event_mapping


LLM_ENDPOINT = "http://127.0.0.1:8000/base"
conversation_length = len(conversation_hector)
conversation_steps = conversation_hector

custom_component = components.declare_component(
    "mycomponent",
    path="./streamlit-app"
)

with open("./iframe/styles.css", "r") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def generate_response(message):
    data = {
        "id": "streamlit-app-1",
        "message": message
    }

    try:
        response = requests.post(LLM_ENDPOINT, json=data, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        assistant_response = response.json()
    except requests.exceptions.RequestException as e:
        assistant_response = "Hubo un error al obtener respuesta del bot."

    return assistant_response

def get_response(turn):
    return conversation_steps[turn]

def run_app():
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Escriba aqui..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            #assistant_response = generate_response(prompt)
            assistant_response = get_response(st.session_state.turn)
            for letra in assistant_response:
                full_response += letra
                time.sleep(0.02)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

            event = event_mapping.get(int(st.session_state.turn))
            if event:
                value = custom_component(action=event[0], id_product=event[1])
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        st.session_state.turn = (st.session_state.turn + 1) % conversation_length

if __name__ == '__main__':
    
    st.title('Copilot de Compra')
    if "turn" not in st.session_state:
        st.session_state.turn = 0
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    run_app()
