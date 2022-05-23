# fashion-generator
This is the code repository of our final project as part of CSE-676 Deep Learning Course

# Objective
The objective is to build a dynamic Fashion Generator model that can generate new fashion and clothing ideas with the help of the user's input

# Instructions to run code
1. Download the DeepFashion Dataset from the official page. Pick the Category and Attribute Prediction Benchmark folder to download
2. The downloaded file(s) are compressed zip files.
3. Run the preprocess.py to unzip and preprocess the data. The preprocess.py file has a command to unzip a single file. The same line could be repeated for unzipping multiple files
4. The preprocess.py step also performing the feature extraction phase. That is the cloth coordinates are taken and the image is cropped with just the clothes, removing the extra noise.
5. The preprocess.py step also categorises the existing folder structure into a labelled folder structure - 'img_folder/label_name/img_file.png'. This is done so that it is easier for the ImageFolder() function to read and assign labels to each image
6. The preprocess.py function creates the cropped images as well as the labelled_imgs folder structure
7. This folder structure is used in the three models built as part of this experiment
8. Run the following .py files to execute each model
    a. vanilla_GAN.ipynb - To build a vanilla_GAN generator model that can generate new clothing ideas
    b. dcgan.py - To build a Deep Convolutional GAN generator model that can generate new clothing ideas
    c. cdcgan.py - To build a Conditional DCGAN generator model that can generate new clothing ideas
