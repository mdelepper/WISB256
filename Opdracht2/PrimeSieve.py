import time
import sys
import pickle
from math import ceil

T1 = time.perf_counter()

file = sys.argv[2]
fh = open(file, "w")

def SoE(N):
    zeef = list(range(2, N))
    
    for x in range(2, N+1):
        for y in range(x, ceil(N/x)):
            getal = x*y
            if getal in zeef:
                zeef.remove(getal)
    return zeef

N = int(sys.argv[1])
mijnZeef = SoE(N)

for k in mijnZeef:
    fh.write(str(k) +'\n')

T2 = time.perf_counter()

print ('Found ' + str(len(mijnZeef)) +' Prime numbers smaller than ' +str(N)+ ' in '+str(T2-T1)+' seconds')
