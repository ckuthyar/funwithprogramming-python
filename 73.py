import cv2
import numpy as np

img1=cv2.imread("pic1.jpg")

dsize=(100,img1.shape[1])
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic1.jpg",img2)

dsize=(200,img1.shape[0])
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic2.jpg",img2)

dsize=(400,img1.shape[0])
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic3.jpg",img2)

dsize=(600,img1.shape[0])
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic4.jpg",img2)


