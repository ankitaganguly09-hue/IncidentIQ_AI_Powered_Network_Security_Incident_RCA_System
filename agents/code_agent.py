from llm import get_llm
from core.vectorstore import load_store
from utils.prompts import CODE_PROMPT

def correlate_code(query):
    llm = get_llm()
    db = load_store()

    docs = db.similarity_search(query, k=6)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    {CODE_PROMPT}

    CODE CONTEXT:
    {context}

    INCIDENT:
    {query}
    """

    return llm.invoke(prompt).content