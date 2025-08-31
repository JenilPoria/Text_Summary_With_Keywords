from state import SummaryState
from prompts import summary_prompt
from llm import groq_llm as llm


def summarize_generator(state : SummaryState) -> SummaryState:
    article = state.input
    response = llm.invoke(summary_prompt.format_messages(text=article)).content
    state.summary.append(response)

    return state
