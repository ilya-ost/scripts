#! /usr/bin/env python2.5

import sys
import os
import re

def apecue2ogg(workdir):
    print workdir
    map(apecue2ogg,
        (os.path.join(workdir, d)
         for d in os.listdir(workdir)
         if os.path.isdir(os.path.join(workdir, d))))

    p = re.compile(r'\.ape$', re.IGNORECASE)
    apefiles = map (lambda f: os.path.join(workdir,f),
                    filter(lambda f: p.search(f),
                           os.listdir(workdir)))
    for ape in apefiles:
        cue = p.sub(".cue", ape)
        if os.path.exists(cue):
            os.system("cuebreakpoints '%s' | shnsplit -a '%s' -o  '%s'" % (cue, p.sub("_", ape), ape))
            os.system("cuetag '%s' %s*.flac" % (cue, p.sub("", ape).replace(" ","\ ")))
#             os.unlink(ape)
#             os.unlink(cue)

            

if __name__ == "__main__":
    apecue2ogg(os.path.expanduser(sys.argv[1]))

