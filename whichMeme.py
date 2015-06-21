from numpy import *
import distance as dist
from skimage import data

def ll(t):
    return concatenate((array([t['density']]).transpose(), t['coord']), axis=1)

def whichMeme(im, templates):
    di = []
    for template in templates:
        di.append(dist.d(ll(im), ll(template)))
    di = array(di)
    di = exp(-di/10)/sum(exp(-di/10))
    p = []
    for i in range(0,len(templates)):
        p.append({"p":di[i],"Title":templates[i]["Title"]})
    return sorted(p, key=lambda x: x['p'])
    #return p

"""
ion()
import time

for k in range(0,25):
    item = t.items()[k+50]
    y = whichMeme(item[1], templates)
    print y[-1]
    im = data.load('E:\\memeproject\\thumbnails\\' + item[0])
    subplot(5,5,k)  
    title(str(k+50) + y[-1]["Title"] + " " + str(round(y[-1]["p"],2)) )
    axis('off')
    imshow(im)
"""

