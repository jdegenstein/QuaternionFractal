#python3

#### NOTE: this is an unworking experimental multi-threaded version of the other single-threaded version
#### do not run because the mandelspace function does not properly concatenate
#### numpy arrays between the multiple threads
#### the actual multi-threading DOES work, but the data needs to be shared somehow between threads
import math
#import cmath #no complex math, so not needed
import re
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import time
from multiprocessing import Pool

scale = 15

def mandelpoint(px,py,pz,pa):
    #note that with Quaternions z no longer the same
    #z = complex(0.0,0.0) #mandelbrot
    x0 = px/scale
    y0 = py/scale
    z0 = pz/scale
    a0 = pa/scale
    x = 0
    y = 0
    z = 0
    a = 0
    #c = complex(px/scale,py/scale) #mandelbrot 
    #c = complex(0.5,0.2)
    
    max_iter = 20
    max_iter_clamp_max = 3
    max_iter_clamp = False#True#False
    iteration = 0
    
    while (iteration < max_iter and pow(x,4) < 10): # + y*y + z*z + a*a
        xtemp = x*x - y*y - z*z - a*a + x0
        y = 2*x*y + y0
        z = 2*x*z + z0
        a = 2*x*a + a0
        x = xtemp
        iteration += 1
    
    if iteration <= max_iter_clamp_max and max_iter_clamp:
        iteration = 0
    else:
        iteration = iteration
    return iteration

varw = 1.2
   
xarr = range(int(-varw*scale),int(varw*scale))
yarr = range(int(-varw*scale),int(varw*scale))
zarr = range(int(-varw*scale),int(varw*scale))
aarr = range(int(-varw*scale),int(varw*scale))

zmat = np.zeros((len(xarr),len(yarr),len(zarr),len(aarr)),dtype=np.int8)  


#to avoid confusion, using q w e r -- as zmat indices
#zmat[q,w,e,r]
# q px (idx/rangevalue)
# w py
# e pz
# r pa
def mandelrow(w,e,r,py,pz,pa): #batch a single 1D x-row
    for q,px in enumerate(xarr):
        zmat[q,w,e,r] = mandelpoint(px,py,pz,pa)

def mandelplane(e,r,pz,pa): #batch a single 2D xy-plane
    for w,py in enumerate(yarr):
        mandelrow(w,e,r,py,pz,pa)

def mandelspace(rpa): #batch a single xyz-3D space
    r = rpa[0]
    pa = rpa[1]
    for e,pz in enumerate(zarr):
        mandelplane(e,r,pz,pa)
    #return zmat

#not used for MULTI THREAD VERSION
def mandelquaternion(): #whole 4D result
    for r,pa in enumerate(aarr):
        mandelspace(r,pa)

############# Actually do stuff
if __name__ == '__main__':
    t0 = time.time()#benchmark
    #mandelquaternion() #actually run it

    
    pool = Pool(4)
    pool.map(mandelspace, [(r, pa) for r, pa in enumerate(aarr)])
    pool.close()
    pool.join()
    
    t1 = time.time()#benchmark
    print(t1-t0)#benchmark    
    np.save('quaternion_30_1pt2.npy',zmat)
