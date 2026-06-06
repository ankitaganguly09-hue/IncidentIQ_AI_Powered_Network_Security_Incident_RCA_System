from langchain_mistralai import ChatMistralAI
from config import MISTRAL_API_KEY

def get_llm():
    return ChatMistralAI(
        api_key=MISTRAL_API_KEY,
        model="mistral-large-latest",
        temperature=0.2
    )