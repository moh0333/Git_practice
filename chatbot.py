from google import genai

API_KEY = input("Enter API Key: ")

client = genai.Client(
    api_key=API_KEY
)

while True :
    question = input("you:")
    if question.lower() =="exit":
        print("goodbye!")
        break

    response = client.models.generate_content(
        model ="gemini-2.5-flash",
        contents = question

    )

    print("AI:",response.text)