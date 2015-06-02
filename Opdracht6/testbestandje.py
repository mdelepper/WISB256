import lorenz
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

f = lorenz.Lorenz([-1,1,0])
u = f.solve(50,.01)

xlijst = []
ylijst = []
zlijst = []

for i in range(int(50/0.01)):
    xlijst.append(u[i][0])
    ylijst.append(u[i][1])
    zlijst.append(u[i][2])

    
ax.plot(xlijst, ylijst, zlijst)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.show()
