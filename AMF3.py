import time,os,sys,random
from sys import platform
from random import randint
msg0=('''+----------------------------------------------+
| Name:        PhoneNumber{ABO NASR}
| Author:      ABONASR
|
Whatsapp +5493517554356
+----------------------------------------------+''')
for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
if platform.startswith("win"):
    os.system("cls")
if "linux" in platform:
    os.system("clear")
if "unix" in platform:
    os.system("clear")
numbers = input("how much number do you want to generate:")
number = int(numbers)
gentype = "123456789"
countrycode = input("Give me the countrycode to generate phone numbers without +:")
for x in range(number):
    generatestarted1 = random.choice(gentype)
    generatestarted2 = random.choice(gentype)
    generatestarted3 = random.choice(gentype)
    generatestarted4 = random.choice(gentype)
    generatestarted5 = random.choice(gentype)
    generatestarted6 = random.choice(gentype)
    generatestarted7 = random.choice(gentype)
    generatestarted8 = random.choice(gentype)
    generatestarted9 = random.choice(gentype)
    generatestarted10 = random.choice(gentype)
    generatestarted = str(("+"+countrycode+generatestarted1+generatestarted2+generatestarted3+generatestarted4+generatestarted5+generatestarted6+generatestarted7+generatestarted8+generatestarted9+generatestarted10))
    savenumbers = open("PhoneNumbers.txt","a").write(generatestarted+"\n")
