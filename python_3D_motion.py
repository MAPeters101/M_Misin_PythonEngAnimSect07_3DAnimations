import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

type=1

# Time array
t0=0
t_end=10
dt=0.02
t=np.arange(t0,t_end+dt,dt)

# Create array for x & y dimensions
r=3
f=1
if type==1:
    x=r*np.cos(2*np.pi*f*t)
    y=r*np.sin(2*np.pi*f*t)
    # Create array for z dimension
    z = t
elif type==2:
    x=t*np.cos(2*np.pi*f*t)
    y=t*np.sin(2*np.pi*f*t)
    # Create array for z dimension
    z = t
elif type==3:
    x=t**2*np.cos(2*np.pi*f*t)
    y=t**2*np.sin(2*np.pi*f*t)
    # Create array for z dimension
    z = t
elif type==4:
    x=r*np.cos(2*np.pi*(f*0.2*t)*t)
    y=r*np.sin(2*np.pi*(f*0.2*t)*t)
    # Create array for z dimension
    z=t
elif type==5:
    x=r*np.cos(2*np.pi*(f)*t)
    y=r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=t**2
elif type==6:
    x=t+r*np.cos(2*np.pi*(f)*t)
    y=r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=t
elif type==7:
    x=r*np.cos(2*np.pi*(f)*t)
    y=t+r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=t
elif type==8:
    x=t+r*np.cos(2*np.pi*(f)*t)
    y=t+r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=t
elif type==9:
    x=10-t
    y=10-t
    # Create array for z dimension
    z=t
elif type==10:
    x=t+r*np.cos(2*np.pi*(f)*t)
    y=t+r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=2.5+np.sin(2*np.pi*(0.2)*t)
elif type==11:
    x=r*np.cos(2*np.pi*(f)*t)
    y=r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=2.5+np.sin(2*np.pi*(0.2)*t)
elif type==12:
    x=r*np.cos(2*np.pi*(f)*t)
    y=r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=2.5+np.sin(2*np.pi*(2)*t)
elif type==13:
    x=r*np.cos(2*np.pi*(f)*t)
    y=r*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=2.5+np.sin(2*np.pi*(3)*t)
elif type==14:
    x=r*np.cos(2*np.pi*(f)*t)
    y=t
    # Create array for z dimension
    z=t
elif type==15:
    x=r*np.cos(2*np.pi*(f)*t)
    y=(r*2)*np.sin(2*np.pi*(f)*t)
    # Create array for z dimension
    z=t


############################## ANIMATION ##############################
frame_amount=len(t)

def update_plot(num):
    # Trajectory
    #plane_trajectory.set_data(x[0:num],y[0:num])
    plane_trajectory.set_xdata(x[0:num])
    plane_trajectory.set_ydata(y[0:num])
    plane_trajectory.set_3d_properties(z[0:num])

    pos_x.set_data(t[0:num],x[0:num])
    pos_y.set_data(t[0:num],y[0:num])
    pos_z.set_data(t[0:num],z[0:num])

    return plane_trajectory,pos_x,pos_y,pos_z

# Set up the figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(3,4)

# 3d motion
ax0=fig.add_subplot(gs[:,0:3],projection='3d',facecolor=(0.9,0.9,0.9))
plane_trajectory,=ax0.plot([],[],[],'r',linewidth=4,label='Flight trajectory')
ax0.set_xlim(min(x),max(x))
ax0.set_ylim(min(y),max(y))
ax0.set_zlim(min(z),max(z))
# ax0.set_xticks([0])
# ax0.set_yticks([0])
# ax0.set_zticks([5])
ax0.set_xlabel('position_x [m]',fontsize=12)
ax0.set_ylabel('position_y [m]',fontsize=12)
ax0.set_zlabel('position_z [m]',fontsize=12)
plt.grid(True)
plt.legend(loc='upper left',fontsize='large')

ax1=fig.add_subplot(gs[0,3],facecolor=(0.9,0.9,0.9))
pos_x,=ax1.plot([],[],'b',linewidth=2,label='x = '+str(r)+'cos(2pi'+str(f)+'t)')
plt.xlim(t0,t_end)
plt.ylim(min(x),max(x))
plt.ylabel('position_x [m]',fontsize=12)
plt.grid(True)
plt.legend(loc='upper left',fontsize='small')

ax2=fig.add_subplot(gs[1,3],facecolor=(0.9,0.9,0.9))
pos_y,=ax2.plot([],[],'b',linewidth=2,label='y = '+str(r)+'sin(2pi'+str(f)+'t)')
plt.xlim(t0,t_end)
plt.ylim(min(y),max(y))
plt.ylabel('position_y [m]',fontsize=12)
plt.grid(True)
plt.legend(loc='upper left',fontsize='small')

ax3=fig.add_subplot(gs[2,3],facecolor=(0.9,0.9,0.9))
pos_z,=ax3.plot([],[],'b',linewidth=2,label='z = t')
plt.xlim(t0,t_end)
plt.ylim(min(z),max(z))
plt.xlabel('time [s]',fontsize=12)
plt.ylabel('position_z [m]',fontsize=12)
plt.grid(True)
plt.legend(loc='lower right',fontsize='small')



plane_ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=False,blit=True)
plt.show()

