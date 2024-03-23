import dotenv
import os
from notifier.types.config import get_config
from notifier.discord import DiscordNotifier
from notifier.board.linkedin import LinkedinJobBoard

def main():
    dotenv.load_dotenv()
    cfg = get_config(dict(os.environ))

    job_titles = ["Software Engineer Intern"] 
    discord_notifier = DiscordNotifier(cfg.discord_webhook_url)
    linkedin_job_board = LinkedinJobBoard(cfg.linkedin_jsession_id, cfg.linkedin_li_at)

    companies_seen = set()

    posts = linkedin_job_board.get_postings(job_titles)
    
    for post in posts:
        company_id = post.companyId

        if company_id in companies_seen:
            print("Skipping because we already sent out a notification for this company")
        else:
            discord_notifier.send(post)
            companies_seen.add(company_id)        

if __name__ == "__main__":
    main()