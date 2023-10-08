import cv2
import numpy as np
image1="Ashok.jfif"
image2="Ashok.jfif"
image3="Ashok.jfif"


src1 = cv2.imread(image1)
src2 = cv2.imread(image2)
src3 = cv2.imread(image3)
cv2.imwrite("image_2.png",src1)
img3=np.concatenate((src1,src2,src3),axis=0)
cv2.imwrite('image.png', img3)
