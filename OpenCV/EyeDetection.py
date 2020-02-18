import numpy as np 
import cv2

img = cv2.imread("faces.jpeg", 1)
#img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

path = "haarcascade_eye.xml"

eye_cascade = cv2.CascadeClassifier(path)

eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=20, minSize=(20,20))
print(len(eyes))

for (x, y, w, h) in eyes:
    xc = (x + x+w)/2
    yc = (y + y+h)/2
    radius = w/2
    cv2.circle(img, (int(xc),int(yc)), int(radius), (0,0,255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()