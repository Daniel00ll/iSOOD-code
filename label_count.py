import os
from PIL import Image
import pandas as pd

images_dir = 'Image folder'
annotations_dir = 'Label folder'

small_threshold = 32 * 32
large_threshold = 96 * 96

small_count = 0
medium_count = 0
large_count = 0
label_sizes = []

for filename in os.listdir(annotations_dir):
    annotation_path = os.path.join(annotations_dir, filename)
    image_base_name = os.path.splitext(filename)[0]
    image_path = os.path.join(images_dir, image_base_name + '.jpg')
    
    with Image.open(image_path) as img:
        image_width, image_height = img.size

    with open(annotation_path, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split()
            if len(parts) >= 5:
                width_ratio, height_ratio = map(float, parts[3:5])
                bbox_area_pixels = (width_ratio * image_width) * (height_ratio * image_height)
                label_sizes.append((width_ratio * image_width, height_ratio * image_height))
                if bbox_area_pixels < small_threshold:
                    small_count += 1
                elif bbox_area_pixels > large_threshold:
                    large_count += 1
                else:
                    medium_count += 1

print(f"Small objects: {small_count}")
print(f"Medium objects: {medium_count}")
print(f"Large objects: {large_count}")
