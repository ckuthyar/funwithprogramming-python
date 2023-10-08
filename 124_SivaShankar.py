def opencv1(n1,n2):
    import cv2
    import numpy as np
    img1=n1
    img2=n2
    src1 = cv2.imread(img1)
    src2 = cv2.imread(img2)

    hor=np.concatenate((src1,src2),axis=1)
    ims1=cv2.resize(hor,(800,800))
    cv2.imwrite('image_siva4.png',ims1)
    
f1=open("cv.txt","r")
start=str(f1.readline().replace("\n",""))
print(start)
end=str(f1.readline().replace("\n",""))
print(end)
opencv1(start,end)

