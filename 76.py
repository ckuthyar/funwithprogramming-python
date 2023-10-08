import cv2
import numpy as np

img2=np.random.randint(255, size=(50,50,3))
cv2.imwrite("newpic1.jpg",img2)

img2=np.random.randint(255, size=(200,200,3))
cv2.imwrite("newpic2.jpg",img2)

img2=np.random.randint(255, size=(400,400,3))
cv2.imwrite("newpic3.jpg",img2)

img2=np.random.randint(255, size=(600,600,3))
cv2.imwrite("newpic4.jpg",img2)


