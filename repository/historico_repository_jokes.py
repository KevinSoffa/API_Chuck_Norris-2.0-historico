from models.dao.project import PROJECT
from models.dao.mongo import db
from math import ceil


def historico_repository_jokes(listagem_dto: dict):
    # Criando páginação e limite por página
    total = db.api.count_documents(
        {}
    )
    limite = 0

    if listagem_dto['paginacao_limite'] !=0:
        paginas = ceil(total/listagem_dto['paginacao_limite'])

    else:
        paginas = 1
        limite = total

    # GET no DB
    response = db.api.find(
        {},
        PROJECT
    ).limit(
        listagem_dto['paginacao_limite']
    ).skip(
        (listagem_dto['paginacao_pagina']) * listagem_dto['paginacao_limite']
    )

    return {
        'total': total,
        'paginas': paginas,
        'pagina': listagem_dto['paginacao_pagina'],
        'limite': limite,
        'jokes': list(response)
    }
