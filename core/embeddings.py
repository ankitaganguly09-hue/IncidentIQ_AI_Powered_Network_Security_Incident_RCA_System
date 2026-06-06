from langchain_mistralai import MistralAIEmbeddings
from config import MISTRAL_API_KEY

def get_embeddings():
    return MistralAIEmbeddings(
        api_key=MISTRAL_API_KEY,
        model="mistral-embed"
    )