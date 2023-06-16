from notifier.worker.worker import AbstractWorker
from notifier.store.store import AbstractStore
from notifier.posting.job_board import AbstractJobBoard
from notifier.notify.notification_pusher import AbstractNotificationPusher


class NotificationWorker(AbstractWorker):
    def __init__(self, store: AbstractStore, job_board: AbstractJobBoard, pusher: AbstractNotificationPusher) -> None:
        self.store = store
        self.job_board = job_board
        self.pusher = pusher

    def work(self):
        print("Getting job postings")
        postings = self.job_board.get_postings()
        #print(postings)
        
        for post in postings:
            postRecord = self.store.get(post.postingId)

            if postRecord is None:
                print("Cache miss")
                self.pusher.send_notification(post)
                print("Sent noty")
                self.store.set(post.postingId, "1")
            else:
                print("Cache hit")

                