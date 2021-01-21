from os import *

system("sudo apt install aircrack-ng john -y ")

def control(f): #otrum ismi
   file=f+"pass.txt"
   if path.isfile(file):
       print(f" '{file}' zaten kirildlmis, sifre:")
       system("cat "+ file)
       exit()
   
def run():
   s=input("yeni oturum ismi: ").strip()
   if session=="":
       print(" [!] hatali giris ")
       exit()
   control(s)
   mac=input("mac address: ")
   cap=input("cap file   : ")
   os.system("rm .log.txt")
   open(f".{s}mac","w").write(mac)
   open(f"{s}.cap","w").write(cap)
   system(f"python3 set.py | john --stdin --session={s} --stdout | aircrack-ng -w - -b {mac} -l .{s}pass.txt {cap}")
   system(f"cat .{s}pass.txt >> passwords.txt")

for file in listdir("."):
    if file.endswith(".rec"):
       key=input("Onceki tarama devam ettirilsin mi? [y/n] : ")

if key.strip().lower()=="y":
   s=input("oturum ismi: ").strip()
   control(s)
   if path.isfile(s)==False:
       print("[!] oturum bulunamadi")
       exit()
   if not (f".{s}mac" in listdir(".") and f".{s}cap" in listdir(".")):
       print(" [!] eksik dosya")
       exit()
   mac=open(f".{s}mac","r").read().strip()
   cap=open(f".{s}cap","r").read().strip()
   system(f"python3 set.py | john --restore={s} | aircrack-ng -w - -b {mac} -l .{s}pass.txt " + cap)
   system(f"cat .{s}pass.txt >> passwords.txt")
else:
   run()

