import os
from skimage import data, transform
from numpy import *
from distance import *
import pickle
import json
import random

templateDir = 'D:\\memeproject\\templates\\'

job = 2

# Generate Template Summaries
i= 0;
templateData = []
for templateFile in os.listdir(r'D:\memeproject\templates'):

    memeName = templateFile.replace("_"," ")[:-4]
    im = data.load(templateDir + templateFile)
    im = array(transform.resize(im, [70,70])*255,dtype=uint8);

    out = {'Title': memeName}
    out.update(toSummary(summary(im)))
    templateData.append(out)

fp = open('D:\\memeproject\\templateData','w')
pickle.dump(templateData, fp)
fp.close()