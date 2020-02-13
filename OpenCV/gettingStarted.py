import numpy as np 
import cv2

# load image
img = cv2.imread("C:/Users/svark/Desktop/Projects/OpenCV/opencv-logo.png", 0)

# display image
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

# wait indefinitely until the user interacts with the keyboard
cv2.waitKey(0)

# write back to file
cv2.imwrite("output.jpg", img)