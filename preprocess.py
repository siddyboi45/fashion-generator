# -*- coding: utf-8 -*-
"""preprocess.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uP54m3SM1tApECma5jfG3xMyfoNceBhF
"""

import shutil
import json
import os
from google.colab import drive
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pickle
drive.mount('/content/drive')

# Unzip the compressed data into the DeepFashion Directory
# Repeat for each compressed file the dataset has
!unzip '/content/drive/MyDrive/dataset.zip' -d '/content/DeepFashion/'

# The bounding box coordinates for each image is present in the list_bbox.txt file
# Iterate through each image and crop it based on the coordinates in list_bbox.txt

deepfashion_root = '/content/DeepFashion/'
save_root = '/content/drive/MyDrive/'

category_annofile = deepfashion_root + 'Anno_coarse/list_category_cloth.txt'
category_imgfile = deepfashion_root + 'Anno_coarse/list_category_img.txt'
category_bboxfile = deepfashion_root + 'Anno_coarse/list_bbox.txt'

categories = open(category_annofile).readlines()[2:]
images = open(category_imgfile).readlines()[2:]
bboxs = open(category_bboxfile).readlines()[2:]

print ('Num of Deepfashion Categories: ', len(categories))
print ('Num of Deepfashion Category Images: ', len(images))
print ('Num of Deepfashion Category bboxs: ', len(bboxs))

for idx in range(len(images)):
  # print ('---', idx, '---', len(images))
  image_name = images[idx].split(' ')[0]
  if (image_name.split('/')[1] in os.listdir('/content/drive/MyDrive/cropped/img/')):
    continue
  category_id = eval(images[idx].split(' ')[-1])
  image_file = deepfashion_root + image_name

  x1, y1, x2, y2 = map(int, bboxs[idx].split(' ')[-4:])

  # print(image_name)
  # print(category_id)
  # print(image_file)
  
  image = Image.open(image_file)
  cropped = image.crop((x1, y1, x2, y2))
  path = image_name.split('/')[0] + '/' + image_name.split('/')[1] + '/'
  if not (os.path.exists(save_root + 'cropped/' + path)):
    os.makedirs(save_root + 'cropped/' + path)
  cropped.save(save_root + 'cropped/' + image_name[:-4] + '.png', format = 'PNG')

# The images also have categories associated with them
# This bit of code is specially needed for the conditional DCGAN model
categories = [x.split(' ')[0] for x in open('/content/DeepFashion/Anno_coarse/list_category_cloth.txt').readlines()[2:]]
img_cat_ids = open('/content/DeepFashion/Anno_coarse/list_category_img.txt').readlines()[2:]

# Copy cropped images from the /cropped directory and move them into a labelled folder structure. That is,
# /img/label_name/img_name.png

save_root = '/content/drive/MyDrive/cropped/'

for idx in range(len(img_cat_ids)):
  image_name = img_cat_ids[idx].split(' ')[0]
  category_id = eval(img_cat_ids[idx].split(' ')[-1])
  print(image_name)
  print(category_id)
  print(categories[category_id-1])
  # image_file = deepfashion_root + image_name
  if not (os.path.exists(save_root + 'labelled_imgs/' + categories[category_id-1])):
    os.makedirs(save_root + 'labelled_imgs/' + categories[category_id-1])
  if not (os.path.exists(save_root + image_name)):
    continue
  shutil.copy(save_root + image_name, save_root + 'labelled_imgs/' + categories[category_id-1])
  break