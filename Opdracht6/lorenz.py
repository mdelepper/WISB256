import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(self.xs, self.ys, self.zs)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.show()
