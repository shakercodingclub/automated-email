import smtplib
import random


#login to secret santa email account to be used
email_address = "young.secretive.santa@gmail.com"
password = "placeholder_password"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, password)

#open participant emails text file and parse data
#each line goes "first_name last_name,emailaddress@email.com"
fp = open('.\emails.txt')

participants = [[], []]

for line in fp:
	line = line.strip()
	row = line.split(',')
	participants[0].append(row[0])
	participants[1].append(row[1])

#assign
assignments = random.sample(range(0, len(participants[0])), len(participants[0]))

#simplistic and probably suboptimally preventing self-assignment of secret santa
while(True):
	breakL = True
	for i in range(0, len(assignments)):
		if (i == assignments[i]):
			assignments = random.sample(range(0, len(participants[0])), len(participants[0]))
			breakL = False
			break
			
	if (breakL):
		break

#matches up each participant with assignment and sends mail.
for i in range(0, len(participants[0])):
	
	msg = participants[0][i] + ", your secret santa assignment is " + participants[0][assignments[i]] + "\n\nbtw guys lets set some grounds rules\nrule 1: no books\nrule 2: that'll be all"
	server.sendmail(email_address, participants[1][i], msg)
	
server.quit()
print("sent")