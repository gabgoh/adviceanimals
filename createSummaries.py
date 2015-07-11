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

compressedThumbs = []
fileNames = []
for filename in os.listdir(thumbnaildir):
    try:
        img = data.load(thumbnaildir + filename)
        compressedThumbs.append(summary(img))
        fileNames.append(filename)
        count = count + 1
        if count > 1e100:
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

f = open(r'D:\memeproject\data\AdviceAnimalsSubmissions','r')
i = 0;
for line in f:
    i = i + 1;
    data = json.loads(line.strip())
    if (data['id']+".jpg") in thumbs:
        mId = data['id'] + ".jpg"
        thumbs[mId]['title'] = data['title']
        thumbs[mId]['url'] = data['url']
        thumbs[mId]['ups'] = data['ups']
        thumbs[mId]['downs'] = data['downs']
        thumbs[mId]['created'] = data['created_utc']

    if i % 10000 == 0:
        print "Progress at" , i
        gc.collect()

fp = open(r'D:\memeproject\ThumbsnailSummaryTitlesAll','w')
pickle.dump(thumbs, fp)
fp.close()