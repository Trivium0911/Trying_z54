from pydantic import BaseSettings
from pydantic import Field


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