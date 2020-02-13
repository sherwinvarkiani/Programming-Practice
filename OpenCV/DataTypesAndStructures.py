import numpy as np 
import cv2

black = np.zeros([150, 200, 1], 'uint8')

# show
cv2.imshow("Black", black)
print(black[0,0,:])

# [height, width, channels]
ones = np.ones([150, 200, 3], 'uint8')
cv2.imshow("Ones", ones)
print(ones[0,0,:])

# White box
white = np.ones([150, 200, 3], 'uint16')
white *= (2**16-1) # maximum value
cv2.imshow("White", white)
print(white[0,0,:])

# copy is a deep copy
color = ones.copy()
color[:,:] = (255,0,0) # Colors in BGR
cv2.imshow("Blue", color)
print(color[0,0,:])


cv2.waitKey(0)
cv2.destroyAllWindows()