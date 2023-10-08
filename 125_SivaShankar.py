def imgjoin1(imgname1,imgname2):
    import cv2
    import numpy as np
    img1=imgname1
    img2=imgname2
    src1 = cv2.imread(img1)
    src2 = cv2.imread(img2)
    hor=np.concatenate((src1,src2),axis=1)
    cv2.imwrite("image_siva3.jpg",hor)
list1=[]
f1=open("cv.txt","r")
im1=f1.readline().replace("\n","")
im2=f1.readline().replace("\n","")
list1.append(im1)
list1.append(im2)
print(im1,im2)
print(list1)
imgjoin1(im1,im2)
