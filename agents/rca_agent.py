from llm import get_llm
from core.vectorstore import load_store
from utils.prompts import RCA_PROMPT

def find_rca(query):
    llm = get_llm()
    db = load_store()

    docs = db.similarity_search(query, k=8)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    {RCA_PROMPT}

    CONTEXT:
    {context}

    INCIDENT:
    {query}
    """

    return llm.invoke(prompt).content