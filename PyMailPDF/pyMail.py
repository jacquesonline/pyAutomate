#!/usr/bin/env python3
# Server name: smtp.office365.com
# Port: 587
# Encryption method: STARTTLS
# mail_server.send_message(message)


import smtplib
import getpass
import mimetypes
import os.path
from email.message import EmailMessage

message = EmailMessage()
sender = "me@example.com"
recipient = "j.c.steenkamp10@gmail.com"
message['From'] = sender
message['To'] = recipient
print(message)
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
print(message)
body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)
print(message)

# attachment_path = "/tmp/example.png"
attachment_path = "C:\\Users\\jcste\\googleAutomation\\pyAutomate\\Pic1.png"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

# print(message)


mail_server = smtplib.SMTP('smtp.gmail.com:587')
mail_server.ehlo()
mail_server.starttls()
mail_pass = getpass.getpass('Password? ')
print(mail_pass)
mail_server.login('j.c.steenkamp10@gmail.com', mail_pass)
mail_server.send_message(message)
# mail_server.sendmail('j.c.steenkamp10@gmail.com',
#  'j.c.steenkamp10@gmail.com', message)
