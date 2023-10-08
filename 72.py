import cv2
import numpy as np

img1=cv2.imread("pic1.jpg")

dsize=(img1.shape[1],100)
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic1.jpg",img2)

dsize=(img1.shape[1],200)
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic2.jpg",img2)

dsize=(img1.shape[1],400)
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic3.jpg",img2)

dsize=(img1.shape[1],600)
img2=cv2.resize(img1,dsize,interpolation=cv2.INTER_AREA)
cv2.imwrite("newpic4.jpg",img2)


