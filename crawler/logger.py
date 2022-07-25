from loguru import logger
from datetime import datetime, timedelta, time


class TimedSizedRotator:
    def __init__(self, *, size, at):
        now = datetime.now()

        self._size_limit = size
        self._time_limit = now.replace(hour=at.hour, minute=at.minute, second=at.second)

        if now >= self._time_limit:
            # The current time is already past the target time so it would rotate already.
            # Add one day to prevent an immediate rotation.
            self._time_limit += timedelta(days=1)

    def should_rotate(self, message, file):
        file.seek(0, 2)
        if file.tell() + len(message) > self._size_limit:
            return True
        if message.record["time"].timestamp() > self._time_limit.timestamp():
            self._time_limit += timedelta(days=1)
            return True
        return False


def init():
    # Rotate file if over 10 MB or at midnight every day
    rotator = TimedSizedRotator(size=10e+6, at=time(0, 0, 0))
    logger.add("logs/logger-{time:YYYY-MM-DD}.log", rotation=rotator.should_rotate, retention=10, buffering=5,
               format="{time} [{thread}] {level} {name} {message}")
