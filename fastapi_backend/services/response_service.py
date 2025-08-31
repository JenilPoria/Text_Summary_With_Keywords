# from models import ArticleResponse, ArticleRequest
from fastapi_backend.models.response_model import ArticleResponse
from fastapi_backend.models.request_model import ArticleRequest
from graph import Main_Graph


def get_llm_response(article: str) -> ArticleResponse:
    response = Main_Graph.invoke({"input":article})
    return ArticleResponse(**response)