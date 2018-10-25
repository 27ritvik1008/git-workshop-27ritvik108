# SENDING A MAIL THROUGH PYTHON......😊

# A MAIL CAN BE SENT THROUGH PYTHON USING THE SMTP MODULE OF PYTHON
# SMTP STANDS FOR Simple Mail Transfer Protocol .....

import smtplib
from email.mime.text import MIMEText as text #MIMEText helps in assigning subject and attachements to mail
gmail_id = input("PLEASE ENTER UR GMAIL ID \n")
gmail_password=input("ENTER UR PASSWORD \n")
receiver_id = input("ENTER THE RECIPIENT'S EMAIL ID \n")
subject = input("ENTER THE SUBJECT OF THE MAIL \n")
message = input("PLEASE ENTER THE MESSAGE U WISH TO SEND \n")
m=text(message)                  # MIMEText decrypts message into string
m['subject'] = subject           # WE ADD SUBJECT USING THE MIMEText MODULE...
m['from'] = gmail_id                         
m['to'] = receiver_id
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()      # Starts an encrypted server . TLS - TRANSPORT LAYER SECURITY 
s.login(gmail_id,gmail_password)
s.sendmail(gmail_id,receiver_id,m.as_string())   #FINALLY,CONVERTING "m" AS A STRING
s.quit()
print("EMAIL SUCCESSFULLY SENT......🤗")
