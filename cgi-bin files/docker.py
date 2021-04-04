
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

y14=x.getvalue("constop")
y15=x.getvalue("conpull")
y16=x.getvalue("version")
y17=x.getvalue("constart")

y18=x.getvalue("condel")
y19=x.getvalue("versiondel")
y20=x.getvalue("linux6")

y21=x.getvalue("conname")
y22=x.getvalue("tag")
y23=x.getvalue("ver")

y24=x.getvalue("conname2")
y25=x.getvalue("ver2")

y26=x.getvalue("conname3")

y27=x.getvalue("log1")


y28=x.getvalue("conname4")
y29=x.getvalue("comma")

if y28 is not None and y29 is not None:
  cmd="sudo docker exec {} {}".format(y28,y29)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))



if y27 is not None:
  cmd="sudo docker logs {}".format(y27)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))
  
if y26 is not None:
  cmd="sudo docker inspect {}".format(y26)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y21 is not None and y23 is not None:
  cmd="sudo docker commit {} {}:{}".format(y21,y22,y23)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y24 is not None and y25 is not None:
  cmd="sudo docker push {}:{}".format(y24,y25)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))



if cmd is not None:
  cmd="sudo {}".format(cmd)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y1 is not None:
  cmd="sudo docker ps -a"
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y2 is not None:
  cmd="sudo docker ps"
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y3 is not None:
  cmd="sudo docker images"
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y4 is not None:
  cmd="sudo docker network inspect"
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y5 is not None:
  cmd="sudo docker network ls"
  y=os.system(cmd)
  print("<pre>{}</pre>".format(y))

if y20 is not None:
  cmd="sudo docker container rm -f $(docker container ls -a -q)"
  y=subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))



if y6 is not None and y7 is not None: 
  if y8 is not None and y9 is not None:
    if y10 is not None and y11 is not None:
      cmd="sudo docker run -dit --name {} -v {}:{} -p {}:{} {}".format(y6,y9,y8,y11,y10,y7)
      y=subprocess.getoutput(cmd)
      print("<pre>{}</pre>".format(y))
    
    else:
      cmd="sudo docker run -dit --name {} -p {}:{} {}".format(y6,y9,y8,y7)
       y=subprocess.getoutput(cmd)
       print("<pre>{}</pre>".format(y))

  else:
    cmd="sudo docker run -dit --name {} {}".format(y6,y7)
    y=subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

else:
  pass


if y12 is not None:
  cmd="sudo docker container rm {}".format(y12)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y)))
  
if y13 is not None:
  cmd="sudo docker image rm -f {}".format(y13)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y14 is not None:
  cmd="sudo docker stop {}".format(y14)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))

if y15 is not None and y16 is not None:
   cmd="sudo docker pull {}:{}".format(y15,y16)
   y=subprocess.getoutput(cmd)
   print("<pre>{}</pre>".format(y))


if y17 is not None:
  cmd="sudo docker start {}".format(y17)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))


if y18 is not None and y19 is not None:
  cmd="sudo docker image rmi {}:{} -f".format(y18,y19)
  y=subprocess.getoutput(cmd)
  print("<pre>{}</pre>".format(y))




