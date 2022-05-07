import cv2

# resim dosyasını okuyoruz
img=cv2.imread("resim1.jpg",-1)

# -1 Loads a color image. Any transparency of image will neglacted
#  0 Loads image in grayscale mod
#  1 Loads image as such including alpha channel










# resimin oranını bozmadan küçültmek için kullanılır.
img=cv2.resize(img,(0,0),fx=0.1,fy=0.1)

print(img.shape)
# (en,boy,channel)

# Resimi istediğmiz boyuta getirmek için kullanılır 300x400
#img=cv2.resize(img,(300,400))




# resimi 90 derece döndürür
img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE) 


# program ismi ve resim değişkenini alır
cv2.imshow("Name of Program",img)


# herhangi bir tuşa basılana kadar beklemesi gereken süre
# eğer değer yerine 0 yazılırsa hernagi bir tuşa basana kadar bekler
cv2.waitKey(0)

# open cv nin açtığı tüm ekranlası kapatır
cv2.destroyAllWindows()



