import math

class Vector:


    def __init__(self, n, a = 0.0):
        if type(a) == list:
            self.v = a
        else:
            self.v = [a]*n

    def __str__(self):
        vector = ''
        for item in self.v:
            vector = vector + "{0:.6f}".format(item)+'\n'
            
        return str(vector)

    def lincomb(self, other, alpha, beta):
        w = Vector(len(self.v))
    
        w = self.scalar(alpha) + other.scalar(beta)
        return w

    def __add__(self, other):
        w = Vector(len(self.v))
        for i in range(len(self.v)):
            w.v[i] = self.v[i] + other.v[i]
        return w

    def __sub__(self, other):
        w = Vector(len(self.v))
        for i in range(len(self.v)):
            w.v[i] = self.v[i] + other.v[i]
        return w

    def scalar(self, alpha):
        w = Vector(len(self.v))
        for i in range(len(w.v)):
            w.v[i]= alpha*self.v[i]

        return w

    def inner(self, other):
        res = 0.0
        for i in range(len(self.v)):
            res += self.v[i]*other.v[i]
        return "{0:.6f}".format(res)

    def norm(self):
        res = self.inner(self)
        return "{0:.6f}".format(math.sqrt(float(res)))
   
def GrammSchmidt(V):
    lijst = V
    for i in range(len(lijst)):
        lijst[i] = lijst[i].scalar(1/( float(lijst[i].norm()) ))
        for j in range(i+1, len(lijst)):
            ratio = float( lijst[i].inner(lijst[j]) ) / float(lijst[j].norm())
            lijst[j] = lijst[j] - lijst[j].scalar(ratio)
        return lijst
