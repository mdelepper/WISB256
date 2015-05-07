import time
import sys
import pickle
from math import ceil

T1 = time.perf_counter()

file = sys.argv[2]
fh = open(file, "w")
i=0

def SoE(N):
    zeef = list(range(2,N))
    
    for x in zeef:
        if x != 0:
            for y in range(x, ceil(N/x)):
                zeef[x*y - 2] = 0
    return zeef

N = int(sys.argv[1])
mijnZeef = SoE(N)

for k in mijnZeef:
    if k != 0:
        i += 1
        fh.write(str(k) +'\n')

T2 = time.perf_counter()

print ('Found ' + str(i) +' Prime numbers smaller than ' +str(N)+ ' in '+str(T2-T1)+' seconds')
