from abc import ABC, abstractmethod

class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        ...