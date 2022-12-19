import datetime
import pytz

from db_worker import DBWorker


class StatusChecker:
    def __init__(self):
        self.worker = DBWorker
        self.last_time = self.last_time()
        self.local_time = self.local_time()
        self.last_status = self.last_status()
        self.time_diff = self.time_diff()
        self.statuses = ["\u26AA\uFE0F Світло є", "\u26AB\uFE0F Світла немає"]

    def last_time(self):
        with self.worker() as worker:
            return worker.get_time()

    def local_time(self):
        if self.last_time:
            local = pytz.timezone('Europe/Kyiv').fromutc(self.last_time)
            return datetime.datetime.strftime(local, "%H:%M:%S %d-%m-%Y")

    def last_status(self):
        with self.worker() as worker:
            if worker.get_status():
                return worker.get_status()[1]

    def time_diff(self):
        if self.last_time:
            return (datetime.datetime.utcnow() -
                    self.last_time).total_seconds()

    def save_to_db(self, status, local_time):
        with self.worker() as w:
            w.insert_status(status, local_time)

    def status_checker(self):
        try:
            if self.time_diff < 60 and self.last_status != self.statuses[0]:
                self.save_to_db(self.statuses[0], self.local_time)
                return f'{self.statuses[0]}\n {self.local_time}'
            if self.time_diff > 60 and self.last_status != self.statuses[1]:
                self.save_to_db(self.statuses[1], self.local_time)
                return f'{self.statuses[1]}\n {self.local_time}'
        except TypeError:
            return None
