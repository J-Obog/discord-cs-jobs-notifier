from notifier.worker.worker import AbstractWorker
from threading import Thread
import time


class WorkerRunner:
    def __init__(self, name: str, worker: AbstractWorker, cadence: int) -> None:
        self.worker = worker
        self.cadence = cadence
        self.name = name
        self.t = Thread(target=self._run_worker, daemon=True)

    def _run_worker(self):
        while True:
            try:
                self.worker.work()
            except Exception as e:
                print(e)
                return
            time.sleep(self.cadence)

    def run(self):
        self.t.start()

