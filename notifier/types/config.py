from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    redis_host: str
    redis_port: int
    linkedin_jsession_id: str
    linkedin_li_at: str
    discord_webhook_url: str


def get_config(env_map: Dict[str, str]) -> Config:
    return Config(
        redis_host=env_map["REDIS_HOST"],
        redis_port=int(env_map["REDIS_PORT"]),
        linkedin_jsession_id = env_map["LINKEDIN_JSESSION_ID"],
        linkedin_li_at = env_map["LINKEDIN_LI_AT"],
        discord_webhook_url = env_map["DISCORD_WEBHOOK_URL"]
    )