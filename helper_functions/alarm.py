import os
import platform
import random
import subprocess
from datetime import datetime
from threading import Thread

directory = 'alarm'  # dir need not be '../alarm' as the Thread is triggered by jarvis.py which is in root dir


class Alarm(Thread):
    def __init__(self, hours, minutes, am_pm):
        super(Alarm, self).__init__()
        if hours and minutes and am_pm:
            self.hours = hours
            self.minutes = minutes
            self.am_pm = am_pm
        else:
            os._exit(0)

    def run(self):
        operating_system = platform.system()
        music_dir = "mp3"
        tone = random.choice(os.listdir(music_dir))
        files = os.listdir(directory)
        file_name = f"{self.hours}_{self.minutes}_{self.am_pm}.lock"
        while True:
            now = datetime.now()
            am_pm = now.strftime("%p")
            minute = now.strftime("%M")
            hour = now.strftime("%I")
            if hour == self.hours and minute == self.minutes and am_pm == self.am_pm and file_name in files:
                if operating_system == 'Darwin':
                    subprocess.call(["open", f"{music_dir}/{tone}"])
                elif operating_system == 'Windows':
                    location = os.path.abspath(os.getcwd())
                    os.system(f'start wmplayer "{location}\\{music_dir}\\{tone}"')
                os.remove(f"{directory}/{file_name}")
                return
