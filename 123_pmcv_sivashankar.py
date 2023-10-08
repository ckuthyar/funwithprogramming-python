import cv2
import numpy as np
img1="modi.jpg"
img2="manmohan.png"
img3="ATV.png"
img4="IG.jpg"
img5="LBS.jpg"
img6="nehru.jpg"


src1=cv2.imread(img1)
src2=cv2.imread(img2)
src3=cv2.imread(img3)
src4=cv2.imread(img4)
src5=cv2.imread(img5)
src6=cv2.imread(img6)

# 6 differnt size of horzontal images with axis=1 

hori=np.concatenate((src1,src2,src3,src4,src5,src6),axis=1)
cv2.imwrite('imageh.png',hori)

hori=np.concatenate((src1,src2,src3,src4,src5,src6),axis=1)
ims1=cv2.resize(hori,(1366,768))
cv2.imwrite('imageh1.png',ims1)

hori=np.concatenate((src1,src2,src3,src4,src5,src6),axis=1)
ims1=cv2.resize(hori,(1920,1080))
cv2.imwrite('imageh2.png',ims1)

hori=np.concatenate((src1,src2,src3,src4,src5,src6),axis=1)
ims1=cv2.resize(hori,(1280,768))
cv2.imwrite('imageh3.png',ims1)

hori=np.concatenate((src1,src2,src3,src4,src5,src6),axis=1)
ims1=cv2.resize(hori,(2560,1600))
cv2.imwrite('imageh4.png',ims1)

hori=np.concatenate((src1,src2,src3,src4,src5,src6),axis=1)
ims1=cv2.resize(hori,(800,600))
cv2.imwrite('imageh5.png',ims1)

hori=np.concatenate((src1,src2,src3,src4,src5,src6),axis=1)
ims1=cv2.resize(hori,(750,334))
cv2.imwrite('imageh6.png',ims1)

#6 different size vertival images with axis=0

verti=np.concatenate((src1,src2,src3,src4,src5,src6),axis=0)
cv2.imwrite('imagev.png',verti)

verti=np.concatenate((src1,src2,src3,src4,src5,src6),axis=0)
ims2=cv2.resize(verti,(768,1366))
cv2.imwrite('imagev1.png',ims2)

verti=np.concatenate((src1,src2,src3,src4,src5,src6),axis=0)
ims2=cv2.resize(verti,(1080,1920))
cv2.imwrite('imagev2.png',ims2)

vrti=np.concatenate((src1,src2,src3,src4,src5,src6),axis=0)
ims2=cv2.resize(verti,(768,1280))
cv2.imwrite('imagev3.png',ims2)

verti=np.concatenate((src1,src2,src3,src4,src5,src6),axis=0)
ims2=cv2.resize(verti,(1600,2560))
cv2.imwrite('imagev4.png',ims2)

verti=np.concatenate((src1,src2,src3,src4,src5,src6),axis=0)
ims2=cv2.resize(verti,(600,800))
cv2.imwrite('imagev5.png',ims2)

verti=np.concatenate((src1,src2,src3,src4,src5,src6),axis=0)
ims2=cv2.resize(verti,(334,750))
cv2.imwrite('imagev6.png',ims2)

