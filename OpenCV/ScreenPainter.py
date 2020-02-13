import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255

color1 = (133, 236, 45)
color2 = (12, 65, 125)
color = color1
point = (0,0)
radius = 10
pressed = False

# click callback
def click(event, x, y, flags, param):
	global canvas, color, color1, color2, point, radius, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		print("LButton Down")
		point = (x,y)
		pressed = True
		cv2.circle(canvas, point, radius, color, -1)
	elif event == cv2.EVENT_MOUSEMOVE and pressed:
		
		cv2.circle(canvas, (x,y), radius, color, -1)
		
	elif event == cv2.EVENT_LBUTTONUP:
		print("LButton Up")

		pressed = False

		if color == color1:
			color = color2
		else:
			color = color1

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	

cv2.destroyAllWindows()