from PIL import Image, ImageDraw
import os

folder_path = 'Your folder'

files = os.listdir(folder_path)
image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]
anno_files = [f for f in files if f.endswith('.txt')]

def read_yolo_annotation(anno_path):
    boxes = []
    with open(anno_path, 'r') as file:
        for line in file.readlines():
            parts = line.split()
            if len(parts) >= 5:
                _, cx, cy, w, h = map(float, parts[:5])
                boxes.append((cx, cy, w, h))
    return boxes

def convert_to_pixels(cx, cy, w, h, img_width, img_height):
    x = int((cx - w / 2) * img_width)
    y = int((cy - h / 2) * img_height)
    width = int(w * img_width)
    height = int(h * img_height)
    return x, y, width, height

def visualize_annotations(image_path, anno_path):
    image = Image.open(image_path)
    img_width, img_height = image.size

    boxes = read_yolo_annotation(anno_path)

    draw = ImageDraw.Draw(image)

    for box in boxes:
        cx, cy, w, h = box
        x, y, width, height = convert_to_pixels(cx, cy, w, h, img_width, img_height)
        draw.rectangle([(x, y), (x + width, y + height)], outline="red", width=5)

    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = os.path.join(folder_path, f"{base_name}_visualized.jpg")

    image.save(output_path)

for image_file in image_files:
    base_name = os.path.splitext(image_file)[0]
    anno_file = f"{base_name}.txt"
    if anno_file in anno_files:
        visualize_annotations(os.path.join(folder_path, image_file), os.path.join(folder_path, anno_file))