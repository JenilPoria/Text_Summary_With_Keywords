from state import SummaryState
from prompts import evaluate_prompt
from llm import groq_llm as llm



def reevaluate_keywords(state : SummaryState) -> SummaryState:
    summary = state.summary[-1]
    keywords = state.keyword[-1]
    article = state.input
    response = llm.invoke(evaluate_prompt.format_messages(input = article,summary=summary, keywords=', '.join(keywords))).content
    score = float(response)
    state.confidence_score.append(score)
    return state