from __future__ import absolute_import

import smtplib
from email.mime.text import MIMEText

from celery import shared_task

SMTPserver = 'smtp.att.yahoo.com'
sender = 'kononenkoa995@ukr.net'
destination = ['kononenkoa995@gmail.com']

USERNAME = "kononenkoa995@ukr.net"
PASSWORD = "apocalypse"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

content="""\
Test message
"""

subject="Sent from Python"


@shared_task(bind=True)
def send_mail(self):
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender  # some SMTP servers will do this automatically, not all

    conn = smtplib.SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

@shared_task(bind=True)
def test(self):
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    message = u"The purchase was applied"
    # fp = open(message, 'rb')
    # Create a text/plain message
    # msg = MIMEText(fp.read())
    # fp.close()
    msg = MIMEText(message)

    me = 'kononenkoa995@gmail.com'
    you = 'kononenkoa995@ukr.net'
    msg['Subject'] = 'Celery'
    msg['From'] = me
    msg['To'] = you

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost', 'Apocalypse1')
    s.sendmail(me, [you], msg.as_string())
    s.quit()

    print "OKs"

    return "The test task executed with argument"
