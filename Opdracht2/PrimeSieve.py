import time
import sys
from math import ceil

T1 = time.perf_counter()

def SoE(N):
    zeef = list(range(1, N))
    
    for x in range(2, N+1):
        for y in range(2, ceil(N/x)):
            getal = x*y
            if getal in zeef:
                zeef.remove(getal)
    return zeef


# N = sys.argv[1]
# mijnZeef = SoE(N)

# python PrimeSieve.py 15000 primes.data

T2 = time.perf_counter()
