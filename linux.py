#!/usr/bin/python3

import cgi
import subprocess
import os

print("content-type: text/html")
print()

x=cgi.FieldStorage()
cmd=x.getvalue("cmd")
y1=x.getvalue("linux1")
y2=x.getvalue("linux2")
y3=x.getvalue("linux3")
ip= x.getvalue("ip")

if cmd is not None:
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y1 is not None:
  y=subprocess.getoutput("ifconfig")
  print("<pre>{}</pre>".format(y))

if y2 is not None:
  y=subprocess.getoutput("cal")
  print("<pre>{}</pre>".format(y))

if y3 is not None:
  cmd="ps -aux"
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))



if ip is not None:
  cmd="ping {}".format(ip)
  y=os.system(cmd)
  print("<pre>{}</pre>".format(y))


