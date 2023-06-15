from abc import ABC, abstractmethod
from typing import List

from notifier.types.job_post import JobPost

class AbstractJobBoard(ABC):
    @abstractmethod
    def get_postings(self) -> List[JobPost]:
        ...