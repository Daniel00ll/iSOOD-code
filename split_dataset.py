import os
import shutil
from sklearn.model_selection import train_test_split

images_folder = 'Image folder' 
annotations_folder = 'Label folder'  

train_images_dest = 'ROOT\\train\images' 
train_annotations_dest = 'ROOT\\train\labels'  

val_images_dest = 'ROOT\\valid\images'  
val_annotations_dest = 'ROOT\\valid\labels'  

test_images_dest = 'ROOT\\test\images'  
test_annotations_dest = 'ROOT\\test\labels'  

for folder in [train_images_dest, train_annotations_dest, val_images_dest, val_annotations_dest, test_images_dest, test_annotations_dest]:
    if not os.path.exists(folder):
        os.makedirs(folder)

file_names = [os.path.splitext(f)[0] for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]

train_files, test_files = train_test_split(file_names, test_size=0.2, random_state=42)  
val_files, test_files = train_test_split(test_files, test_size=0.5, random_state=42) 

def move_files(file_list, src_folder, dest_folder, file_ext):
    for file_name in file_list:
        shutil.move(os.path.join(src_folder, file_name + file_ext),
                    os.path.join(dest_folder, file_name + file_ext))

move_files(train_files, images_folder, train_images_dest, '.jpg') 
move_files(train_files, annotations_folder, train_annotations_dest, '.txt')

move_files(val_files, images_folder, val_images_dest, '.jpg')
move_files(val_files, annotations_folder, val_annotations_dest, '.txt')

move_files(test_files, images_folder, test_images_dest, '.jpg')
move_files(test_files, annotations_folder, test_annotations_dest, '.txt')

