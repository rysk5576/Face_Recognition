import time
import cv2
import os
from PIL import Image
import face_recognition
import numpy as np

base_directory = os.path.dirname(os.path.abspath(__file__))
image_directory = os.path.join(base_directory, "Images")

images_list = []
class_names = []


def png_converter(picture_path):
    img = Image.open(picture_path)
    img.save(f'{picture_path.split(".")[0]}.png')


def find_encodings(image_list):
    encode_list = []
    for img in image_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list


for directory in os.listdir(image_directory):
    for root, dirs, files in os.walk(os.path.join(image_directory, directory)):
        for file in files:
            if file.endswith("jpeg") or file.endswith("jpg"):
                png_converter(os.path.join(root, file))

            if file.endswith("png"):
                curImg = cv2.imread(os.path.join(root, file))
                images_list.append(curImg)
                class_names.append(os.path.splitext(file)[0])
                for idx in range(len(class_names)):
                    class_names[idx] = class_names[idx].split()[0]

print(list(set(class_names)))

start = time.time()

encode_list_known = find_encodings(images_list)

end = time.time()

print(f'Total Time Taken to encode all the Images = {end-start} seconds')


np.savetxt("encodings.csv", encode_list_known, delimiter=",")

for directory in os.listdir(image_directory):
    for root, dirs, files in os.walk(os.path.join(image_directory, directory)):
        for file in files:
            if file.endswith("png"):
                os.remove(os.path.join(root, file))

print("All PNG Images have been Deleted")













