import random
import math
import sys

if len(sys.argv) != 3:
    seed = int(sys.argv[3])
    random.seed(seed)
    
try:
    N = int(sys.argv[1])                            #aantal experimenten
    l = float(sys.argv[2])                          #lengte van naald
    h = 0                                           #aantal hits
    
except:
    print ('Use: python3 estimate_pi.py N L')
    exit()

assert(l <= 1), "L should be smaller than 1"

def drop_needle(L):
    x_1 = random.random()
    hoek = random.vonmisesvariate(0,0)

    x_2 = x_1 + l*math.cos(hoek)

    if x_2 > 1 or x_2 < 0:
        return True
    else:
        return False

for x in range(N):
    if drop_needle(x) == True :
        h += 1
        
pi = (2*l*N)/h

print(str(h) + ' hits in ' + str(N) + ' tries \n' +'Pi = ' + str(pi))
