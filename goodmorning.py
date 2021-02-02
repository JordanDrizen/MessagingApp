# storing the good morning and night messages
good_morning_messages = [
    "Good morning beautiful!",
    "I hope your morning is as great as you are!",
    "Today is your day, you are gonna do great",
    "Good morning gorgeous",
    "Don't forget to take your medicine!",
    "You are going to have an amazing day!",
]

good_night_messages = [
    "Don't forget to take your medicine!",
    "Sleep tight",
    "I love you",
    "Don't let the bed bugs bite",
    "Sweet dreams",
    "Make sure to check under the bed",
    "You deserve a good night's rest after this long day!",
]

from twilio.rest import Client
import random
from datetime import datetime
import sys

# creating function with authentication token to use twilio client
def send_message(message):
    account = "ACf1d9fc1fcd54a21c1a0eafb77630b5bc"
    token = "7dedc61554b80599bbcdacb1fd3825f3"
    client = Client(account, token)
    cellphone = 4697445642
    twilio_number = 18186503151

    client.messages.create(to=cellphone, from_=twilio_number, body=message)


now = datetime.now()
AM_or_PM = now.strftime("%p")

# determing the time of day to send the proper message
if AM_or_PM == "AM":
    send_message(random.choice(good_morning_messages))
else:
    send_message(random.choice(good_night_messages))

sys.exit()
