#!/usr/bin/python
from ftplib import FTP
import os
def ftpDownloader(filename,host="ftp.pyclass.com",user="student@pyclass.com",password="student123"):
	ftp=FTP(host)
	ftp.login(user,password)
	print(ftp.nlst())
	ftp.cwd("Data")
	os.chdir("/Users/prem/Documents/pyLearn")
	with open(filename,'wb') as file:
		ftp.retrbinary('RETR %s' % filename,file.write)

ftpDownloader("isd-lite-format.pdf")
