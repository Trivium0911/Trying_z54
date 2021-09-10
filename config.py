import os
from pydantic import BaseSettings
from pydantic import Field
admin_token = os.getenv("ADMIN_TOKEN")
print(f"{admin_token = !r}")

webhook_secret = os.getenv("WEBHOOK_SECRET")
assert webhook_secret, "env var WEBHOOK_SECRET is not set"
webhook_path = f"/tg/wh{webhook_secret}"
print(f"{webhook_path = !r}")

bot_token = os.getenv("TG_BOT_TOKEN")
assert bot_token, "env var TG_BOT_TOKEN is not set"
bot_url = f"https://api.telegram.org/bot{bot_token}"
print(f"{bot_url = !r}")


class Settings(BaseSettings):
    admin_token: str = Field(..., env="ADMIN_TOKEN")
    bot_token: str = Field(..., env="TG_BOT_TOKEN")
    webhook_secret: str = Field(..., env="WEBHOOK_SECRET")


    @property
    def bot_url(self):
        return f"https://api.telegram.org/bot{self.bot_token}"
    @property
    def webhook_path(self):
        return f"/tg/wh{self.webhook_secret}"


settings = Settings()

