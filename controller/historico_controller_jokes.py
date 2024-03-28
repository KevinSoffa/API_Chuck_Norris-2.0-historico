from models.dto.listagem_model_dto import ListagemModelDTO
from service import historico_service_jokes
from fastapi import status, Depends
from .router import router


@router.get('', status_code=status.HTTP_200_OK)
def historico_controller_jokes(
    listagem_dto: ListagemModelDTO = Depends()
):
    return historico_service_jokes(
        listagem_dto.__dict__
    )
