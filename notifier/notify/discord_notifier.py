from abc import ABC, abstractmethod
import requests

from notifier.notify.notification_pusher import AbstractNotificationPusher
from notifier.types.job_post import JobPost

BOT_NAME = "cs-job-notifier"
BOT_AVATAR = "https://wallpaperaccess.com/full/1428481.jpg"

class DiscordNotifier(AbstractNotificationPusher):
    def __init__(self, webhook_url: str) -> None:
        super().__init__()
        self.webhook_url = webhook_url

    def send_notification(self, post: JobPost):
        body = {
            "username": BOT_NAME,
            "avatar_url": BOT_AVATAR,
            "embeds": [
              {
                    "title": f"**New Job Opening @ {post.companyName}**", 
                    "color": 5763719,
                    "description": f"Position: {post.title}\nApply Link: {post.link}",
                    "thumbnail": {
                        "url": post.companyLogoUrl,
                        "height": 0,
                        "width": 0 
                    }
                }
            ]
        }

        requests.post(self.webhook_url, json=body)