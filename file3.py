import cv2
from cv2 import imread
from cv2 import imshow



img=imread("resim1.jpg",-1)



img=cv2.resize(img,(0,0), fx=0.15,fy=0.15)


# resimdeki belirli bir alan nasıl kırpılır o gösterilmiştir

crop=img[100:200,200:300]

img[300:400,250:350]=crop



imshow("Title of Window",img)


cv2.waitKey(0)

cv2.destroyAllWindows()