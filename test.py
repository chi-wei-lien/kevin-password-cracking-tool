import pexpect

guess = "zxo"
try:
  child = pexpect.spawn("mysql -u root -p" + guess)
  i = child.expect('mysql> ')
  print("[*] " + guess + " |  success")

except:
  print("[*] " + guess + " |  failed")
