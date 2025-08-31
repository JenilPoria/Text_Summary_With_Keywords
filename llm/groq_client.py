import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv 
load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")


groq_llm = ChatGroq(temperature=0.5, api_key=groq_key, model_name="llama3-8b-8192")
