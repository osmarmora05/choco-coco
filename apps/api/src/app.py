from robyn import Robyn, ALLOW_CORS
from config import app_config


from api.chat import chat

app = Robyn(__file__)

app.include_router(chat)
ALLOW_CORS(app, origins=["http://localhost:5173"])
