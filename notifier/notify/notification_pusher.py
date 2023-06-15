from abc import ABC, abstractmethod

from notifier.types.job_post import JobPost

class AbstractNotificationPusher(ABC):
    @abstractmethod
    def send_notification(self, post: JobPost):
        ...