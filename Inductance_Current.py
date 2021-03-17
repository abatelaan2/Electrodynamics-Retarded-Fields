from scipy.integrate import quad
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.widgets import Slider, Button, RadioButtons

x_list=[]
distance_step = 0.2
n=-1.05
while n <= 1.05:
    x_list.append(round(n,3))
    n = round(n +distance_step,3)

print(x_list)

y_list=[]
n=-1.05
while n<= 1.05:
    y_list.append(round(n,3))
    n = round(n + distance_step, 3)

t_list=[]
time_step = 0.1
time_stop = 20
n=0
while n<= time_stop:
    t_list.append(n)
    n+=time_step

class point():
    def __init__(self,t,x,y,A_z,B_x,B_y,E_z):
        self.t = t
        self.x = x
        self.y = y
        self.A_z = A_z
        self.B_x = B_x
        self.B_y = B_y
        self.E_z = E_z

def integrand(t, x, y, z):
    return (1-np.exp(-(1) * (t - np.sqrt(x ** 2 + y ** 2 + z ** 2)))) / np.sqrt(x ** 2 + y ** 2 + z ** 2)

def integrandB(t, x, y, z):
    return np.sqrt(x**2+y**2)*(math.e**(-(1) * (t - np.sqrt(x ** 2 + y ** 2 + z ** 2)))) / (x ** 2 + y ** 2 + z ** 2) + np.sqrt(x**2+y**2)*(1-math.e**(-(1) * (t - np.sqrt(x ** 2 + y ** 2 + z ** 2)))) / (x ** 2 + y ** 2 + z ** 2)**(3/2)

def integrandE(t, x, y, z):
    return -np.exp(-(t-np.sqrt(x**2+y**2+z**2)))/np.sqrt(x**2+y**2+z**2)

point_list = []
n=0
while n<=len(t_list)-1:
    m=0
    while m<=len(x_list)-1:
        l=0
        while l<=len(y_list)-1:
            t = t_list[n]
            x = x_list[m]
            y = y_list[l]
            if t**2 < x**2 + y**2:
                point_list.append(point(t_list[n], x_list[m], y_list[l], 0, 0, 0, 0))
            elif np.sqrt(t**2 - (x**2 + y**2)) <= 10:
                limit_1= -np.sqrt(t**2-(x**2+y**2))
                limit_2= np.sqrt(t**2-(x**2+y**2))
                I = quad(integrand, limit_1, limit_2, args=(t,x,y))
                J = quad(lambda z:integrandB(t,x,y,z), limit_1, limit_2)
                K = quad(lambda z:integrandE(t,x,y,z), limit_1, limit_2)
                point_list.append(point(t_list[n],x_list[m],y_list[l],I[0], -J[0]*y/np.sqrt(x**2+y**2), J[0]*x/np.sqrt(x**2+y**2), K[0]))
            else:
                limit_1= -10
                limit_2= 10
                I = quad(integrand, limit_1, limit_2, args=(t,x,y))
                J = quad(lambda z:integrandB(t,x,y,z), limit_1, limit_2)
                K = quad(lambda z:integrandE(t,x,y,z), limit_1, limit_2)
                point_list.append(point(t_list[n],x_list[m],y_list[l],I[0], -J[0]*y/np.sqrt(x**2+y**2), J[0]*x/np.sqrt(x**2+y**2), K[0]))
            l+=1
        m+=1
    n+=1

x_point = 0.2

fig = plt.figure()
ax2 = fig.add_subplot(111, projection='3d')

ax2.title.set_text("Wire Segment: I(t)=1-$e^{-t}$")
line = art3d.Line3D([0,0], [0,0], [-1,1], color='black')
ax2.add_line(line)
ax2.set_xlim(-1, 1)
ax2.set_ylim(-1, 1)
ax2.set_zlim(-1, 1)
for object in point_list:
    if object.t == 0.05:
        ax2.quiver(object.x, object.y, 0, 0, 0, object.E_z, length=0.5, color='red')
        ax2.quiver(object.x, object.y, 0, object.B_x, object.B_y, 0, length=0.1, color='blue')


t0=0
axhauteur = plt.axes([0.2, 0.1, 0.65, 0.03])
shauteur = Slider(axhauteur, 'Time', 0, time_stop, valinit=t0)

def update(val):
    t = shauteur.val
    ax2.clear()
    ax2.title.set_text("Wire Segment: I(t)=1-$e^{-t}$")
    line = art3d.Line3D([0, 0], [0, 0], [-1, 1], color='black')
    ax2.add_line(line)
    for object in point_list:
        if object.t <= t and object.t > t-time_step:
            ax2.quiver(object.x, object.y, 0, 0, 0, object.E_z, length=0.5, color='red')
            ax2.quiver(object.x, object.y, 0, object.B_x, object.B_y, 0, length=0.1, color='blue')
            ax2.set_xlim(-1, 1)
            ax2.set_ylim(-1, 1)
            ax2.set_zlim(-1, 1)
            fig.canvas.draw_idle()
shauteur.on_changed(update)

plt.show()

# t=[]
# B=[]
# E=[]
# A=[]
#
# for object in point_list:
#     if object.x == x_point and object.y == x_point:
#         t.append(object.t)
#         B.append(object.B_x)
#         E.append(object.E_z)
#         A.append(object.A_z)
#
# plt.scatter(t,B, color='blue')
# plt.scatter(t,E, color='red')
# # plt.scatter(t,A)
# plt.show()