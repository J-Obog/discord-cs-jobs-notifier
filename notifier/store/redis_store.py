from abc import ABC, abstractmethod
from typing import Optional
from redis import Redis

from notifier.store.store import AbstractStore

class RedisStore(AbstractStore):
    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.client = Redis(host=host, port=port, db=0)

    def get(self, key: str) -> Optional[str]:
        val = self.client.get(key)
        return None if val is None else str(val)

    def set(self, key: str, val: str):
        self.client.set(key, val)