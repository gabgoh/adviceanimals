from skimage.draw import *
from numpy import *
from skimage import color
from matplotlib.pyplot import *
import itertools
from numpy.linalg import norm
import pickle 

"""
A visualization for the histogram-point representation of the image
"""
figure()

fp = open('D:\\memeproject\\templateData','r')
templates = pickle.load(fp)
fp.close()

data = templates[12]
print data['Title']

img = zeros((35, 60,3),dtype=uint8)

def ll(t):
    return concatenate((array([t['density']]).transpose(), t['coord']), axis=1)

def findNearest(x, m):
    return argmin([norm(x-p) for p in m[:,4:6]])

m = ll(data)
for i,j in itertools.product(range(0,img.shape[0]),range(0,img.shape[1])):
    nearest = findNearest(array([i,j]), m)
    img[i,j,0] = m[nearest][1]
    img[i,j,1] = m[nearest][2]
    img[i,j,2] = m[nearest][3]
    
#im = color.lab2rgb(img)*255
figure()
imshow(img)
show()



