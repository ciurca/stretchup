import time
from win10toast import ToastNotifier
import webbrowser

times = 0


def stretch():
    def open_browser_tab():
        webbrowser.open("https://www.healthline.com/health/deskercise", new=1)

    toast = ToastNotifier()
    toast.show_toast(title="Stretch time!", msg="Click on me so you can get your exercises.",
                     icon_path="people2.ico", duration=10, threaded=False, callback_on_click=open_browser_tab)
    print("You stretch now!")

def getup():
    toast = ToastNotifier()
    toast.show_toast(title="Get up!", msg="Go and get an apple.",
                     icon_path="people2.ico", duration=10, threaded=False)
    print("You get up now!")

# Bring up the dialog box here
# Only run if the user types in "start"
while True:
    time.sleep(1800)
    stretch()
    time.sleep(1800)
    getup()
