import sys
import time
from win10toast import ToastNotifier

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

class PomodoroTimer():

    def __init__(self, workTime, brakeTime, intervals):
        self.workTime = workTime
        self.brakeTime = brakeTime
        self.intervals = intervals
    

    def countdownWorktime(self):
        workTime = self.workTime * 60
        brakeTime = self.brakeTime * 60
        intervals = self.intervals
        toaster = ToastNotifier()
        for index in range(intervals):
            print("Worktime, yo")
            toaster.show_toast("Worktime","Shut the hell up and WORK!")
            countdown(workTime)
            print("Brake time baby")
            toaster.show_toast("Brake","Brake time baby")
            countdown(brakeTime)
            print("Interval: "+str(index+1))
if  len(sys.argv) < 3:
    pomodoro = PomodoroTimer(25, 5, 4)
    pomodoro.countdownWorktime()
else:
    pomodoro = PomodoroTimer(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    pomodoro.countdownWorktime()
