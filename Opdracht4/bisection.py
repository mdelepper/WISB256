import math

def findRoot(f, a, b, epsilon):
    m = (a+b)/2

    if ( (f(a)*f(b) < 0) and math.fabs(b-a) > epsilon):
        if (f(a)*f(m) < 0):
            m = findRoot(f, a, m, epsilon)
        else:
            m = findRoot(f, m, b, epsilon)

    return m
