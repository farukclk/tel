from os import system, path, listdir

system("sudo apt install aircrack-ng john -y ")

def yaz(dosya, value):
    d=open(dosya, "w")
    d.write(value)
    d.close()

def control(f): #otrum ismi
   file="." + f + "pass.txt"
   if path.isfile(file):
       print(f" '{file}' zaten kirildlmis, sifre:")
       system("cat "+ file)
       exit()
   

key=""
for file in listdir("."):
    if file.endswith(".rec"):
       while True:
           key=input("Onceki tarama devam ettirilsin mi? [y/n] : ").strip().lower()
           if key=="y" or key=="n":
               break
       break
print()
if key.strip().lower()=="y":
   s=input("oturum ismi: ").strip()
   control(s)
   if path.isfile(s + ".rec")==False:
       print("[!] oturum bulunamadi")
       exit()
   elif not (f".{s}mac" in listdir(".") and f".{s}cap" in listdir(".")):
       print(" [!] eksik dosya")
       exit()
   mac=open(f".{s}mac","r").read().strip()
   cap=open(f".{s}cap","r").read().strip()
   system(f"python3 set.py | john --restore={s} | aircrack-ng -w - -b {mac} -l .{s}pass.txt " + cap)
   system(f"cat .{s}pass.txt >> passwords.txt")
else:
   s=input("yeni oturum ismi: ").strip()
   control(s)
   if s=="":
       print(" [!] hatali giris ")
       exit()
   elif s + ".rec" in listdir("."):
       print("{!] bu isimde oturum zaten mevcut")
       exit()

   mac=input("mac address: ").strip()
   cap=input("cap file   : ").strip()
   yaz(f".{s}mac", mac)
   yaz(f".{s}cap", cap)
   system(f"python3 set.py | john --stdin --session={s} --stdout | aircrack-ng -w - -b {mac} -l .{s}pass.txt {cap}")
   system(f"cat .{s}pass.txt >> passwords.txt")


