import smtplib
from email.message import EmailMessage
from config import USERNAME, PASSWORD
from string import Template
from pathlib import Path

html = Template(Path('template.html').read_text())

email = EmailMessage()
email['from'] = 'Zach Wahrer <developer@wahreroftheworlds.com>'
email['to'] = 'me@zachw.io'
email['subject'] = "Notification from wahreroftheworlds.com"

email.set_content('Sent via Python.')
email.add_alternative(html.substitute(name='Zach'), subtype='html')


with smtplib.SMTP(host='mail.wahreroftheworlds.com', port=2525) as smtp:
    smtp.set_debuglevel(1)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(USERNAME, PASSWORD)
    smtp.send_message(email)
    print('Mail sent.')
