from tensorflow.keras.preprocessing.image import ImageDataGenerator
import logging
import glob
import pathlib
import cv2
import numpy as np
import os
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import array_to_img
import shutil
from PIL import Image

ext = ['png', 'jpg', 'gif', 'tiff']  
files = []
original_image_path = "C:/linedata/train/good"

class DataModification:

    def __init__(self, original_image_path):
        #self.validation_data_path = self.__dataaugmentation__(validation_data_path)
        self.training_data_path = self.__dataaugmentation__(original_image_path)
      #  self.final_data_path = self.__split_dataset__("C:/predictions/val")
        #print(self.training_data_path)        

    def __dataaugmentation__(self, data_path):
        trainDataGenerator = ImageDataGenerator(shear_range=0.2, zoom_range=0.2,
                                                horizontal_flip=True, rotation_range=20, vertical_flip=True, 
                                                height_shift_range=0.2)
        
        [files.extend(glob.glob(data_path + '/*.' + e)) for e in ext]
        
         
   
        for path in files:
            print(path)
            
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)    
            img = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0)
            #img = Image.open(path)
            #mg = img.resize((224,224), Image.ANTIALIAS)
            #img = np.expand_dims(img, axis=0)
                     # print(path)
            a = (path.split(os.path.sep)[-1])
            total = 0
            print(a, data_path)
            for _ in trainDataGenerator.flow(img, batch_size=1,
                    save_to_dir='{}/{}/{}'.format(data_path, 'augment',
                 a), save_format='png'):

                   # print(total)
                    total += 1
                    if total == 1:
                        break
        return (data_path + "/augmented")


    def __split_dataset__(self, data_path):
        #copy from the created augmented directory to validation and training dataset. split 80/20
        # 
        os.makedirs(data_path + "val")
        [files.extend(glob.glob(data_path + '*.' + e)) for e in ext]
        print(len(files))
        for i in range(0, int(0.8*len(files))):
            for img in files:
                shutil.move(img, data_path+"val")        

        
DataModification(original_image_path)  
        
  

















