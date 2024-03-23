from abc import ABC, abstractmethod
from typing import List

from notifier.types.job_post import JobPost

class JobBoard(ABC):
    @abstractmethod
    def get_postings(self, titles: List[str]) -> List[JobPost]:
        ...