import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECEIVE_EMAIL_ADDRESS

to_list = [RECEIVE_EMAIL_ADDRESS, RECEIVE_EMAIL_ADDRESS]
msg = ", ".join(to_list)
print(msg)

msg["Cc"] = RECEIVE_EMAIL_ADDRESS
msg["Bcc"] = RECEIVE_EMAIL_ADDRESS

msg.set_content("본문입니다.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "test mail"
    body = "mail body"

    msg = f"Subject: {subject}\n{body}"
    smtp.send_message(msg)