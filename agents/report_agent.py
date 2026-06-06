from llm import get_llm
from utils.prompts import REPORT_PROMPT

def generate_report(rca, fix, logs):
    llm = get_llm()

    prompt = f"""
    {REPORT_PROMPT}

    RCA:
    {rca}

    FIX:
    {fix}

    LOGS:
    {logs}
    """

    return llm.invoke(prompt).content