
#Go over to gmail and set up 2-factor authentication
#Generate app password
#Create a function to send the email

from email.message import EmailMessage
email_sender = 'edmundgyimah05@gmail.com'
email_password = 'trpcbrmxakbzttgm'
import ssl
import smtplib

email_receiver = 'fepako1580@crtsec.com'

subject = "Do not forget to apply"
body = """
After you go through, apply with confidence. 
"""

#Creating an instance of the EmailMessage library package imported
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


#Create a context (need to import the SSL and SMTP Library first)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

