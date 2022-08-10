#!/usr/bin/env python3
import random
import glob
import sys
import argparse
import os
from PIL import Image



def parse_args(args):
    parser = argparse.ArgumentParser(description="Enter description here")
    parser.add_argument(
        "-f","--input_files", nargs='*', default="",
        help="input data.txt, overrides input dir"
        )
    parser.add_argument(
        "-i","--input_dir",default="../full_galaxy_data",
        help="directory with data.txt"
        )
    parser.add_argument(
        "-o","--output_dir",default="../pro_image",
        help="directory for outputs"
        )
    return parser.parse_args(args)




def main():
    args = parse_args(sys.argv[1:])
    input_files = args.input_files
    if not input_files:
        input_dir  = args.input_dir
        all_images = glob.glob(os.path.join(input_dir,"*.jpg"))
        print(all_images)
    else:
        all_images = input_files
    
    for img_path in all_images:
        img = Image.open(img_path)
        width, height = img.size
        new_width = 256
        new_height = 256

        left   = (width - new_width)/2
        top    = (height - new_height)/2
        right  = (width + new_width)/2
        bottom = (height + new_height)/2

        img = img.crop((left, top, right, bottom))
        img_id = img_path.split(".")[2].split("/")[2]
        img_path = "../pro_image/" + img_id + "_proc.jpg"
        img.save(img_path)





if __name__ == '__main__':
	main()


