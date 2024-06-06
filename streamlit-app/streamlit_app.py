import time
import streamlit as st
import streamlit.components.v1 as components
from conversation import conversation, event_mapping


custom_component = components.declare_component(
    "mycomponent",
    path="./streamlit-app"
)

with open("./iframe/styles.css", "r") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


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

            event = event_mapping.get(int(st.session_state.turn))
            if event:
                print(event)
                value = custom_component(action=event[0], id_product=event[1])
                
            #assistant_response = generate_response(prompt)
            assistant_response = conversation[st.session_state.turn]
            for letra in assistant_response:
                full_response += letra
                time.sleep(0.02)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)


        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        st.session_state.turn = (st.session_state.turn + 1) % len(conversation)

if __name__ == '__main__':
    
    st.title('Copilot de Compra')
    if "turn" not in st.session_state:
        st.session_state.turn = 0
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    run_app()
