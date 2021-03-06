from cv2 import *
import os
from skimage import io
from skimage import data
import pymeanshift as pms
from numpy import *
import pickle
from matplotlib.pyplot import *

debug = 0
count = 0

"""
Perform clustering on colors, also do a crop
"""
def seg(img,a,b,c):
    lx, ly, ch = img.shape
    img = img[lx / 4:-lx/4,ly/10:-ly/10,:]
    l = list(pms.segment(img[:,:,0:3],a,b,c)) #1,12,30 "magic"
    l.extend(list(img.shape))
    return l
    
"""
Compress Image into a discrete measure on R^5, (r,g,b,x,y)
"""
def summary(img):
    [image,m,d,lx,ly,dim] = seg(img,1,11,40) # Using 1,11,20
    o = []
    for cluster in range(0,d):
        #imagel = color.rgb2lab(image)
        imagel = image
        (i,j) = where(m==cluster)
        o.append((float(len(i))/(lx*ly),
            uint8(imagel[i[0],j[0],0]), 
            uint8(imagel[i[0],j[0],1]), 
            uint8(imagel[i[0],j[0],2]),
            1*uint8(mean(i)),
            1*uint8(mean(j))))
            
    if debug:
        print "debug"
        subplot(2,1,1)
        io.imshow(image)
        subplot(2,1,2)
        io.imshow(img)  
        
    return o

"""
Return distance between two (compressed) images.

Usage
> im1 = data.load(thumbnaildir + '10007b.jpg')
> im2 = data.load(thumbnaildir + '10022k.jpg')
> dist(compress(im1), compress(im2))
"""
def dist(im1, im2):
    i1 = array(im1)
    i2 = array(im2)
    i1[:,4:6] = i1[:,4:6]*0.5
    i2[:,4:6] = i2[:,4:6]*0.5
    sig1 = cv.CreateMat(i1.shape[0], i1.shape[1], cv.CV_32FC1)
    sig2 = cv.CreateMat(i2.shape[0], i2.shape[1], cv.CV_32FC1)
    cv.Convert(cv.fromarray(i1), sig1)
    cv.Convert(cv.fromarray(i2), sig2)
    return cv.CalcEMD2(sig1, sig2, cv.CV_DIST_L1)

"""
Helper functions
"""

def toSummary(compimage):
    coord   = array(compimage,dtype=uint8)[:,1:]
    density = array(compimage,dtype=single)[:,0]
    return {"coord": coord, "density":density}


def fromSummary(thumb):
    coord = thumb['coord']
    density = thumb['density']
    out = []
    for i in range(len(thumb['density'])):
        out.append((density[i],) + tuple(coord[i]))
    return out
