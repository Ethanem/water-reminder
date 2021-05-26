import os
import schedule
import time
from datetime import datetime as dt
import random

def send_message(phone_number, message):
    os.system('osascript imessage.scpt {} "{}"'.format(phone_number, message))

def water_remind():
    water_reminders = [
        "", #add list of different reminders - just to spice things up!
        "",
        ""
    ]

    names = [
        "", #add list of different names to make messages unique
        "",
        ""
    ]

    if __name__ == '__main__':
        phone_number = '' #enter phone number here
        reminder = random.choice(water_reminders) + random.choice(names)
        send_message(phone_number, reminder)

schedule.every(30).minutes.do(water_remind)

while True:
    if dt.now().hour in range(11, 22): #the time period in the day when messages will send
        schedule.run_pending()
        time.sleep(1)
