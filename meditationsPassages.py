# Program to distribute a Meditations passage on a daily basis

import random
import os
import ezgmail
from datetime import date
import logging
logging.basicConfig(filename='meditationsPassagesLog.txt', level=logging.DEBUG, format='%asctime)s - %(levelname)%s - '
                                                                                       '%(message)s')

os.chdir('C:\\Users\\Vincent\\Desktop')

text = 'meditations.txt' # Declaring meditations as our text here

with open(text,'r', encoding="utf-8") as myFile: # This will open the text as myFile, declares data as reading the text
    data = myFile.read()

# DONE: Split the text into a list of paragraphs and then use the choice function on that list

passage = random.choice(list(data.split(' \n')))

# DONE: Add the distribution via email or text to the code

emails = 'stoic emails.txt' # Commented in and out for testing purposes
# emails = 'just my email.txt' # This will be commented in and out for testing purposes.

# DONE: Add date and time to the subject of the email.

today = date.today()

# Done: Add a signature to the email.

signature = f"\n\n\n-----\n\nThis is a daily passage from Marcus Aurielus's The Meditations. \nSit on this thought " \
            f"just like he did. "

with open(emails,'r', encoding="utf-8") as stoicEmails:
    for email in stoicEmails:
        ezgmail.send(email, "Today's Passage, " + today.strftime("%m-%d-%y"), passage + signature)

# TODO: Scheduling the passages to be sent out at a certain time of day

# Done with windows task schedule///////this doesnt seem to work so im gonna work on this myself

print('Passage sent. Memento mori.')

# TODO: Add images and beautify the email.

