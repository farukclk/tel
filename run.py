import os, sys
os.system("sudo apt install aircrack-ng -y ")
os.system("touch .log.txt")
lo=open(".log.txt","r").read()
if lo!="" and os.path.isfile(".cap") and os.path.isfile(".mac"):
 
  key=input("Onceki tarama devam ettirilsin mi? [y/n] : ")
  if key.strip()=="y" or key.strip=="Y":
   mac=open(".mac","r").read().strip()
   cap=open(".cap","r").read().strip()
  else:
   mac=input("mac address: ")
   cap=input("cap file   : ")
   os.system("rm .log.txt")
   open(".mac","w").write(mac)
   open(".cap","w").write(cap)
else:
   mac=input("mac address: ")
   cap=input("cap file   : ")
   os.system("rm .log.txt")
   open(".mac","w").write(mac)
   open(".cap","w").write(cap)

os.system("sudo python3 set.py | sudo aircrack-ng -w - -b " + mac + " -l sifreler.txt "+ cap)
