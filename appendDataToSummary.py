import pickle
import json
import gc

fp = open('E:\\memeproject\\thumbnailsummary_all','r')
t = pickle.load(fp)
fp.close()

print "Thumbnails Loaded"

f = open(r'E:\memeproject\data\adviceAnimalsSubmissions','r')
i = 0;
for line in f:
    i = i + 1;
    data = json.loads(line.strip())
    if data['id'] in t:
        mId = data['id']
        t[mId]['title'] = data['title']
        t[mId]['url'] = data['url']
    if i % 10000==0:
        print "Progress at" , i 
        gc.collect()

fp = open(r'E:\memeproject\thumbsnailSummaryTitles','w')
pickle.dump(t, fp)
fp.close()