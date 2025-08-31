from fastapi import APIRouter
# from models import ArticleResponse, ArticleRequest
# from services import get_llm_response
from fastapi_backend.models.request_model import ArticleRequest
from fastapi_backend.models.response_model import ArticleResponse
from fastapi_backend.services.response_service import get_llm_response
router = APIRouter()

@router.get("/health")
def home():
    return {"message": "FastAPI backend running! our API is healthy"}


@router.post("/process", response_model=ArticleResponse)
async def process_article(article: ArticleRequest):
    return get_llm_response(article.input)
