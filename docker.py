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
y4=x.getvalue("linux4")
y5=x.getvalue("linux5")


y6=x.getvalue("nameco")
y7=x.getvalue("nameim")
y8=x.getvalue("cport")
y9=x.getvalue("dhport")
y10=x.getvalue("cvol")
y11=x.getvalue("dhvol")

y12=x.getvalue("namecon")
y13=x.getvalue("nameima")

if cmd is not None:
  cmd="sudo {}".format(cmd)
  y=subprocess.getoutput(cmd)
  print(y)

if y1 is not None:
  cmd="sudo docker ps -a"
  y=subprocess.getoutput(cmd)
  print(y)

if y2 is not None:
  cmd="sudo docker ps"
  y=subprocess.getoutput(cmd)
  print(y)

if y3 is not None:
  cmd="sudo docker images"
  y=subprocess.getoutput(cmd)
  print(y)

if y4 is not None:
  cmd="sudo docker network inspect"
  y=subprocess.getoutput(cmd)
  print(y)

if y5 is not None:
  cmd="sudo docker network ls"
  y=os.system(cmd)
  print(y)


if y6 is not None and y7 is not None: 
  if y8 is not None and y9 is not None:
    if y10 is not None and y11 is not None:
      cmd="sudo docker run -dit --name {} -v {}:{} -p {}:{} {}".format(y6,y9,y8,y11,y10,y7)
      y=subprocess.getoutput(cmd)
      print(y)
    
    else:
      cmd="sudo docker run -dit --name {} -p {}:{} {}".format(y6,y9,y8,y7)
       y=subprocess.getoutput(cmd)
       print(y)
  else:
    cmd="sudo docker run -dit --name {} {}".format(y6,y7)
    y=subprocess.getoutput(cmd)
    print(y)
else:
  pass


if y12 is not None:
  cmd="sudo docker container rm {}".format(y12)
  y=subprocess.getoutput(cmd)
  print(y)
  
if y13 is not None:
  cmd="sudo docker image rm -f {}".format(y13)
  y=subprocess.getoutput(cmd)
  print(y)
