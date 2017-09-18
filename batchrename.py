#!/usr/bin/python
# -*- coding:utf-8 -*-
#14th Aug  2017 Emacs_yang

import os

path = "/home/heyang/mywork/mydoc/"
flag = 0

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file)) == True:
        filename,suffix = os.path.splitext(os.path.join(path,file))
        if (suffix.lower() == ".doc") or (suffix.lower() == ".docx"):
            newname = str(flag)+suffix
            #print (os.path.isfile(os.path.join(path,str(flag)+".doc")) == True  or os.path.isfile(os.path.join(path,str(flag)+".docx")) == True)
            if (os.path.isfile(os.path.join(path,str(flag)+".doc")) == True  or os.path.isfile(os.path.join(path,str(flag)+".docx")) == True):
                print newname,"file exist, continue"
            else:
                os.rename(os.path.join(path,file),os.path.join(path,newname))
                print file,"ok"

            flag += 1

print "total file count %d" % flag
