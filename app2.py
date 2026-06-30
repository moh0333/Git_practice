import streamlit as st 
from google import genai

#Gemini chat 
client = genai.Client(
    api_key="your api key"
)

#page confirm
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Study Assitant")

#sidebar
st.sidebar.title("Menu")

if st.sidebar.button("Clear Chat"):
   st.session_state.messages = []
   st.rerun()

#session memory
if "messages" not in st.session_state:
    st.session_state.messages =[]

#display old message
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#chat input
question = st.chat_input("Ask Anything...")

if question:

    #user message
    st.session_state.messages.append(
        {
        "role":"User",
        "content":question

        }
       
    )

    with st.chat_message("assistant"):
     st.markdown(question)

    try:
        
        conversation = ""

        for message in st.session_state.messages:
            conversation += f"{message['role']}: {message['content']}\n"

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=conversation
        )

        answer =response.text

    except Exception as e:
        answer = str(e)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer

        }
    )

    with st.chat_message("assitant"):
        st.markdown(answer)

    
