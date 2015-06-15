import os
from caption_list import captions

mypath = "./DFXP/"

for filename in os.listdir(mypath):
    if filename.endswith("xml"):
        for k, v in captions.iteritems():
            if k in filename:
                #print filename, k, v
                os.rename(mypath+filename, mypath+v+".DFXP.xml")



