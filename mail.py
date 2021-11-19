import os
import smtplib
import pandas as pd
from email.message import EmailMessage


EMAIL_ADDRESS = "anonymousoxfordian@gmail.com"
EMAIL_PASSWORD = "poorna1999"

contacts = pd.read_csv("static/files/mail.csv")
mails = contacts['Emails'].values


msg = EmailMessage()
msg['Subject'] = 'New Mail!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ",".join(mails)

msg.set_content('This is a plain text email')

# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)