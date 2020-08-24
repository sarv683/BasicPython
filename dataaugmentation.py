from keras.preprocessing.image import ImageDataGenerator
import logging
import glob
import pathlib
import cv2
import numpy as np
import os
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from PIL import Image

class DataModification:
    def __init__(self, validation_data_path, training_data_path, class_labels):
        #self.validation_data_path = self.__dataaugmentation__(validation_data_path)
        self.training_data_path = self.__dataaugmentation__("C:/predictions/image")
        

    def __dataaugmentation__(self, data_path):
        trainDataGenerator = ImageDataGenerator(shear_range=0.2, zoom_range=0.2,
                                                horizontal_flip=True, rotation_range=20, vertical_flip=True, 
                                                height_shift_range=0.2)
        filenames = glob.glob(data_path + '/*/*.JPG', recursive="True")         
   
        for path in filenames:
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)    
            img = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0)
            #img = Image.open(path)
            #mg = img.resize((224,224), Image.ANTIALIAS)
            #img = np.expand_dims(img, axis=0)
            pathlib.Path('{}/{}/{}'.format(data_path, 'augmented',
                path.split(os.path.sep)[-2])).mkdir(
            parents=True, exist_ok=True)
           # print(path)
            total = 0
            for image in trainDataGenerator.flow(img, batch_size=1,
                    save_to_dir='{}/{}/{}'.format(data_path, 'augmented',
                    path.split(os.path.sep)[-2]), save_format='png'):

                   # print(total)
                    total += 1
                    if total == 150:
                        break
        return (data_path + "/augmented")

def myFunc(image):
    image = np.array(image)
    hsv_image = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    return Image.fromarray(hsv_image)

#DataModification("C:/HiDrive/valid/","C:/HiDrive/train/", [""])

   
        
  
