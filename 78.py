import cv2

img1=cv2.imread("pic1.jpg")
img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imwrite("pic2.jpg",img2)

