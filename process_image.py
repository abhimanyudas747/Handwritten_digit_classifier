# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:50:17 2020

@author: Abhimanyu
"""

import cv2
import matplotlib.pyplot as plt
import joblib
import numpy as np
def process_img():
    #img = plt.imread(image)
    img = cv2.imread('upload.jpg', cv2.IMREAD_UNCHANGED)
    #print('Original Dimensions : ',img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #resized = cv2.resize(img, (28, 28), interpolation = cv2.INTER_AREA)
    #cv2.imshow(img, resized)
    #plt.imshow(img)
    #plt.show()
    img = 255 - img;
    dim = (28, 28)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    #print('Resized Dimensions : ',resized.shape)
    resized = resized/255;
    resized = resized.reshape(1,28,28,1)
    #print(aux.shape)
    #print(aux[0:1])
    cnn = joblib.load('cnn.pkl')
    pred = cnn.predict(resized)
    #pred = [0,0,0,1,0,0,0,0,0,0]
    pred = np.argmax(pred)
    return pred
    
     