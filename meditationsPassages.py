# Program to distribute a Meditations passage on a daily basis

import random
import ezgmail
from datetime import date

text = 'meditations.txt'  # Declaring meditations as our text here

with open(
        text, 'r', encoding="utf-8"
) as myFile:  # This will open the text as myFile, declares text as meditations
    meditations = myFile.read()

emailList = 'emails.txt'

signature = '''\n\n\n-----\n\nThis is a daily passage from Marcus Aurielus's The Meditations. 
\nSit on this thought just like he did.
\nFor questions, comments, or to be removed from the list, please contact vincentraia1@gmail.com.'''

today = date.today()

# split the text into a list of paragraphs and then use the choice function on that list
passage = random.choice(list(meditations.split(' \n')))

# attempt to clean passage on mobile by splitting new lines
passage = passage.strip('\n')

with open(emailList, 'r', encoding="utf-8") as stoicEmails:
    for email in stoicEmails:
        ezgmail.send(email,
                        "Today's Passage, " + today.strftime("%m-%d-%y"),
                        passage + signature)

print('Passage sent. Memento mori.' + today.strftime("%m-%d-%y"))