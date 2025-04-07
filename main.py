import random_scheduler
import schedule
import time
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, time_window_start, time_window_end):
        self.name = name
        self.time_window_start = time_window_start  # datetime object
        self.time_window_end = time_window_end      # datetime object
        self.scheduled_time = None

    def schedule_task(self):
        start_seconds = int(self.time_window_start.timestamp())
        end_seconds = int(self.time_window_end.timestamp())
        random_seconds = random_scheduler.generate_random_number(start_seconds, end_seconds)
        self.scheduled_time = datetime.fromtimestamp(random_seconds)

    def __str__(self):
        return f"Task: {self.name}, Scheduled at: {self.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == "__main__":
    tomorrow = datetime.now() + timedelta(days=1)
    start_time = tomorrow.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = tomorrow.replace(hour=17, minute=0, second=0, microsecond=0)

    task = Task("Team Meeting", start_time, end_time)
    task.schedule_task()
    print(task)

    print("Running scheduler... Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(60)
