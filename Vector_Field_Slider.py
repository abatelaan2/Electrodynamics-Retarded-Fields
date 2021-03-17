import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.widgets import Slider, Button, RadioButtons


fig = plt.figure()
x, y, z = np.meshgrid(np.arange(-1, 1, 0.3),
                      np.arange(-1, 1, 0.3),
                      np.arange(-1, 1, 0.8))

positions = np.vstack([x.ravel(), y.ravel(), z.ravel()])

t0=0

ax2 = fig.add_subplot(111, projection='3d')
E = np.log(1+np.sqrt((t0**2)-((x ** 2) + (y ** 2)))/t0)-np.log(1-np.sqrt((t0**2)-((x ** 2) + (y ** 2)))/t0)
B = np.sqrt((t0**2)-((x ** 2) + (y ** 2)))/((x ** 2) + (y ** 2))
u = B*(-y / ((x ** 2) + (y ** 2)))
v = B*(x / ((x ** 2) + (y ** 2)))
w = 0

ax2.title.set_text("Infinite Wire: I(t)=$I_0$t")
ax2.quiver(x, y, z, u, v, w, length=0.1, color = 'blue')
ax2.quiver(x, y, z, 0, 0, E, length=0.1, color='red')
line = art3d.Line3D([0,0], [0,0], [-1,1], color='black')
ax2.add_line(line)
ax2.set_xlim(-1,1)
ax2.set_ylim(-1,1)
ax2.set_zlim(-1,1)
axhauteur = plt.axes([0.2, 0.1, 0.65, 0.03])
shauteur = Slider(axhauteur, 'Time', 0, 5, valinit=t0)

def update(val):
    t = shauteur.val
    ax2.clear()
    E = np.log(1+np.sqrt((t**2)-((x ** 2) + (y ** 2)))/t)-np.log(1-np.sqrt((t**2)-((x ** 2) + (y ** 2)))/t)
    B = np.sqrt((t**2)-((x ** 2) + (y ** 2)))/((x ** 2) + (y ** 2))
    u = B*(-y / ((x ** 2) + (y ** 2)))
    v = B*(x / ((x ** 2) + (y ** 2)))
    w = 0
    ax2.title.set_text("Infinite Wire: I(t)=$I_0$t")
    ax2.quiver(x, y, z, u, v, w, length=0.005, color='blue')
    ax2.quiver(x, y, z, 0, 0, E, length=0.1, color='red')
    line = art3d.Line3D([0, 0], [0, 0], [-1, 1], color='black')
    ax2.add_line(line)
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(-1, 1)
    fig.canvas.draw_idle()
shauteur.on_changed(update)

plt.show()