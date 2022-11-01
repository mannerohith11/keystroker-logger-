# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
import time

f=open('output.txt','w').close()


def sendmail():
# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("abc@gmail.com", "abcdef")
	f=open('output.txt','r')



schedule.every().day.at("12:00").do(sendmail)
