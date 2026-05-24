from pydantic import BaseModel, Field


class PokemonAttribute(BaseModel):
    name_pokemon: str = Field("The name of Pokémon (creature)")
