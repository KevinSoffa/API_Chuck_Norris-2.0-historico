from fastapi import APIRouter
from decouple import config # Variaveis no arquivo .env


router = APIRouter(
    prefix=config('PREFIXO'),
    tags=[],
)