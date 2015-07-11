from distance import *
from skimage import data, transform

thumbdir = 'D:\\memeproject\\thumbnails\\'

"""
precompute and sort thumbnails
"""

def compareAll(imageFileName, thumbs):
    im = data.load(imageFileName)
    template_summary = summary(uint8(transform.resize(im, [70,70,3])*255))
    
    count = 0
    comparisons = []
    for (title, thumb) in thumbs.items():
        compressed_thumb = fromSummary(thumb)
        count = count + 1
        comparisons.append((dist(template_summary, compressed_thumb),title))
        
        if count > 1000000:
            break
        if count % 1000==0:
            print "\rAt " + str(count),
    
    s = sorted(comparisons)
    
    cutoff = argmax(gradient([ii[0] for ii in s if s > 50])[100:40000])
    cutoff = cutoff + 100
    return s, cutoff

if __name__ == "__main__":

    fp = open('D:\\memeproject\\ThumbsnailSummaryTitlesAll','r')
    thumbs = pickle.load(fp)
    fp.close()
    print "Thumbnail Summaries Loaded"

    for name in os.listdir(r'D:\\memeproject\\templates\\'):

        imageFileName = 'D:\\memeproject\\templates\\' + name
        (s,cutoff) = compareAll(imageFileName, thumbs)

        fp = open('D:\\memeproject\\thumbssort\\' + name, 'w')
        pickle.dump((s, cutoff), fp)
        print "Wrote to", ('D:\\memeproject\\thumbssort\\' + name)
        fp.close()
