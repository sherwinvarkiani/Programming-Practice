import numpy as np 
import cv2
color = cv2.imread("butterfly.jpg", 1)

# Convert image to grayscale
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg", gray)

# Split channels
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

# Set up alpha layer (transparency layer)
# setting the last input as g means a high green value will have a high alpha value (opaque)
# and a low green value as transparent
rgba = cv2.merge((b,g,r,g))

# png as it supports transparency
cv2.imwrite("rgba.png", rgba)