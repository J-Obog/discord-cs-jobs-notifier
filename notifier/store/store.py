from abc import ABC, abstractmethod
from typing import Optional

class AbstractStore(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        ...

    @abstractmethod
    def set(self, key: str, val: str):
        ...