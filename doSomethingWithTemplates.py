import os
from skimage import data, transform
from numpy import *
from distance import *
import pickle

templateDir = 'D:\\memeproject\\templates\\'

i= 0;
templateData = []
for templateFile in os.listdir(r'D:\memeproject\templates'):
    
    memeName = templateFile.replace("_"," ")[:-4]
    im = data.load(templateDir + templateFile)
    im = array(transform.resize(im, [70,70])*255,dtype=uint8);
    
    out = {'Title': memeName}
    out.update(toSummary(comp(im)))
    templateData.append(out)
    
    i = i + 1
    print "Processing ",  memeName
    if i > 100000:
        break
        
fp = open('D:\\memeproject\\templateData','w')
pickle.dump(templateData, fp)
fp.close()