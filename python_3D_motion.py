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






