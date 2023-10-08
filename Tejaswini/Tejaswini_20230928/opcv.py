import cv2
image1="ju.jpeg"
src1=cv2.imread(image1)
for i in range(1,3,1):
    cv2.imwrite("Planetr_"+str(i)+".jpeg",src1)
