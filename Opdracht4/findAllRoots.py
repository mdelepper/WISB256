import math

def findRoot(f, a, b, epsilon):
    m = (a+b)/2
    if ( (f(a)*f(b) < 0) and math.fabs(b-a) > epsilon):
        if (f(a)*f(m) < 0):
            m = findRoot(f, a, m, epsilon)
        else:
            m = findRoot(f, m, b, epsilon)

    return m


def findallRoots(f, a, b, epsilon):
    lijst = [[a,b]]
    
    while(numRoots(lijst) < 4 and (lijst[0][1] - lijst[0][0]) > epsilon):
        lijst = halveerIntervallen(lijst)

    roots= []
    for j in lijst:
        if f(j[0])*f(j[1]) < 0 :
            roots.append(findRoot(f, j[0], j[1], epsilon))
    return roots
            
    
        
def numRoots(lijst):
    j = 0
    for i in lijst:
        if i[0]*i[1] < 1 :
            j += 1
    return j
        
          


def halveerIntervallen(lijst):
    hoi = []
    for i in lijst:
        m = (i[1] + i[0])/2
        hoi.extend(([i[0], m], [i[1], m]))
    return hoi
