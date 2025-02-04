import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "test mail"
    body = "mail body"

    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, RECEIVE_EMAIL_ADDRESS, msg)

