from abc import ABC, abstractmethod
from typing import List

from notifier.types.posting import JobPost

class JobBoard(ABC):
    @abstractmethod
    def get_postings(self, titles: List[str]) -> List[JobPost]:
        ...