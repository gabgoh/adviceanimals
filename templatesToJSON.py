__author__ = 'Gabriel'

import os
import json

# Generate template list for thumbBar (name, karma)

data = []
for templateFile in os.listdir(r'D:\memeproject\code\html\memes'):
    fp = open(r'D:\memeproject\code\html\memes\\' + templateFile, 'r')
    memes = json.load(fp)
    fp.close()
    totalKarma = 0
    for meme in memes:
        totalKarma = totalKarma + meme["pt"]
    data.append({"name": templateFile[0:-3].replace("_"," "),
                 "filename": templateFile,
                 "karma": totalKarma})
    print "Processed ", templateFile

data = sorted(data, key = lambda x: x["name"])
#data.reverse()

jsonData = "templateData = " + json.dumps(data)

fp = open(r'D:\memeproject\code\html\templateInfo.js', 'w')
fp.write(jsonData)
fp.close()