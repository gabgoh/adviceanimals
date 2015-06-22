import pickle
import json
import gc
import os
from distance import *

thumbnaildir = 'D:\\memeproject\\thumbnails\\'

"""
Step 1
Generate Summary of Compressed Thumbnails
"""

def toSummary(compimage):
    coord   = array(compimage,dtype=int8)[:,1:]
    density = array(compimage,dtype=single)[:,0]
    return {"coord": coord, "density":density}


def fromSummary(thumb):
    coord = thumb['coord']
    density = thumb['density']
    out = []
    for i in range(len(thumb['density'])):
        out.append((density[i],) + tuple(coord[i]))
    return out

compressedThumbs = []
fileNames = []
for filename in os.listdir(thumbnaildir):
    try:
        img = data.load(thumbnaildir + filename)
        compressedThumbs.append(compress(img))
        fileNames.append(filename)
        count = count + 1
        if count > 1000000000:
            # Use if you wish to limit the thumbnails processed
            break
        if count % 1000 == 0:
            print "At " + str(count)
    except:
        pass

thumbs = {}
for i in range(0,len(compressedThumbs)):
    thumbs[fileNames[i]] = toSummary(compressedThumbs[i])

"""
Step 2
Append MetaData to Summary
"""

f = open(r'D:\memeproject\data\adviceAnimalsSubmissions','r')
i = 0;
for line in f:
    i = i + 1;
    data = json.loads(line.strip())
    if (data['id']+".jpg") in thumbs:
        mId = data['id'] + ".jpg"
        thumbs[mId]['title'] = data['title']
        thumbs[mId]['url'] = data['url']
    if i % 10000==0:
        print "Progress at" , i 
        gc.collect()

fp = open(r'D:\memeproject\ThumbsnailSummaryTitles','w')
pickle.dump(thumbs, fp)
fp.close()