import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'your_email'        #Enter sender's mail.
email_password = 'your_password' #Enter sender's mail email_password
email_send = 'recipient_email'   #Enter reveiver's email.

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='filename'

try:
  attachment  =open(filename,'rb')
  part = MIMEBase('application','octet-stream')
  part.set_payload((attachment).read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition',"attachment; filename= "+filename)

  msg.attach(part)
  text = msg.as_string()

except Exception as p:
  print(p)

smtpServer = ["smtp.mail.yahoo.com", "smtp.gmail.com", "smtp.live.com"]
smtpPort = [465, 587, 465]

try:
  server = smtplib.SMTP(smtpServer[1],smtpPort[1]) #Write the corresponding server from the above list.
  server.starttls()
  server.login(email_user,email_password)
  server.sendmail(email_user,email_send,text)

except Exception as e:
  print(e)

finally:
  server.quit()
