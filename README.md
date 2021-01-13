## Meditations Passages Project
The Meditation Passages Project is a program which disseminates a passage from Marcus Aurelius's renowned _The Meditatons_, which is a collection of writings from his daily journal. It is foundational to the Stoic philosphy, and has inspired myself, my friends, and countless others. This project allows you to read one of his thoughts a day and meditate on it.

### Modules Used
The main module that is used to run is [EZGmail](https://pypi.org/project/EZGmail/), developed by Al Sweigart, to send the passage from a gmail account set up for this specific purpose.

Next and also important is the [schedule](https://pypi.org/project/schedule/), which easily allows the code to run on set days and time, so the passage is there in the morning.

Run on a Raspberry Pi 4.

### How To Use
I have already provided the necessary modules in the needed in the requirements.txt file, so you would just have to run _pip install -r requirements.txt_ in the working directory. You will also have to setup EZGmail, but it is pretty straightforward and all instructions are listed on the modules PyPi page above.

Then, simply place the email addresses you want to send the passage to in a file named stoic emails.txt, and you are good to go! You can change the time and days you want the passage to be sent if you would like.

Easiest would to just be to contact myself, and I can add you to my own list to receive a passage at 8:15 AM weekdays.

### Stoicism
If you are new to stoicism and would like to know more, I would reccomend reading _The Meditations_ or visiting [The Daily Stoic](https://dailystoic.com/) and reading books from Ryan Holiday.
