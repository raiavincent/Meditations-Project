# Program to distribute a Meditations passage on a daily basis

import random
import ezgmail
from datetime import date
import datetime
import time
import schedule

text = 'meditations.txt'  # Declaring meditations as our text here

with open(
        text, 'r', encoding="utf-8"
) as myFile:  # This will open the text as myFile, declares data as reading the text
    data = myFile.read()

# DONE: Add a signature to the email.

def stoicEmail(listOfEmails):
    signature = '''\n\n\n-----\n\nThis is a daily passage from Marcus Aurielus's The Meditations. 
\nSit on this thought just like he did.
\nFor questions, comments, or to be removed from the list, please contact vincentraia1@gmail.com.'''
    today = date.today()
    # split the text into a list of paragraphs and then use the choice function on that list
    passage = random.choice(list(data.split(' \n')))
    # attempt to clean passage on mobile by splitting new lines
    passage = passage.strip('\n')
    with open(listOfEmails, 'r', encoding="utf-8") as stoicEmails:
        for email in stoicEmails:
            ezgmail.send(email,
                         "Today's Passage, " + today.strftime("%m-%d-%y"),
                         passage + signature)
    print('Passage sent. Memento mori.' + today.strftime("%m-%d-%y"))


schedule.every().monday.at('08:15').do(stoicEmail, listOfEmails=emailList)
schedule.every().tuesday.at('08:15').do(stoicEmail, listOfEmails=emailList)
schedule.every().wednesday.at('08:15').do(stoicEmail, listOfEmails=emailList)
schedule.every().thursday.at('08:15').do(stoicEmail, listOfEmails=emailList)
schedule.every().friday.at('08:15').do(stoicEmail, listOfEmails=emailList)

while True:
    schedule.run_pending()
    time.sleep(1)