from dataclasses import dataclass
from typing import Optional
from enum import Enum

class PostSource(Enum):
    LINKEDIN = 0

@dataclass
class JobPost:
    postingId: str
    companyId: str
    companyName: str
    title: str
    description: Optional[str]
    source: PostSource
    link: str
    companyLogoUrl: str