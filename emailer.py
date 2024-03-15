import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import csv

#Server Config
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'accessengupenn@gmail.com'
password = 'accessisgreat'

subject = "Email Subject"

emails = []
names = []

with open('/Users/jfanale/Desktop/Sponsorship_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        emails.append(row[0])
        names.append(row[0] + " " + row[1])

emails = ["jfanale@seas.upenn.edu"]
names = ["Jake Fanale"]

recipients = emails

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)

    for i in range(len(recipients)):
        if i > 0:
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = "Access Engineering at The University of Pennsylvania"
            message['To'] = recipients[i]

            body = f"""\
                <html>
                <head></head>
                <body>
                <p>Hello, {names[i]}!</p>
                </body>
                </html>
                """

            message.attach(MIMEText(body, 'html'))

            server.sendmail(username, recipients[i], message.as_string())
            print(recipients[i])
