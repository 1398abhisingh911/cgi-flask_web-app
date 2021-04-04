#!/usr/bin/python3

import cgi
import subprocess
import os

print("content-type: text/html")
print()

x=cgi.FieldStorage()
y1=x.getvalue("linux1")
y2=x.getvalue("linux2")


if y1 is not None:
  cmd="ansible-playbook cluster.yml"
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))


if y2 is not None:
  cmd="ansible-playbook task11master.yml"
  cmd2="ansible-playbook task11slave.yml"
  y=subprocess.getoutput(cmd)
  y2=subprocess.getoutput(cmd2)
  print("<pre>{}</pre>".format(y))
  print("<pre>{}</pre>".format(y2))



