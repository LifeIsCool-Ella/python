#imap tools 검색 https://pypi.org/project/imap-tools/
from imap_tools import MailBox
from account import *

import time
print(time.strftime('%d-%a-%Y'))

import datetime
dt = datetime.datetime.strptime("2024-12-31", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%a-%Y'))


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    for msg in mailbox.fetch(limit=5, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(UNSEEN)'):
        print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(FROM sender@gmail.com)', limit=3, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(TEXT "test mail")', limit=3, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(SUBJECT "test mail")', limit=3, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch(limit=5, reverse=True):
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2024)', limit=5, reverse=True):
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(ON 07-Nov-2024)', limit=5, reverse=True):
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(ON 07-Nov-2024 SUBJECT "test mail" UNSEEN)', limit=5, reverse=True):
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(OR ON 07-Nov-2024 SUBJECT "test mail" UNSEEN)', limit=5, reverse=True):
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject))




