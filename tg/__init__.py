from fastapi import Depends

from .methods import getMe
from .methods import getWebhookInfo
from .methods import sendMessage
from .methods import setWebhook
from .methods import telegram_client
from .types import GetMeResponse
from .types import GetWebhookInfoResponse
from .types import Message
from .types import Response
from .types import SendMessageRequest
from .types import SendMessageResponse
from .types import SetWebhookResponse
from .types import Type
from .types import Update
from .types import User
from .types import WebhookInfo

Telegram = Depends(telegram_client)