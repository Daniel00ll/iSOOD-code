import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

annotations_folder = 'Your folder' 

fig, ax = plt.subplots(figsize=(10, 8))
num = 1
ax.set_xlim(0, num)
ax.set_ylim(0, num)

for annotation_file in os.listdir(annotations_folder):
    file_path = os.path.join(annotations_folder, annotation_file)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            class_id, x_center, y_center, width, height = map(float, parts[0:])
            
            x = 0.5 - width / 2
            y = 0.5 - height / 2
            
            rect = patches.Rectangle((x*num, y*num), width*num, height*num, linewidth=0.2, edgecolor='lightcoral', facecolor='none', alpha=0.5)

            ax.add_patch(rect)

ax.tick_params(axis='x')
ax.tick_params(axis='y')
ax.set_aspect('equal', adjustable='box')
plt.title('Distribution of Annotation Box Sizes', fontname='Times New Roman',fontsize=15)
plt.xticks(fontsize=15, fontname='Times New Roman')
plt.yticks(fontsize=15, fontname='Times New Roman')  
ax.set_xlabel('Normalized X',fontsize=15, fontname='Times New Roman')
ax.set_ylabel('Normalized Y',fontsize=15, fontname='Times New Roman') 

plt.show()

