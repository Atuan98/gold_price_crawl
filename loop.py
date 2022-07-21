import os
import time
import schedule

parent_dir = os.getcwd()
def loop():
    os.system("python main.py")

schedule.every(5).seconds.do(loop)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)