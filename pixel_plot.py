from PIL import Image
import os
import matplotlib.pyplot as plt

dataset_path = 'Your folder'

image_sizes = []

for img_file in os.listdir(dataset_path):
    img_path = os.path.join(dataset_path, img_file)
    with Image.open(img_path) as img:
        width, height = img.size
        if width * height < 1280*1280:
            image_sizes.append((width, height))
        #image_sizes.append((width, height))

print("Collected sizes of all images.")

pixels = [width * height for width, height in image_sizes]

plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(pixels, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.gca().set_facecolor('#D3D3D3')
plt.ylim([0, 250])
plt.xlim([0, 1600000])

#target_pixel = 1280 * 1280
#plt.axvline(target_pixel, color='r', linestyle='--', linewidth=2)
#plt.axvspan(0, target_pixel, color='#D3D3D3', alpha=0.5)
#left_side = sum(p <= target_pixel for p in pixels) / len(pixels) * 100

#right_side = sum(p > target_pixel for p in pixels) / len(pixels) * 100
#print(left_side,right_side)

#plt.title('Image Pixel Distribution Histogram', fontsize=15, fontname='Times New Roman')
#plt.xlabel('Pixels', fontsize=15, fontname='Times New Roman')  
#plt.ylabel('Frequency', fontsize=15, fontname='Times New Roman')  

plt.xticks(fontsize=15, fontname='Times New Roman') 
plt.yticks(fontsize=15, fontname='Times New Roman') 

plt.gca().xaxis.get_offset_text().set_fontsize(15)
plt.gca().xaxis.get_offset_text().set_fontname('Times New Roman') 

plt.show()

