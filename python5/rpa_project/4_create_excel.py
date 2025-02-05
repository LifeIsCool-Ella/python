import smtplib
from imap_tools import MailBox
from account import *
from email.message import EmailMessage
from openpyxl import Workbook

max_val = 3
applicant_list = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1
    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2024)'):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip.split("/")
            print("닉네임 : {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

for applicant in applicant_list:
    print(applicant)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    for applicant in applicant_list:
        to_addr = applicant[0].from_
        #index = applicant[1]
        #nickname = applicant[2]
        #phone = applicant[3]
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= 3 :
            title = "파이썬 특강 안내[선정]"
            content = "{}님 축하드립니다. {} 번".format(nickname, index)
        else:
            title = "파이썬 특강 안내[탈락]"
            content = "{}님 탈락입니다. 대기순번 {} 번".format(nickname, index-max_val)

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname, "님에게 메시지 발송 완료")


wb = Workbook()
ws = wb.active
ws.append(["순번", "닉네임", "전화번호"])

for applicant in applicant_list[:max_val]:
    ws.append(applicant[1:])

ws.save("result.xlsx")

print("모든 작업이 완료되었습니다.")
