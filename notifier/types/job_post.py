from dataclasses import dataclass
from typing import Optional

from notifier.types.post_source import PostSource

@dataclass
class JobPost:
    postingId: str
    companyId: str
    companyName: str
    title: str
    description: Optional[str]
    source: PostSource
    link: str