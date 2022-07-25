import os
import time
import schedule
from config import LOOP_TIMEOUT


def loop():
    os.system("python main.py")


schedule.every(LOOP_TIMEOUT).seconds.do(loop)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
