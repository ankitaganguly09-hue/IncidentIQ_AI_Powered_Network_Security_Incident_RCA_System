from llm import get_llm
from utils.prompts import FIX_PROMPT

def suggest_fix(rca, code_context):
    llm = get_llm()

    prompt = f"""
    {FIX_PROMPT}

    RCA:
    {rca}

    CODE:
    {code_context}
    """

    return llm.invoke(prompt).content