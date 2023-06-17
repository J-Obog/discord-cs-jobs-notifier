from typing import List
from requests import Session

from notifier.posting.job_board import AbstractJobBoard
from notifier.types.job_post import JobPost
from notifier.types.post_source import PostSource

LINKEDIN_JOBS_URL = "https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards"

def get_id_from_urn(urn: str) -> str:
    return urn.split(":")[-1]

class LinkedinJobBoard(AbstractJobBoard):
    def __init__(self, jsession_id: str, li_at: str) -> None:
        super().__init__()
        self.session = Session()
        self.session.cookies['li_at'] = li_at
        self.session.cookies["JSESSIONID"] = jsession_id
        self.session.headers["csrf-token"] = jsession_id.strip('"')

    def get_postings(self) -> List[JobPost]:
        posts = [] 

        decoId = "com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-168"
        count = 25
        start = 0
        query = "(origin:JOB_SEARCH_PAGE_OTHER_ENTRY,keywords:software%20engineer%20internship,locationUnion:(geoId:103644278),selectedFilters:(distance:List(25)),spellCorrectionEnabled:true)"
        q = "jobSearch"

        url = f"{LINKEDIN_JOBS_URL}?decorationId={decoId}&count={count}&q={q}&query={query}&start={start}"

        data = self.session.get(url).json()

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

            posts.append(post)

        return posts