import cv2 

image = 'p1.jpg'  #changed from .png to .jpg on 28-Sep-2023 by CS
new_width = 1100
new_height = 1100

b1 = cv2.imread(image)

resized_image = cv2.resize(b1,(new_width, new_height))
cv2.imwrite('resized_p1.png', resized_image)
