import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

if __name__ == "__main__":
    response = model.invoke("Two most important ingradient in samosa are ")
    print(response.content)