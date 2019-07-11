#python3
import math
import re
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import time

zmat = np.load("quaternion_25_1pt2.npy") #load file from prior step
xsize = zmat[:,0,0,0].size #60 ish (currently always square)

# Visualization of 4D tensors is a pain thanks to our monkey brain
# code below is a half-measure towards that goal, at best

def pltfunction(filename):
    fig, ax = plt.subplots()
    ax.axis('off')
    plt.imshow(slicemat, interpolation='nearest', cmap=cm.inferno)
    plt.savefig(filename,bbox_inches='tight', pad_inches=0)
    plt.close()
    
for a in range(0,xsize):
    j = 0
    b = slice(None) #equivalent to ":"
    c = slice(None) #equivalent to ":"
    d = int(xsize/2)
    slicemat = zmat[a,b,c,d]
    pltfunction("itr"+"-"+str(j)+"-"+str(a))
    
for b in range(0,xsize):
    j = 1
    a = slice(None)
    c = slice(None)
    d = int(xsize/2)    
    slicemat = zmat[a,b,c,d]
    pltfunction("itr"+"-"+str(j)+"-"+str(b))
    
for c in range(0,xsize):
    j = 2
    a = slice(None)
    b = slice(None)
    d = int(xsize/2)    
    slicemat = zmat[a,b,c,d]
    pltfunction("itr"+"-"+str(j)+"-"+str(c))

for d in range(0,xsize):
    j = 3
    a = slice(None)
    b = slice(None)
    c = int(xsize/2)    
    slicemat = zmat[a,b,c,d]
    pltfunction("itr"+"-"+str(j)+"-"+str(d))