import cv2
picture1="Ashok_Smart.jpg"
picture2="Ashok_Smart.jpg"

img1=cv2.imread(picture1,cv2.IMREAD_COLOR)
img2=cv2.imread(picture2,cv2.IMREAD_COLOR)

img3=cv2.addWeighted(img1,1,img2,1,0.0)
cv2.imwrite("pic3.jpg",img3)

