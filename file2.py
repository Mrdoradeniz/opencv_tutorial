import cv2
import random
from cv2 import imread
from cv2 import imshow

img=imread("resim1.jpg",-1)

# [blue, green, red]

img=cv2.resize(img,(0,0),fx=0.1,fy=0.1)


# img[y_ekseni][x_ekseni]
# 100x200 alanındaki pixelleri random renk şeyleri oluşturduk.

for i in range(100):

    for a in range(200):
        
        img[i][a] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]



imshow("Title of window",img)



cv2.waitKey(0)

cv2.destroyAllWindows()




