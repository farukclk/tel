import os, sys
os.system("touch .log.txt")
lo=open(".log.txt","r").read()
if lo!="" and os.path.isfile(".cap") and os.path.isfile(".mac"):
 
  key=input("Onceki tarama devam ettirilsin mi? [y/n] : ")
  if key.strip()=="y" or key.strip=="Y":
   mac=open(".mac","r").read()
   cap=open(".cap","r").read()
  else:
   mac=input("mac address: ")
   cap=input("cap file   : ")
   os.system("rm .log.txt")
   open(".mac","w").write(mac)
   open("cap","w").write(cap)
else:
   mac=input("mac address: ")
   cap=input("cap file   : ")
   os.system("rm .log.txt")
   open(".mac","w").write(mac)
   open("cap","w").write(cap)

os.system("python3 set.py | aircrack-ng -w - -b " + mac + " " + cap)
