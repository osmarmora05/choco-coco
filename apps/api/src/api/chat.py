from devtools import debug
from typing import Optional

from pydantic import BaseModel
from robyn import SubRouter

from controllers.chat_controller import query_chat
from models.pokemon import PokemonProperty

chat = SubRouter(__file__, prefix="/api/chat")


class ChatMessage(BaseModel):
    content: str


class ChatMessageResponse(BaseModel):
    content: str
    properties: Optional[PokemonProperty]


@chat.post("/message")
async def create_message(request: ChatMessage) -> ChatMessageResponse:
    [response, pokemon_property] = await query_chat(request.content)

    if pokemon_property is not None:
        debug(
            ChatMessageResponse(
                content=str(response.response), properties=pokemon_property
            )
        )
        return ChatMessageResponse(
            content=str(response.response), properties=pokemon_property
        )

    debug(ChatMessageResponse(content=str(response.response), properties=None))
    return ChatMessageResponse(content=str(response.response), properties=None)
