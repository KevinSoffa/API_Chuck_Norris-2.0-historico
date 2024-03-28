from repository import historico_repository_jokes
from fastapi import HTTPException


def historico_service_jokes(listagem_dto: dict):
    response = historico_repository_jokes(
        listagem_dto
    )

    if response:
        return response or []
    
    raise HTTPException(400)
