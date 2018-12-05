import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
#Log into your gmail account
email_address = "YOUR_EMAIL@gmail.com"
password = "password"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, password)

#Person to receieve the email
recipient = "RECIPIENT_EMAIL@gmail.com"

msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = recipient

#add a subject to the email
msg['Subject'] = "SUBJECT OF THE MAIL"

#Add the message you'd like to send
message = "YOUR MESSAGE HERE"
msg.attach(MIMEText(message, 'plain'))
 
 
#send out the slightly more complex email
text = msg.as_string()
server.sendmail(email_address, recipient, text)

print("sent")
server.quit()