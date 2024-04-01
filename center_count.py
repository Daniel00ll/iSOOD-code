import os

annotations_dir = 'Your folder'

middle_area_count = 0  
edge_area_count = 0  

for filename in os.listdir(annotations_dir):
    filepath = os.path.join(annotations_dir, filename)
    with open(filepath, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split()
            if len(parts) >= 5:
                x_center, y_center = map(float, parts[1:3])

                if 0.25 <= x_center <= 0.75 and 0.25 <= y_center <= 0.75:
                    middle_area_count += 1
                else:
                    edge_area_count += 1

print(f"Number of boxes in the middle area: {middle_area_count}")
print(f"Number of boxes in the edge area: {edge_area_count}")
