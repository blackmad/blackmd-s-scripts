#!/opt/local/bin/python2.4

import sys
import os
import glob
import eyeD3

def process_dir(dir):
    print "Processing %s" % dir
    files = glob.glob(os.path.join(dir, "*.mp3"))
    if len(files) == 0:
        print "no mp3 files!"
        return
    print "found %s" % files[0]
    tag = eyeD3.Tag()
    tag.link(files[0])
    if not tag.getArtist() or not tag.getAlbum():
        return
    new_dirname = "%s - %s" % (tag.getArtist(), tag.getAlbum())
    if tag.getYear():
        new_dirname += " (%s)" % tag.getYear()
    print new_dirname
    os.rename(dir, new_dirname)

for dir in sys.argv[1:]:
    process_dir(dir)

    
    
    
   
