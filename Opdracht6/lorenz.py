import numpy as np
import scipy as sp
from scipy.integrate import odeint
from scipy import linalg as la
from math import *

class Lorenz:

    def __init__(self, coordinaten, sigma = 10.0, rho = 28.0, beta = 8/3):
        self.s = float(sigma)
        self.r = float(rho)
        self.b = float(beta)
        self.xs = coordinaten[0]
        self.ys = coordinaten[1]
        self.zs = coordinaten[2]
        

    def solve(self, T, dt):
        T = int(T)
        dt = float(dt)
        looptijd = [0]*ceil(T/dt)
        for i in range(len(looptijd)):
            looptijd[i] = i*dt
        
        return odeint(self.lorenz, [self.xs, self.ys, self.zs], looptijd)

    def lorenz(self, lijst, t):
        x = lijst[0]
        y = lijst[1]
        z = lijst[2]
        x_dot = self.s*(y - x)
        y_dot = x*(self.r - z) - y
        z_dot = x*y - self.b*z
        return [x_dot, y_dot, z_dot]
    
    def df(u):
        
        jacobi = np.array([0]*3,[0]*3,[0]*3)
        jacobi[0][0] = -1*self.s
        jacobi[0][1] = self.s
        jacobi[1][0] = self.r - u[2]
        jacobi[1][1] = -1
        jacobi[1][2] = u[0]
        jacobi[2][0] = u[1]
        jacobi[2][1] = u[0]
        jacobi[2][2] = -1*self.b

        return jacobi

    def isStable(u):
        res = df(u)
        w = la.eig(res)

        if (w[0] < 0 and w[1] < 0 and w[2] < 0):
            return True
        else:
            return False




        
