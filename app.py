import streamlit as st

st.title("AI Study Assistent")

question = st.text_area("Ask Anything")

if st.button("Send"):
    st.write("You Asked")
    st.write(question)
    st.success("Message send")