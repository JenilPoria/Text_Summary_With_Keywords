from pydantic import BaseModel, Field
from typing import List, Literal


class SummaryState(BaseModel):
    input : str = Field(..., description="The original input text to be summarized provided by the user.")
    summary : List[str] = Field(..., description="The concise list summary of the input text.",default_factory=list)
    keyword : List[List[str]] = Field(..., description="The list of 5 relevant keywords extracted from the summary.",default_factory=list)
    confidence_score : List[float] = Field(..., description="The confidence score out of 100 for each keyword extracted.",default_factory=list)

