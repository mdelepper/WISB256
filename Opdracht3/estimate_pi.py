import random
import math
import sys

N = int(sys.argv[1]) #aantal experimenten
l = float(sys.argv[2]) #lengte van naald

assert l <= 1


h = 0 #aantal hits

def drop_needle(L):
    x_1 = random.random()
    y_2 = random.random()
    hoek = random.vonmisesvariate(0,0)

    x_2 = x_1 + l*math.cos(hoek)

    if x_2 > 1:
        return True
    else:
        return False

for x in range(N):
    if drop_needle(x) == True:
        h += 1

print(h)
