from abc import ABC, abstractmethod
import requests

from notifier.notify.notification_pusher import AbstractNotificationPusher
from notifier.types.job_post import JobPost

class DiscordNotifier(AbstractNotificationPusher):
    def __init__(self, webhook_url: str, bot_name: str, bot_avatar: str) -> None:
        super().__init__()
        self.webhook_url = webhook_url
        self.bot_name = bot_name
        self.bot_avatar = bot_avatar

    def send_notification(self, post: JobPost):
        body = {
            "username": self.bot_name,
            "avatar_url": self.bot_avatar,
            "embeds": [
                {
                    "title": f"New Job Opening!", 
                    "color": 5763719,
                    "description": f"{post.companyName} has opened a new position for {post.title}"
                }
            ]
        }

        requests.post(self.webhook_url, json=body)