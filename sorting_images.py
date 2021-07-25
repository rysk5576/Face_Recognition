import os
import shutil
import ntpath
import time

base_directory = os.path.dirname(os.path.abspath(__file__))
image_directory = os.path.join(base_directory, "Images")

my_list = os.listdir(image_directory)
extensions = ['jpeg', 'png', 'jpg']
class_names = []


def path_leaf(path_name):
    head, tail = ntpath.split(path_name)
    return tail or ntpath.basename(head)


for people in my_list:
    class_names.append(os.path.splitext(people)[0])  # Splits root name and file extension
    for idx in range(len(class_names)):
        class_names[idx] = class_names[idx].split()[0]
class_names = list(set(class_names))
print(class_names)

try:
    for names in class_names:
        os.mkdir(os.path.join(image_directory, names))
except FileExistsError:
    print('Directory already Exists')

start = time.time()

for root, dirs, files in os.walk(image_directory):
    for file in files:
        if file.endswith('jpeg') or file.endswith('jpg') or file.endswith('png'):
            path = os.path.join(root, file)
            file_name = path_leaf(path)
            file_name = file_name.split()[0]
            if file_name in class_names:
                try:
                    shutil.move(os.path.join(image_directory, file),
                                os.path.join(image_directory, file_name))  # file_name_path = image_directory\file_name
                except shutil.Error:
                    print('Directories already created and exist')
                    break

end = time.time()
total = int((end-start)*1000)
print("All Images Have been Sorted")
print(f"Total Time taken to sort the images: {total} milli seconds")
