#!/usr/bin/python2.5

import os
import sys
import codecs

from mutagen.easyid3 import EasyID3

# log = open(os.path.expanduser("~/tag_info_log"), "w")

def print_track(track):
    try:
        audio = EasyID3(track)
        print "File: %s" % track
        if "title" in audio:
            print (u"Title:\t%s" % (audio["title"][0],)).encode('utf-8')
        if "artist" in audio:
            print (u"Artist:\t%s" % (audio["artist"][0],)).encode('utf-8')
        if "album" in audio:
            print (u"Album:\t%s" % (audio["album"][0],)).encode('utf-8')
        print "\n"

    except Exception, ex:
#         log.write(ex.message)
#         log.write("\n")
        pass
        
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        track = sys.argv[1]
        print_track(track)
#     else:
#         for track in os.listdir(os.getcwd()):
#             print_track(track)


#                   "info-year=%y\\n"
#                   "info-genre=%g\\n"
#                   "info-note=%c\\n"
#                   "info-playing-time=%S\\n"))



