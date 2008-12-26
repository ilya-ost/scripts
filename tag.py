#! /usr/bin/env python2.5
# -*- coding: utf-8 -*- 


import os
from mutagen.easyid3 import EasyID3

artist = u"Вежливый Отказ"
album = u"Герань"

for filename in os.listdir(os.getcwd()):
    try:
#         title = unicode(filename.split(" - ")[-1].replace('.mp3','').strip(), 'utf-8')
        title = unicode(filename[3:-26], 'utf-8')
        print title
        audio = EasyID3(filename)
        audio["title"] = title
        audio["album"] = album
        audio["artist"] = artist
        audio.save()
    except Exception,ex:
        print ex
