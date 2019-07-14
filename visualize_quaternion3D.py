#python3
import math
import re
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import time

zmat = np.load("quaternion_75_1pt2.npy") #load file from prior step
xsize = zmat[:,0,0,0].size #60 ish (currently always square)

# Visualization of 4D tensors is a pain thanks to our monkey brain
# code below is a half-measure towards that goal, at best
    
def ThreeDplt(bmatp, filename):
    fig = plt.figure()
    colors = np.empty(bmatp.shape, dtype=object)
    colors[bmatp] = 'red'
    ax = fig.gca(projection='3d')
    ax.voxels(bmatp, facecolors=colors, shade=True)
    #plt.show()
    plt.savefig(filename,bbox_inches='tight', pad_inches=0)
    plt.close()

#q px
#w py
#e pz
#r pa
bmat = np.zeros((xsize,xsize,xsize),dtype=np.bool)

for r in range(0,xsize):
    th = 18 #threshold
    tmat = zmat[:,:,:,r]
    tmat[tmat <= th] = False
    tmat[tmat > th] = True
    bmat[:,:,:] = tmat
    print("th done")

    bmatp = bmat
    print(bmatp.shape)
    filename = 'test-th'+ str(th) + '-' + str(r) + '.png'
    t1 = time.time()
    ThreeDplt(bmatp, filename)
    t0 = time.time()

    print(t0-t1)