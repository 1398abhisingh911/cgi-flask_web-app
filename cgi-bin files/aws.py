#!/usr/bin/python3

import cgi
import subprocess
import os

print("content-type: text/html")
print()

x=cgi.FieldStorage()
y0=x.getvalue("keyname")
y1=x.getvalue("sgname")
y2=x.getvalue("itype")
y3=x.getvalue("no")
y4=x.getvalue("key")
y5=x.getvalue("sgid")
y6=x.getvalue("amid")


if y0 is not None:
  cmd="sudo aws ec2 create-key-pair --key-name {}".format(y0)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y1 is not None:
  cmd="sudo aws ec2 create-security-group --group-name {}".format(y1)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y2 is None or y3 is None or y4 is None or y5is None or y6 is None:
  pass
else:
  cmd="sudo aws run-instances --security-group-ids {} {} --count {} --image-id {} --key-name {}".format(y5,y2,y3,y6,y4)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))




