import cv2
import numpy as np
image1="new1.jpg"
image2="new1.jpg"
image3="new1.jpg"
image4="new1.jpg"
image5="new1.jpg"
image6="new1.jpg"

src1 = cv2.imread(image1)
src2 = cv2.imread(image2)
src3 = cv2.imread(image3)
src4 = cv2.imread(image4)
src5 = cv2.imread(image5)
src6 = cv2.imread(image6)
cv2.imwrite("image1.jpg",src1)
img3=np.concatenate((src1,src2,src3),axis=0)
cv2.imwrite("image1_axis0.png",img3)
img3=np.concatenate((src4,src5,src6),axis=1)
cv2.imwrite("image2_axis1.png",img3)
