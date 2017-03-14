#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import deepzoom

path = '/var/www/http/DZI_Storage'
# Specify your source image
#SOURCE = "helloworld.jpg"

def main (arg1, arg2):
    # Create Deep Zoom Image creator with weird parameters
    creator = deepzoom.ImageCreator(tile_size=128, tile_overlap=2, tile_format="png",
                                image_quality=0.8, resize_filter="bicubic")

    # Create Deep Zoom image pyramid from source

    creator.create(arg1, arg2)

if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
    #main(sys.argv[1],sys.argv[2]);
