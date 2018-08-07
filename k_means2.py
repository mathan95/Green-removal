# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:00:43 2018

@author: MathanP
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import cv2

img=mpimg.imread("7.jpg")
A=img/255
ish=A.shape
X=np.reshape(A,(ish[0]*ish[1],ish[2]))

centroids=np.array([0,1,0])
errlist=np.zeros((X.shape[0],1),np.float64)

for p in range(0,X.shape[0],1):
    mat=X[p,:]
    mat3=mat-centroids
    err=np.sum(np.multiply(mat3,mat3))
    errlist[p]=err

threshold=0.7
errlist=np.greater(errlist,threshold)
X=np.multiply(X,errlist)
X_out=np.reshape(X,(ish[0],ish[1],ish[2]))


plt.subplot(1,2,1),plt.imshow(X_out)
plt.subplot(1,2,2),plt.imshow(mpimg.imread('2.jpg'))
