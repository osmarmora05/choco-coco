from pydantic import BaseModel


class PokemonProperty(BaseModel):
    name: str
    ascii: str
