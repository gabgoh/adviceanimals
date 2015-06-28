__author__ = 'Gabriel'

# Generate template list for thumbBar (name, karma)

data = []
for templateFile in os.listdir(r'D:\memeproject\templates'):
    data.append({"name": templateFile[0:-4].replace("_"," "),
                 "filename": templateFile[0:-4] + ".js",
                 "karma": })

fp = open(r'D:\memeproject\code\html\templateInfo.js', 'w')
json.dump(data, fp)
fp.close()