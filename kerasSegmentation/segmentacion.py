#!/usr/bin/env python

# Pattern Recognition and Machine Learning (PARMA) Group
# School of Computing, Costa Rica Institute of Technology
#
# title           :unet_CellSegmentation.py
# description     :Cell segmentation using pretrained unet architecture.
# authors         :Willard Zamora wizaca23@gmail.com,
#                 Manuel Zumbado manzumbado@ic-itcr.ac.cr
# date            :20180823
# version         :0.1
# usage           :python unet_CellSegmentation.py
# python_version  :>3.5
# ==============================================================================
#
import os
import time
import numpy as np

from PIL import Image
import glob
from keras.models import Model
from keras.layers import Input, concatenate
from keras.layers import Conv2D, MaxPooling2D, Conv2DTranspose
from keras.optimizers import Adam
from keras import backend as K

# Set channel configuration for backend
K.set_image_data_format('channels_last')

# Image size
img_rows = 256
img_cols = 256
# Dice coeficient parameter
smooth = 1.


def dice_coef(y_true, y_pred):

    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)

    coeficiente = (2. * intersection + smooth)
    coeficiente = coeficiente/(K.sum(y_true_f))
    coeficiente = coeficiente+K.sum(y_pred_f)+smooth
    return coeficiente


def load_test_data(image_path):
    raw = []
    image_filename = dict()
    count = 0
    for filename in glob.glob(image_path):
        name = os.path.basename(filename)[:-4]
        try:
            im = Image.open(filename)
            im = im.convert('L')
            im = im.resize((img_rows, img_cols))
            raw.append(np.array(im))
            image_filename[count] = name
            count = count+1
            im.close()
            print(123)
        except IOError:
            print('Error loading image ', filename)
        
    return [raw, image_filename]


