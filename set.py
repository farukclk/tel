
  GNU nano 3.2                                                                                set.py                                                                                 Modified  

import time, os, sys

if os.path.isfile(".log.txt"):
 f=open(".log.txt","r")
 list=f.read().split()
 f.close()
else:
 os.system("touch .log.txt")
 list=["312","0312",

"530","0530","531","0531","532","0532","533","0533","534","0534","535","0535",
"536","0536","537","0537","538","0538","539","0539","561","0561",

"501","0501","505","0505","506","0506","507","0507",
"551","0551","552","0552","553","0553","554","0554","555","0555","559",
"0559",
"540","0540","541","0541","542","0542","543","0543","544","0544","545",
"0545","546","0546","547","0547","548","0548","549","0549"]
 f=open(".log.txt","w")
 for i in list:
  f.write(str(i)+" ")

list2=list[:]
for i in list:
 with open("tel.txt","r") as file:
  for  ii in file:
     print(str(i).strip()+ii.strip())
  if len(list2)==0:
    os.system("touch taramaBitti")
    os.system("rm .log.txt")
    exit()
  f=open(".log.txt","w")
  list2=list2[1:]
  for no, b in list2:
    f.write(str(b)+" ")
  f.close()
