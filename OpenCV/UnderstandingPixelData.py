import numpy as np 
import cv2

img = cv2.imread("C:/Users/svark/Desktop/Projects/OpenCV/opencv-logo.png", 1)

print(type(img))
print(len(img))
print(len(img[0]))
print(img.shape)
print(img.dtype)

# get the pixel values at a specific area
print(img[10,5])

print(img[:, :, 0])
