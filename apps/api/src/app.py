from robyn import Robyn

from api.chat import chat

app = Robyn(__file__)

app.include_router(chat)
