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
    img = cv2.imread('upload', cv2.IMREAD_UNCHANGED)
    #print('Original Dimensions : ',img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #resized = cv2.resize(img, (28, 28), interpolation = cv2.INTER_AREA)
    #cv2.imshow(img, resized)
    #plt.imshow(img)
    #plt.show()
    
   
    dim = (28, 28)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    resized.reshape(1,28,28)
    #print('Resized Dimensions : ',resized.shape)
    aux = np.array([resized])
    #print(type(resized))
    aux = aux/255
    #print(aux.shape)
    #print(aux[0:1])
    ann = joblib.load('Digitclassifier.pkl')
    pred = ann.predict(aux[0:1])
    #pred = [0,0,0,1,0,0,0,0,0,0]
    pred = np.argmax(pred)
    return pred
    
     