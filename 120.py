import cv2
image1="Ashok_Samrat.jpg"
src1=cv2.imread(image1)
for i in range(1,11,1):
    cv2.imwrite("Aditya_"+str(i)+".jpg",src1)
