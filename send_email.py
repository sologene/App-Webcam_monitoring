import smtplib, ssl
import os
import imghdr
from email.message import EmailMessage


def send_email(img_path):
    host = "smtp.gmail.com"
    port = 587
    password = os.getenv("PASSWORD")
    username = "website.contact34@gmail.com"
    receiver = "website.contact34@gmail.com"

    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up"
    email_message.set_content("Hey, we just saw a new customer")

    with open(img_path, "rb") as file:
        content = file.read()
        email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    context = ssl.create_default_context()
    gmail = smtplib.SMTP("smtp.gmail.com", port)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username,receiver, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("")



