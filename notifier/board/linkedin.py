from typing import List
from requests import Session

from notifier.board.board import JobBoard
from notifier.types.posting import JobPost, PostSource

LINKEDIN_JOBS_URL = "https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards"

def get_id_from_urn(urn: str) -> str:
    return urn.split(":")[-1]

class LinkedinJobBoard(JobBoard):
    def __init__(self, jsession_id: str, li_at: str) -> None:
        super().__init__()
        self.session = Session()
        self.session.cookies['li_at'] = li_at
        self.session.cookies["JSESSIONID"] = jsession_id
        self.session.headers["Csrf-Token"] = jsession_id.strip('"')
        self.session.headers["Accept"] = "*/*"
        
    def get_postings(self, titles: List[str]) -> List[JobPost]:
        posts = [] 

        if len(titles) > 0:
            decoId = "com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-168"
            count = 20
            start = 0
            query = f"(origin:JOB_SEARCH_PAGE_OTHER_ENTRY,keywords:Software%20Engineer%20Intern,locationUnion:(geoId:103644278),selectedFilters:(distance:List(25)),spellCorrectionEnabled:true)"
            q = "jobSearch"

            url = f"{LINKEDIN_JOBS_URL}?decorationId={decoId}&count={count}&q={q}&query={query}&start={start}"

            resp = self.session.get(url)
            
            data = resp.json()

            postObjs = data["elements"]

            for postObj in postObjs:
                postObjData = postObj["jobCardUnion"]["jobPostingCard"]
                postingId = get_id_from_urn(postObjData["jobPostingUrn"])   

                baseLogoObj = postObjData["logo"]["attributes"][0]["detailData"]["companyLogo"]["logo"]["vectorImage"]
                rootLogoUrl = baseLogoObj["rootUrl"]
                logoPathSegment = baseLogoObj["artifacts"][0]["fileIdentifyingUrlPathSegment"]

                post = JobPost(
                    postingId = postingId,
                    companyId = postObjData["logo"]["attributes"][0]["detailDataUnion"]["companyLogo"],
                    companyName = postObjData["primaryDescription"]["text"],
                    title = postObjData["jobPostingTitle"],
                    description = None,
                    source = PostSource.LINKEDIN,
                    link = f'https://www.linkedin.com/jobs/view/{postingId}',
                    companyLogoUrl =  rootLogoUrl + logoPathSegment
                )
                
                print(post.companyId) 

                posts.append(post)

        return posts