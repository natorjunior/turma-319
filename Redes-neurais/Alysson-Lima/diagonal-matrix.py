# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QKPolIxevIGjdtrdCoPeFma1IEY5TY6R
"""

import numpy
import pandas as pd

mult = numpy.zeros((15, 15),dtype=int)

df = pd.DataFrame(mult)

for i in range (15):
  for j in range(15):
    if i+j == 14:
      df.iloc[i,j] = 255
  df.iloc[i,i] = 255

df

import cv2

cv2.imwrite("df.png",df.values)

df.values