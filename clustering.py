from skimage import io, color, data, transform
from distance import *
import numpy as np
import json
from numpy import *
from distance import *
from skimage import data, transform

print "Templates Loaded"

thumbdir = 'D:\\memeproject\\thumbnails\\'

def l(t,s):
    return concatenate((array([t[s]['density']]).transpose(), t[s]['coord']), axis=1)

imageFileName = r'D:\memeproject\templates\Awkward_Penguin.jpg'

def compareAll(imageFileName, thumbs):
    im = data.load(imageFileName)
    template_summary = comp(uint8(transform.resize(im, [70,70,3])*255))
    
    count = 0
    comparisons = []
    for thumb in thumbs:
        compressed_thumb = fromSummary(thumb)
        count = count + 1
        comparisons.append((d(template_summary, compressed_thumb),i))
        
        if count > 1000000:
            break
        if count % 1000==0:
            print "At " + str(count)
    
    s = sorted(comparisons)
    
    cutoff = argmax(gradient([ii[0] for ii in s if s > 50])[100:40000])
    cutoff = cutoff + 100
    return s, cutoff

def previewThumbs(thumbList, dims):
    thumbdir = 'D:\\memeproject\\thumbnails\\'
    pview = uint8(np.zeros((70*dims[0],70*dims[1],3)));
    for i in range(0,dims[0]*dims[1]):
        thumb = data.load(thumbdir + thumbList(i))[:,:,0:3]
        if thumb.shape[1] != 70:
            blankRight = uint8(zeros((thumb.shape[0], 70 - shape(thumb)[1],3)))
            thumb = concatenate((thumb, blankRight),axis=1)
        blankBottom = uint8(zeros((70 - shape(thumb)[0],70,3)))
        pthumb = concatenate((thumb, blankBottom))
        x = i/dims[1]
        y = i - dims[1]*(i/dims[1])
        pview[70*x:70*(x+1), 70*y:70*(y+1)] = pthumb
    imshow(pview)


fp = open('D:\\memeproject\\templateData','r')
thumbs = pickle.load(fp)
fp.close()

compareAll(imageFileName, thumbs)

#titems = t.items()
#getI = lambda i: titems[i][0]
# s,cutoff = compareAll(imageFileName, t)