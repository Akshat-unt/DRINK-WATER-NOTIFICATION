#---------------->IMPORTS<-----------------
import time
from plyer import notification
#--------------->NOTIFY<-------------
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water!!",
            message = "drinking water keeps us healthy and hydrated",
            app_icon = "G:\\Program files\\Python\\drink water notification\\water.ico",
            timeout=4
        )
        time.sleep(60*60) # time delay between two notifications.
