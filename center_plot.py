import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 标注文件的目录
annotations_dir = 'Your folder'

x_centers = []
y_centers = []

for filename in os.listdir(annotations_dir):
    filepath = os.path.join(annotations_dir, filename)
    with open(filepath, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split()
            if len(parts) >= 5:
                x_center, y_center = map(float, parts[1:3])
                x_centers.append(x_center)
                y_centers.append(y_center)

x_centers = np.array(x_centers)
y_centers = np.array(y_centers)

heatmap, xedges, yedges = np.histogram2d(x_centers, y_centers, bins=(50, 50))

plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(8, 6))
ax = sns.heatmap(heatmap.T, cmap='YlGnBu', cbar_kws={'label': 'Frequency'})
cbar = ax.collections[0].colorbar

cbar.set_label('Frequency', fontsize=13, fontname='Times New Roman')
cbar.ax.tick_params(labelsize=13)

plt.title('Heatmap of Annotation Box Center Distribution', fontname='Times New Roman',fontsize=15)
plt.xlabel('X Center', fontname='Times New Roman',fontsize=15)
plt.ylabel('Y Center', fontname='Times New Roman',fontsize=15)

plt.xticks(np.linspace(0, 50, num=6), labels=np.round(np.linspace(0, 1, num=6), 2), fontname='Times New Roman',fontsize=15)
plt.yticks(np.linspace(0, 50, num=6), labels=np.round(np.linspace(0, 1, num=6), 2), fontname='Times New Roman',fontsize=15)

plt.show()

plt.figure(figsize=(10, 6))
plt.hist(x_centers, bins=10, alpha=0.5, color='yellow', label='X Centers', edgecolor='yellow')

plt.hist(y_centers, bins=10, alpha=0.5, color='blue', label='Y Centers', edgecolor='blue')

plt.title('Distribution of Annotation Box Center Coordinates')
plt.xlabel('Normalized Center Coordinates')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.legend()  
plt.show()

print('ok')