#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
convert2dzi.py

Converts images to Deep Zoom format using the deepzoom library.
"""

import sys
try:
    import deepzoom
except ImportError:
    deepzoom = None
    print("Warning: deepzoom module not found. Please install it.")

def main(input_path, output_path):
    """Main function to convert image to Deep Zoom format."""
    if deepzoom is None:
        print("DeepZoom library is required.")
        return
    creator = deepzoom.ImageCreator(tile_size=128, tile_overlap=2, tile_format="png",
                                    image_quality=0.8, resize_filter="bicubic")
    creator.create(input_path, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert2dzi.py <input_image> <output_path>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
