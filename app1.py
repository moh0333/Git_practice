import streamlit as st 
from google import genai

client = genai.Client(
    api_key="your_api_key"
)

st.title("AI Study Assistant")

question = st.text_area("Ask Anything")

if st.button("Send"):
     
    try: 
     
     response = client.models.generate_content(
          model=("gemini-3.1-flash-lite"),
          contents=question
     )

     st.write("### AI answer")
     st.write(response.text)

    except Exception as e:
      st.error(f"error :{e}")
   
