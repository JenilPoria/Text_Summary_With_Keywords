from state import SummaryState
from typing import List, Literal

def choose(state : SummaryState) -> Literal["yes","no"]:
    score = float(state.confidence_score[-1])
    if score >= 75:
        return  "yes"
    else:

        return  "no"