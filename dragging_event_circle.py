import cv2
import numpy as np

ix,iy = 30,40
drawing = False

img = np.zeros((512,512,3))

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event ==  cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img,(ix,iy),(x,y),color = (255,0,0),thickness = -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),color = (255,0,0),thickness = -1)
        
cv2.namedWindow(winname = 'Dragging Rectangle')

cv2.setMouseCallback('Dragging Rectangle',draw_rectangle)

while True:
    cv2.imshow('Dragging Rectangle',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()        
# Closes all windows if more than 1 are open