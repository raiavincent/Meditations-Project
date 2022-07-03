# Program to distribute a Meditations passage on a daily basis

import random
import ezgmail
from datetime import date
import datetime
import time
import schedule

text = 'meditations.txt' # Declaring meditations as our text here

with open(text,'r', encoding="utf-8") as myFile: # This will open the text as myFile, declares data as reading the text
    data = myFile.read()



# DONE: Add the distribution via email
emails = 'stoic emails.txt' # Commented in and out for testing purposes
# emails = 'just my email.txt' # This will be commented in and out for testing purposes.

# DONE: Add a signature to the email.

signature = f"\n\n\n-----\n\nThis is a daily passage from Marcus Aurielus's The Meditations. \nSit on this thought just like he did.\nFor questions, comments, or to be removed from the list, please contact vincentraia1@gmail.com."

def stoicEmail():
    # DONE: Add date and time to the subject of the email.
    today = date.today()
    # DONE: Split the text into a list of paragraphs and then use the choice function on that list
    passage = random.choice(list(data.split(' \n')))
    with open(emails,'r', encoding="utf-8") as stoicEmails:
        for email in stoicEmails:
            ezgmail.send(email, "Today's Passage, " + today.strftime("%m-%d-%y"), passage + signature)
    print('Passage sent. Memento mori.' + today.strftime("%m-%d-%y"))

schedule.every().monday.at('08:15').do(stoicEmail)
schedule.every().tuesday.at('08:15').do(stoicEmail)
schedule.every().wednesday.at('08:15').do(stoicEmail)
schedule.every().thursday.at('08:15').do(stoicEmail)
schedule.every().friday.at('08:15').do(stoicEmail)

while True:
    schedule.run_pending()
    time.sleep(1)
