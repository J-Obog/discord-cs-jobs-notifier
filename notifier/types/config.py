from dataclasses import dataclass


@dataclass
class Config:
    redis_host: str
    redis_port: int
    linkedin_jsession_id: str
    linkedin_li_at: str
    discord_webhook_url: str