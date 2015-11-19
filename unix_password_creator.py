import hashlib, argparse, base64
from random import randint
from datetime import date


def createMD5Hash(plainPassword):
	salt = "1Ha7"
	hash = hashlib.md5(plainPassword + salt).digest()
	return salt, base64.b64encode(hash)

def writeStringToPasswordFile(string):
	f = open('passwordTest/passwd.txt', 'a')
	f.write(string)

def writeStringToShadowFile(string):
	f = open('passwordTest/shadow.txt', 'a')
	f.write(string)

def getNewUserID():
	return randint(101,2000)

def getGroupID():
	#random group id. "users"
	return 100

def calculateDaysSince1970():
	d0 = date.today()
	d1 = date(1970, 1, 1)
	delta = d0 - d1
	return delta.days

def appendToShadowFile(username, password):
	#username
	writeStringToShadowFile(username)
	#password hash
	salt, hash = createMD5Hash(password)
	writeStringToShadowFile(":$1$" + salt + "$" + hash)
	#last password change 
	writeStringToShadowFile(":" + str(calculateDaysSince1970()))
	#minumun days till pw change
	writeStringToShadowFile(":0")
	#maximum days till pw change
	writeStringToShadowFile(":99999")
	#Warn, Inactive and Expire
	writeStringToShadowFile(":7:::")

def appendToPasswdFile(username):
	#username
	writeStringToPasswordFile(username)
	#going to store the password in the shadow file
	writeStringToPasswordFile(":x")
	#User ID (UID)
	writeStringToPasswordFile(":" + str(getNewUserID()))
	#Group ID (GID)
	writeStringToPasswordFile(":" + str(getGroupID()))
	#User ID Info
	writeStringToPasswordFile(":" + "Info for " + username)
	#Home Directory
	writeStringToPasswordFile(":" + "/home/")# +username)
	#Command/Shell
	writeStringToPasswordFile(":" + "/bin/bash")

def main(username, password):
	appendToPasswdFile(username)
	appendToShadowFile(username, password)



if __name__== '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("username")
	parser.add_argument("password")
	args = parser.parse_args()
	main(args.username, args.password)
