import time
from win10toast import ToastNotifier
import webbrowser
import datetime

currentDT = datetime.datetime.now()
times = 0

print("Started program")

def stretch():
    def open_browser_tab():
        webbrowser.open("https://www.healthline.com/health/deskercise", new=1)

    toast = ToastNotifier()
    toast.show_toast(title="Stretch time!", msg="Click on me so you can get your exercises.",
                     icon_path="people2.ico", duration=10, threaded=False, callback_on_click=open_browser_tab)
    print("You stretch now! - " + currentDT.strftime("%H:%M"))

def getup():
    toast = ToastNotifier()
    toast.show_toast(title="Get up!", msg="Go and get an apple.",
                     icon_path="people2.ico", duration=10, threaded=False)
    print("You get up now! - " + currentDT.strftime("%H:%M"))


while True:
    time.sleep(1800)
    stretch()
    time.sleep(1800)
    getup()
