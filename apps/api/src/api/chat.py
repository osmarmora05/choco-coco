import re
from typing import Optional

from devtools import debug
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

    content_str = re.sub(r"^assistant:\s*", "", str(response.response))

    if pokemon_property is not None:
        debug(
            ChatMessageResponse(content=str(content_str), properties=pokemon_property)
        )
        return ChatMessageResponse(
            content=str(content_str), properties=pokemon_property
        )

    debug(ChatMessageResponse(content=str(content_str), properties=None))
    return ChatMessageResponse(content=str(content_str), properties=None)
