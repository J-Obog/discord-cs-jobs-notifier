import dotenv
import os

from notifier.types.config import get_config

from notifier.notify.discord_notifier import DiscordNotifier
from notifier.store.redis_store import RedisStore
from notifier.posting.linkedin import LinkedinJobBoard
from notifier.worker.notification_worker import NotificationWorker
from notifier.worker.runner import WorkerRunner
from notifier.types.job_post import JobPost
from notifier.types.post_source import PostSource

def main():
    dotenv.load_dotenv()
    cfg = get_config(dict(os.environ))

    discord_notifier = DiscordNotifier(cfg.discord_webhook_url)
    redis_store = RedisStore(cfg.redis_host, cfg.redis_port)
    linkedin_board = LinkedinJobBoard(cfg.linkedin_jsession_id, cfg.linkedin_li_at)

    worker = NotificationWorker(redis_store, linkedin_board, discord_notifier)

    runner = WorkerRunner("cs-jobs-linkedin-worker", worker, 30)
    runner.run()


if __name__ == "__main__":
    main()