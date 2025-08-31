from pydantic import BaseModel, Field


class ArticleRequest(BaseModel):
    input : str = Field(..., description="The original input text to be summarized provided by the user.")
