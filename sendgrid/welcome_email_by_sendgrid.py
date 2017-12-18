# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    from_email = Email("test@example.com")
    to_email = Email(email)
    subject = 'Welcome'
    content = Content("text/plain", 'Hi {0}'.format(name))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')