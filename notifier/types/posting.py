from dataclasses import dataclass
from typing import Optional

@dataclass
class JobPosting:
    postingId: str
    companyId: str
    companyName: str
    title: str
    description: Optional[str]