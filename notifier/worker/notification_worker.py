from typing import List

from notifier.worker.worker import AbstractWorker
from notifier.store.store import AbstractStore
from notifier.posting.job_board import AbstractJobBoard
from notifier.notify.notification_pusher import AbstractNotificationPusher


class NotificationWorker(AbstractWorker):
    def __init__(self, job_titles: List[str], store: AbstractStore, job_board: AbstractJobBoard, pusher: AbstractNotificationPusher) -> None:
        self.store = store
        self.job_board = job_board
        self.pusher = pusher
        self.job_titles = job_titles

    def work(self):
        postings = self.job_board.get_postings(self.job_titles)
        
        for post in postings:
            postRecord = self.store.get(post.postingId)

            if postRecord is None:
                self.pusher.send_notification(post)
                self.store.set(post.postingId, "1")
                