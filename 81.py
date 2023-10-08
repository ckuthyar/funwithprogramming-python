import cv2
import numpy as np
image1="Ashok_Samrat_1.jpg"
image2="Ashok_Samrat_2.jpg"

src1 = cv2.imread(image1)
src2 = cv2.imread(image2)

img3=np.concatenate((src1,src2),axis=1)
cv2.imwrite('image.png', img3)

