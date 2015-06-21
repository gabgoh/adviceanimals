import json
from numpy import *
from distance import *
from skimage import data
import pickle

fp = open('E:\\memeproject\\thumbnailSummaryTitlesRGB','r')
t = pickle.load(fp)
fp.close()

fp = open('E:\\memeproject\\templateData','r')
templates = pickle.load(fp)
fp.close()
