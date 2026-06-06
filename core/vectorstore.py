from langchain_community.vectorstores import Chroma
from core.embeddings import get_embeddings
from config import CHROMA_PATH

def create_store(docs):
    embeddings = get_embeddings()
    db = Chroma.from_texts(
        texts=docs,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    db.persist()
    return db


def load_store():
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )