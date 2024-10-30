import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Time array
t0=0
t_end=10
dt=0.02
t=np.arange(t0,t_end+dt,dt)

# Create array for x & y dimensions
r=3
f=1
x=r*np.cos(2*np.pi*f*t)
y=r*np.sin(2*np.pi*f*t)

# Create array for z dimension
z=t

############################## ANIMATION ##############################
frame_amount=len(t)

def update_plot(num):

    return

# Set up the figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(3,4)

# 3d motion
ax0=fig.add_subplot(gs[:,0:3],projection='3d',facecolor=(0.9,0.9,0.9))
plane_trajectory,=ax0.plot([],[],[],'r',linewidth=4,label='Flight trajectory')
ax0.set_xlim(min(x),max(x))
ax0.set_ylim(min(y),max(y))
ax0.set_zlim(min(z),max(z))

ax0.set_xlabel('position_x [m]',fontsize=12)
ax0.set_ylabel('position_y [m]',fontsize=12)
ax0.set_xlabel('position_z [m]',fontsize=12)
plt.grid(True)
plt.legend(loc='upper left',fontsize='large')





plt.show()

