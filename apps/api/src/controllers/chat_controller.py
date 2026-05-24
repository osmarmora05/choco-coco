from typing import Optional, TypeVar

from devtools import debug

from lib.choco_coco_brain import get_coquito
from models.pokemon import PokemonProperty
from photo import photo_pokemon_to_ascci

T = TypeVar("T")  # o_O


async def query_chat(
    query: str,
) -> tuple[T, Optional[PokemonProperty]]:

    response = await get_coquito().run(query)

    if response.structured_response is not None:
        name_pokemon = response.structured_response["name_pokemon"]
        ascii_pokemon = photo_pokemon_to_ascci(name_pokemon)

        if ascii_pokemon is not None:
            return (
                response,
                PokemonProperty(
                    name=name_pokemon,
                    ascii=ascii_pokemon,
                ),
            )

    debug(response)

    return (response, None)
