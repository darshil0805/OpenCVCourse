import cv2

img = cv2.imread("cat.jpg")
while True:
    cv2.imshow("Window Name",img)
    if cv2.waitKey(1) & 0xFF = 27:
        break
cv2.destroyAllWindows()        