#!/usr/bin/python3

import cgi
import subprocess
import os

print("content-type: text/html")
print()

x = cgi.FieldStorage()
cmd = x.getvalue("cmd")
y1 = x.getvalue("linux1")
y2 = x.getvalue("linux2")
y3 = x.getvalue("linux3")
y4 = x.getvalue("linux4")
y5 = x.getvalue("linux5")
y6 = x.getvalue("linux6")
y7 = x.getvalue("linux7")
y8 = x.getvalue("linux8")
y9 = x.getvalue("linux9")
y10 = x.getvalue("linux10")

ip = x.getvalue("ip")
pn1 = x.getvalue("pn1")
pn2 = x.getvalue("pn2")
pn3 = x.getvalue("pn3")
pn4 = x.getvalue("pn4")

pn5 = x.getvalue("pn5")
pn6 = x.getvalue("pn6")
pn7 = x.getvalue("pn7")
pn8 = x.getvalue("pn8")
pn9 = x.getvalue("pn9")
pn10 = x.getvalue("pn10")
pn11 = x.getvalue("pn11")
pn12 = x.getvalue("pn12")
pn13 = x.getvalue("pn13")
pn14 = x.getvalue("pn14")
pn15 = x.getvalue("pn15")
pn16 = x.getvalue("pn16")
pn17 = x.getvalue("pn17")
pn18 = x.getvalue("pn18")
pn19 = x.getvalue("pn19")
pn20 = x.getvalue("pn20")
pn21 = x.getvalue("pn21")
pn22 = x.getvalue("pn22")
pn23 = x.getvalue("pn23")
pn24 = x.getvalue("pn24")
pn25 = x.getvalue("pn25")
pn26 = x.getvalue("pn26")
pn27 = x.getvalue("pn27")
pn28 = x.getvalue("pn28")
pn29 = x.getvalue("pn29")
pn30 = x.getvalue("pn30")
pn31 = x.getvalue("pn31")
pn32 = x.getvalue("pn32")
pn33 = x.getvalue("pn33")
pn34 = x.getvalue("pn34")
pn35 = x.getvalue("pn35")
pn36 = x.getvalue("pn36")
pn37 = x.getvalue("pn37")
pn38 = x.getvalue("pn38")
pn39 = x.getvalue("pn39")
pn40 = x.getvalue("pn40")
pn41 = x.getvalue("pn41")
pn42 = x.getvalue("pn42")
pn43 = x.getvalue("pn43")
pn44 = x.getvalue("pn44")
pn45 = x.getvalue("pn45")
pn46 = x.getvalue("pn46")
pn47 = x.getvalue("pn47")
pn48 = x.getvalue("pn48")
pn49 = x.getvalue("pn49")
pn50 = x.getvalue("pn50")
pn51 = x.getvalue("pn51")
pn52 = x.getvalue("pn52")
pn53 = x.getvalue("pn53")
pn54 = x.getvalue("pn54")
pn55 = x.getvalue("pn55")
pn56 = x.getvalue("pn56")
pn57 = x.getvalue("pn57")
pn58 = x.getvalue("pn58")
pn59 = x.getvalue("pn59")
pn60 = x.getvalue("pn60")
pn61 = x.getvalue("pn61")
pn62 = x.getvalue("pn62")
pn63 = x.getvalue("pn63")
pn64 = x.getvalue("pn64")
pn65 = x.getvalue("pn65")
pn66 = x.getvalue("pn66")
pn67 = x.getvalue("pn67")
pn68 = x.getvalue("pn68")
pn69 = x.getvalue("pn69")
pn70 = x.getvalue("pn70")
pn71 = x.getvalue("pn71")
pn72 = x.getvalue("pn72")
pn73 = x.getvalue("pn73")
pn74 = x.getvalue("pn74")
pn75 = x.getvalue("pn75")
pn76 = x.getvalue("pn76")
pn77 = x.getvalue("pn77")
pn78 = x.getvalue("pn78")
pn79 = x.getvalue("pn79")
pn80 = x.getvalue("pn80")


if pn79 is not None and pn80 is not None:
    cmd = "sudo chgrp {} {}".format(pn80, pn79)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn77 is not None and pn78 is not None:
    cmd = "sudo useradd -G {} {}".format(pn78, pn77)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn76 is not None:
    cmd = "sudo groupadd {}".format(pn76)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn74 is not None and pn75 is not None:
    cmd = "sudo chown {} {}".format(pn74, pn75)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn72 is not None and pn73 is not None:
    cmd = "sudo chmod {} {}".format(pn72, pn73)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn69 is not None:
    cmd = "sudo finger {}".format(pn69)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn70 is not None:
    cmd = "id -u {}".format(pn70)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if p71 is not None:
    cmd = "id -g {}".format(pn71)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn45 is not None:
    cmd = "sudo pvcreate {}".format(pn45)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn46 is not None:
    cmd = "pvdisplay {}".format(pn41)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn47 is not None:
    cmd = "vgcreate {} {} {}".format(pn47, pn48, pn49)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn50 is not None:
    cmd = "lvcreate --size {} --name {} {}".format(pn50, pn51, pn52)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn54 is not None:
    cmd = "vgdisplay {}".format(pn54)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn53 is not None:
    cmd = "lvdisplay {}".format(pn53)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn55 is not None:
    cmd = "mkfs.ext4 {}".format(pn55)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn56 is not None and pn57 is not None:
    cmd = "sudo mount {} {}".format(pn56, pn57)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn58 is not None and pn59 is not None:
    cmd = "sudo lvextend --size {} {}".format(pn58, pn59)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn60 is not None:
    cmd = "sudo resize2fs {}".format(pn60)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn61 is not None and pn62 is not None:
    cmd = "sudo vgextend  {} {}".format(pn61, pn62)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn63 is not None:
    cmd = "sudo unmount {}".format(pn63)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn64 is not None:
    cmd = "sudo e2fsck -f {}".format(pn64)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn65 is not None and pn66 is not None:
    cmd = "sudo resize2fs  {} {}".format(pn65, pn66)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn67 is not None and pn68 is not None:
    cmd = "sudo lvreduce --size {} {}".format(pn67, pn68)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn41 is not None:
    cmd = "mkfs.ext4 {}".format(pn41)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn43 is not None and pn44 is not None:
    cmd = "mount {} {}".format(pn43, pn44)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn44 is not None:
    cmd = "unmount {}".format(pn44)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn40 is not None:
    cmd = "fdisk -l {}".format(pn40)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn30 is not None:
    cmd = "sshpass - p {} scp {}  {}:{}".format(pn30, pn32, pn31, pn33)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn39 is not None:
    cmd = "sshpass  - p {} scp -r {}  {}:{}".format(pn30, pn39, pn31, pn33)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn34 is not None:
    cmd = "sshpass - p {} scp {}:{} {}".format(pn34, pn35, pn37, pn36)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn38 is not None:
    cmd = "sshpass - p {} scp -r  {}:{}  {}".format(pn34, pn35, pn38, pn36)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn29 is not None:
    cmd = "ssh - p {} {} {}".format(pn27, pn29, pn28)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn25 is Not None and pn26 is not None:
    cmd = "sudo grep {}  {}".format(pn25, pn26)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn24 is Not None and pn26 is not None:
    cmd = "sudo grep -n {}  {}".format(pn24, pn26)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn23 is not None:
    cmd = "sudo wc {}".format(pn23)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn22 is not None:
    cmd = "sudo {}>status.txt".format(pn22)
    y = subprocess.getoutput(cmd)

    read = "sudo cat status.txt"
    y2 = subprocess.getoutput(read)
    print("<pre>{}</pre>".format(y2))


if pn21 is not None:
    cmd = "sudo rpm -qf {}".format(pn21)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn20 is not None:
    cmd = "sudo which {}".format(pn20)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn19 is not None:
    cmd = "suod rpm -qi {}".format(pn19)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn18 is not None:
    cmd = "sudo rpm -i".format(pn18)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn17 is not None:
    cmd = "sudo rpm -e {}".format(pn17)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn16 is not None:
    cmd = "sudo rpm -q {}".format(pn16)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn15 is not None and pn14 is not None:
    cmd = "cat {} {}".format(pn14, pn15)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn10 is not None:
    cmd = "cd {}".format(pn10)
    y = subprocess.getoutput(cmd)
    y2 = "Directory changed to {}".format(pn10)
    print(y2)


if pn9 is not None:
    cmd = "ls -l {}".format(pn9)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn8 is not None:
    cmd = "id {}".format(pn8)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn6 is not None and pn7 is not None:
    cmd1 = "sudo useradd {}".format(pn6)
    cmd2 = "echo {} | passwd --stdin {}".format(pn7, pn6)
    y1 = subprocess.getoutput(cmd1)
    y2 = subprocess.getoutput(cmd2)
    print("<pre>{}</pre>".format(y1))


if pn5 is not None:
    cmd = "nslookup {}".format(pn5)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if pn4 is not None:
    cmd = "sudo kill {}".format(pn4)
    y = subprocess.getoutput(cmd)
    y2 = "Appended"
    print("<pre>{}</pre>".format(y2))

if pn12 is not None and pn13 is not None:
    cmd = "echo {}|cat >> {}".format(pn12, pn13)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn11 is not None and pn13 is not None:
    cmd = "echo {}|cat > {}".format(pn11, pn13)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn3 is not None:
    cmd = "sudo jobs"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn1 is not None:
    cmd = "sudo {} &".format(pn1)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if pn2 is not None:
    cmd = "sudo man {}".format(pn2)
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if cmd is not None:
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if y1 is not None:
    y = subprocess.getoutput("ifconfig")
    print("<pre>{}</pre>".format(y))

if y2 is not None:
    y = subprocess.getoutput("cal")
    print("<pre>{}</pre>".format(y))

if y3 is not None:
    cmd = "ps -aux"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))
if y4 is not None:
    cmd = "tty"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))
if y5 is not None:
    cmd = "sudo route -n"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if y6 is not None:
    cmd = "sudo setenforce 0"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))


if y7 is not None:
    cmd = "sudo setenforce 1"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if y8 is not None:
    cmd = "fdisk -l"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if y9 is not None:
    cmd = "sudo chronyc sources"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if y9 is not None:
    cmd = "sudo groups"
    y = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(y))

if ip is not None:
    cmd = "ping {}".format(ip)
    y = os.system(cmd)
    print("<pre>{}</pre>".format(y))
