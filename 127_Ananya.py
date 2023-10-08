import cv2
import numpy as np

src1 = cv2.imread("1.jfif")
src2 = cv2.imread("2.jfif")
src3 = cv2.imread("3.jfif")
src4 = cv2.imread("4.jfif")
src5 = cv2.imread("5.jfif")
src6 = cv2.imread("6.jfif")
src7 = cv2.imread("7.jfif")
src8 = cv2.imread("8.jfif")
src9 = cv2.imread("9.jfif")

src1=cv2.resize(src1,(200,200))
src2=cv2.resize(src2,(200,200))
src3=cv2.resize(src3,(200,200))
src4=cv2.resize(src4,(200,200))
src5=cv2.resize(src5,(200,200))
src6=cv2.resize(src6,(200,200))
src7=cv2.resize(src7,(200,200))
src8=cv2.resize(src8,(200,200))
src9=cv2.resize(src9,(200,200))

h_stack1=np.hstack([src1,src2,src3])
h_stack2=np.hstack([src4,src5,src6])
h_stack3=np.hstack([src7,src8,src9])

v_stack=np.vstack([h_stack1,h_stack2,h_stack3])
cv2.imwrite('image1.png',v_stack)


