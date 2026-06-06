from core.embeddings import get_embeddings
from core.vectorstore import load_store
from utils.prompts import LOG_ANALYSIS_PROMPT
from llm import get_llm

def analyze_logs(query):
    llm = get_llm()
    db = load_store()

    docs = db.similarity_search(query, k=5)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    {LOG_ANALYSIS_PROMPT}

    LOGS:
    {context}

    QUERY:
    {query}
    """

    return llm.invoke(prompt).content