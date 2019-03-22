import os
import sys
import time

class PomodoroTimer():

    def __init__(self, workTime, brakeTime):
        self.workTime = workTime
        self.brakeTime = brakeTime

    @staticmethod
    def notify(title, text):
        os.system(
            """osascript -e 'display notification "{}" with title "{}"'""".format(text, title))

    @staticmethod
    def sayNotification(message):
        os.system('say "{}"'.format(message))

    def countdownWorktime(self):
        workTime = self.workTime * 60
        brakeTime = self.brakeTime * 60
        for index in range(4):
            print("It's worktime")
            self.notify("Worktime", "Shut the fuck up and work")
            self.sayNotification("Its time to work mother fucka")
            time.sleep(workTime)
            print("brake")
            self.notify("Brake", "Brake time baby")
            self.sayNotification("Brake time baby")
            time.sleep(brakeTime)

if len(sys.argv[1:]) != 2:
    pomodoro = PomodoroTimer(25, 5)
    pomodoro.countdownWorktime()

else:
    pomodoro = PomodoroTimer(float(sys.argv[1:][0]), float(sys.argv[1:][1]))
    pomodoro.countdownWorktime()
