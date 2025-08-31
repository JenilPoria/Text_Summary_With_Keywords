from state import SummaryState
from prompts import keywords_prompt
from llm import groq_llm as llm

def keywords_generator(state : SummaryState) -> SummaryState:
    summary = state.summary[-1]
    response = llm.invoke(keywords_prompt.format_messages(text=summary)).content
    keywords = [kw.strip() for kw in response.split(',')][:5]
    state.keyword.append(keywords)  
    return state
