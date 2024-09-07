#!/usr/bin/python
from PIL import Image, ImageSequence
import os
import glob

# walk trough and convert, at end delete webp file
def convert_webp_to_format(input_folder):
    for root, dirs, filenames in os.walk(input_folder):
        for filename in filenames: 
            if filename.endswith('.webp'):
                input_filename = os.path.join(root, filename)
                img = Image.open(input_filename)
                output_format = "png"
                is_animated = getattr(img, "is_animated", False)
                if(is_animated):
                    output_format = "gif"                    
                output_filename = os.path.join(root, os.path.splitext(filename)[0] + '.' + output_format)
                img.save(output_filename, format=output_format.upper(), save_all=True)
                os.remove(input_filename)
                print(f"Converted {input_filename} to {output_filename}")

convert_webp_to_format(".")
