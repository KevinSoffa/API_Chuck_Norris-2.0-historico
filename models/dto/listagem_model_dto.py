from dataclasses import dataclass
from fastapi import Query


@dataclass
class ListagemModelDTO:
    paginacao_limite: int = Query(10, gt=1)
    paginacao_pagina: int = Query(0)
