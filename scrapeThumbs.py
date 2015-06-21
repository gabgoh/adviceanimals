import json
import numpy as np
import matplotlib
import urllib2
import time
import os
import socket
import sys
import urllib2

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)

f = open(r'E:\memeproject\data\adviceAnimalsSubmissions', 'r')
f2 = open('out.txt', 'w')
i = 0
max = float('inf') #4000
count = 0

#numbins = 500
#mybins = np.linspace(-100, 3000, numbins)
#myhist = np.zeros(numbins-1, dtype='int32')
nothumb = 0

thumbdir = 'E:\\memeproject\\thumbnails\\'
fulldir = 'E:\\memeproject\\full\\'

alreadyFetchedThumbs = []
for filename in os.listdir(thumbdir):
    alreadyFetchedThumbs.append(filename[:-4])

alreadyFetchedFulls = []
for filename in os.listdir(fulldir):
    alreadyFetchedFulls.append(filename[:-4])


headers = { 'User-Agent' : "Advice Animal Scraper, by Marcos and Gabriel. " + \
"Should this bot should overstep the bounds of courteous scraping, please " + \
"contact reddit_user:gabgoh email:gabgohjh@gmail.com. Thanks!"}

def dlfile(url, writeto):
    # Open the url
    try:
        print url
        req = urllib2.Request(url, None, headers)
        f = urllib2.urlopen(req)
        print "downloading " + url
        # Open our local file for writing
        with open(writeto, "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except urllib2.HTTPError, e:
        print "HTTP Error:", e.code, url
    except urllib2.URLError, e:
        print "URL Error:", e.reason, url

for line in f:
    
    data = json.loads(line.strip())
  
    #htemp, jnk = np.histogram(int(data['ups']) - int(data['downs']), mybins)
    #myhist += htemp

  
    #if int(data['ups']) - int(data['downs']) >= 2000:
    #    count = count + 1 

    if int(data['ups']) - int(data['downs']) >= 30:
        
        # Fetch Thumbnails
        if data['id'] not in alreadyFetchedThumbs:
            if data['thumbnail'] != "default" and data['thumbnail'] != "self" and data['thumbnail'] != "nsfw" :
                try:
                    dlfile(data['thumbnail'], thumbdir + data['id'] + ".jpg")
                    print "Retrieved thumbnail meme for ", data['id'], " score: ", int(data['ups']) - int(data['downs']), i
                    print ""
                    time.sleep(0.3)                    
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    
        """    
        # Fetch Full Image        
        if data['id'] not in alreadyFetchedFulls:
            if "imgur" in data['url'] and "jpg" in data['url']:
                try:
                    dlfile(data['url'], fulldir + data['id'] + ".jpg")
                    print "Retrieved full meme for ", data['id'], " score: ", int(data['ups']) - int(data['downs'])
                    print ""
                    time.sleep(1)                    
                except:
                    print "Unexpected error:", sys.exc_info()[0]
        """
        if i >= max:
            break
    
    i += 1
    if i % 10000==0:
        print "Progress at" , i
    
    
f.close()
f2.close()
