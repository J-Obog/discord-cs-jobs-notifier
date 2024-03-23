import dotenv
import os
from notifier.types.config import get_config
from notifier.discord import DiscordNotifier
from notifier.board.linkedin import LinkedinJobBoard

def main():
    dotenv.load_dotenv()
    cfg = get_config(dict(os.environ))

    job_titles = ["Software Engineer Internship"] 
    discord_notifier = DiscordNotifier(cfg.discord_webhook_url)
    linkedin_job_board = LinkedinJobBoard(cfg.linkedin_jsession_id, cfg.linkedin_li_at)

    posts = linkedin_job_board.get_postings(job_titles)
    
    for post in posts:
        discord_notifier.send(post)

if __name__ == "__main__":
    main()