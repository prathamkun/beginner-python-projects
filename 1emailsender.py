from email.message import EmailMessage
import ssl
import smtplib
email_sender = 'prathamkunbusiness@gmail.com'
email_password = '#WRITE YOUR PASS HERE'

email_receiver = '#create a temporary email from the temp website just to check if its working or not'

subject = "How are you?"
body = """
 Hi,

I hope youre doing well. Its been a while since we last talked, so I thought I did check in and see how you are doing. How is everything going on your side—work, studies, and life in general?

Things are going fine here. Lets catch up soon when you get some time. I did really love to hear from you.

Take care and talk soon.

Best regards,
Pratham kun
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
