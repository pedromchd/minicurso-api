from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Categoria(Enum):
    doce = "doce"
    citrico = "citrico"
    tropical = "tropical"


class Item(BaseModel):
    nome: str
    tamanho: float
    cor: str
    categoria: Categoria


items = {
    1: Item(nome="banana", tamanho=0.2, cor="amarelo", categoria=Categoria.tropical),
    2: Item(nome="laranja", tamanho=0.3, cor="laranja", categoria=Categoria.citrico),
    3: Item(nome="uva", tamanho=0.1, cor="roxo", categoria=Categoria.doce),
}


@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}
