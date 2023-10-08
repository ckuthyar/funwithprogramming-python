import cv2
import numpy as np
image1="1.jpg"
image2="2.jpg"
image3="3.jpg"
image4="4.jpg"
image5="5.jpg"
image6="6.jpg"

src1 = cv2.imread(image1)
src2 = cv2.imread(image2)
src3 = cv2.imread(image3)
src4 = cv2.imread(image4)
src5 = cv2.imread(image5)
src6 = cv2.imread(image6)

img3=np.concatenate((src1,src2,src3),axis=0)
cv2.imwrite("image1.png",img3)
img3=np.concatenate((src4,src5,src6),axis=1)
cv2.imwrite("image2.png",img3)