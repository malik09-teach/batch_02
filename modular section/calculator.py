import math 
import random
from datetime import datetime,timedelta
import os 
from pathlib import Path 
import sys




t__now =datetime.now()
print("start time:",t__now)
print ("factorial:",math.factorial(5))
print("underroot:",math.sqrt(49))


print(random.choice(["lather jacket","wool jacket","polythen"]))
print(random.randint(1,10))



curent_dir=Path.cwd()

newfile=curent_dir/"test.txt"
print(newfile)

print(curent_dir)







t__now =datetime.now()
print("end time :",t__now)

















from geometry import cirArea,squre,rArea
from signtific__cal import sinval,cosin




num=int(input("enter number for squre:"))

squre(num)

sin_value=sinval(80)
print ("sin value:",sin_value)

sin_value=cosin(80)
print ("cosin value:",sin_value)




import sys
import math 

math.factorial()


print ("cirArea" in sys.modules)