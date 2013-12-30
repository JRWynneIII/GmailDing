#!/usr/bin/env python

import imaplib
import time
import pygame
import pynotify
import subprocess

def main():
	uname = raw_input("Username: ")
	passwrd = raw_input("Password: ")
	
	if not "@gmail.com" in uname:
		uname += "@gmail.com"
	
	account = imaplib.IMAP4_SSL('imap.gmail.com')
	account.login(uname, passwrd)
	account.select("INBOX")
	result, data = account.uid('search', None, "ALL") # search and return uids instead
	latest_email_uid = data[0].split()[-1]
	result, data = account.uid('fetch', latest_email_uid, '(RFC822)')

	print "Running..."
	subprocess.Popen(['notify-send', "Running...."])

	while True:
		account.select("INBOX")
		result, data = account.uid('search', None, "ALL") # search and return uids instead
		latest_email_uid_new = data[0].split()[-1]
		if (latest_email_uid_new != latest_email_uid):
			print "New Email!"
			subprocess.Popen(['notify-send', "New Email!"])
			pygame.init()
			pygame.mixer.music.load("/home/jake/Projects/python/gmailding/tone_alert.mp3")
			pygame.mixer.music.play()
			time.sleep(10)
		latest_email_uid = latest_email_uid_new

if (__name__ == "__main__"):
	main()
