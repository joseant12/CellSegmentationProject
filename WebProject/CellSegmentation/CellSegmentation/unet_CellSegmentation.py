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
from .contador import pintarCelulas

img_rows = 256
img_cols = 256
smooth = 1.
os.chdir(os.path.dirname(__file__))
def analyze(directorio,coleccion):
    # Set channel configuration for backend
    K.set_image_data_format('channels_last')

    # Image size
    
    # Dice coeficient parameter
    
    # Paths declaration
    print(os.getcwd())
    weights_path = 'pre_0_3_5.h5'
    name = directorio[:-5]
    pred_dir = name + 'preds/'
    predict(directorio,weights_path,pred_dir,coleccion)


# Compute dice coeficient used in loss function
def dice_coef(y_true, y_pred):

    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)

    coeficiente = (2. * intersection + smooth)
    coeficiente = coeficiente/(K.sum(y_true_f))
    coeficiente = coeficiente+K.sum(y_pred_f)+smooth
    return coeficiente


# Loss function
def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)


# Load test data from directory
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
        except IOError:
            print('Error loading image ', filename)
    return [raw, image_filename]


# Preprocess loaded images
def preprocess(imgs):
    imgs_p = np.ndarray((len(imgs), img_rows, img_cols), dtype=np.float32)
    for i in range(len(imgs)):
        imgs_p[i] = imgs[i].reshape((img_rows, img_cols))/255.

    imgs_p = imgs_p[..., np.newaxis]

    # Perform data normalization
    mean = imgs_p.mean()
    std = imgs_p.std()
    imgs_p -= mean
    imgs_p /= std
    return imgs_p


# Define unet architecture
def get_unet():
    inputs = Input((img_rows, img_cols, 1))
    conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
    conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool1)
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(pool2)
    conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(pool3)
    conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

    conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(pool4)
    conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv5)

    up6 = concatenate([Conv2DTranspose(256, (2, 2), strides=(2, 2),
                      padding='same')(conv5), conv4], axis=3)

    conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')(up6)
    conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv6)

    up7 = concatenate([Conv2DTranspose(128, (2, 2), strides=(2, 2),
                      padding='same')(conv6), conv3], axis=3)
    conv7 = Conv2D(128, (3, 3), activation='relu', padding='same')(up7)
    conv7 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv7)

    up8 = concatenate([Conv2DTranspose(64, (2, 2), strides=(2, 2),
                      padding='same')(conv7), conv2], axis=3)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(up8)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv8)

    up9 = concatenate([Conv2DTranspose(32, (2, 2), strides=(2, 2),
                      padding='same')(conv8), conv1], axis=3)
    conv9 = Conv2D(32, (3, 3), activation='relu', padding='same')(up9)
    conv9 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv9)

    conv10 = Conv2D(1, (1, 1), activation='sigmoid')(conv9)

    model = Model(inputs=[inputs], outputs=[conv10])

    model.compile(optimizer=Adam(lr=1e-4),
                  loss=dice_coef_loss, metrics=[dice_coef])

    return model


def predict(image_path,weights_path,pred_dir,coleccion):
    
    print('-'*30)
    print('Loading and preprocessing test data...')
    print('-'*30)

    # Load test data
    cell_segmentation_data = load_test_data(image_path)

    # Preprocess and reshape test data
    x_test = preprocess(cell_segmentation_data[0])
    test_id = cell_segmentation_data[1]

    print('-'*30)
    print('Creating and compiling model...')
    print('-'*30)
    # Get model
    model = get_unet()

    print('-'*30)
    print('Loading saved weights...')
    print('-'*30)
    # Load weights
    model.load_weights(weights_path)

    print('-'*30)
    print('Predicting masks on test data...')
    print('-'*30)
    # Make predictions
    imgs_mask_predict = model.predict(x_test, verbose=1)

    print('-' * 30)
    print('Saving predicted masks to files...')
    np.save('imgs_mask_predict.npy', imgs_mask_predict)
    print('-' * 30)
    if not os.path.exists(pred_dir):
        os.mkdir(pred_dir)
        new_dir = pred_dir + "count/"
        os.makedirs(new_dir)
    # Save predictions as images
    for image_pred, index in zip(imgs_mask_predict, range(x_test.shape[0])):
        image_pred = image_pred[:, :, 0]
        image_pred[image_pred > 0.5] *= 255.
        im = Image.fromarray(image_pred.astype(np.uint8))
        pred_img = os.path.join(pred_dir, str(test_id[index]) + '_pred.png')
        im.save(pred_img)
        pintarCelulas(pred_img,coleccion,str(test_id[index]))


if __name__ == '__main__':
    pass
