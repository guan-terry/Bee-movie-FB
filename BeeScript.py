import fbchat
import getpass
import time
import random

# Run by typing winpty py BeeScript.py
user = input('Username/Email: ')
client = fbchat.Client(user, getpass.getpass())
friends = client.searchForUsers(input('friend name: '))
friend = friends[0]
f = open('Bee Movie Script.txt')
lines = f.readlines()
for line in lines:
    if line.strip() == '':
        continue
    time.sleep(random.uniform(.2, .5))
    sent = client.sendMessage(line, thread_id = friend.uid)
