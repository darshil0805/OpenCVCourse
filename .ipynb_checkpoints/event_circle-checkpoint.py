import cv2
import numpy as np

# Function based on cv2 event

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)
        
img = np.zeros((512,512,3),np.uint8)

# Naming the window
cv2.namedWindow(winname = "Circle")
cv2.setMouseCallback("Circle",draw_circle)

while True:
    cv2.imshow("Circle",img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()        