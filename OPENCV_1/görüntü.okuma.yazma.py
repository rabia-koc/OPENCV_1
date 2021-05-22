# Resim okuma işlemi yapıcaz

import cv2
from matplotlib import pyplot as plt
# görsele yakınlaşma hangi pikselde neyin yer aldığını görmek için kullanıyoruz.

resim = cv2.imread("kizkulesi.jpg", 0)
# ilk parametre dosya ismi
# 2. parametreye 0 yazarsak gri tonlamalı olarak dönüşür.

# hazır olarak bir pencere ismi oluşturabilirim.
cv2.namedWindow("resim", cv2.WINDOW_AUTOSIZE)
# 2. parametreye WINDOW_NORMAL yazarsak resmi istediğimiz gibi büyültüp küçültebilirz.

cv2.imshow("resim", resim)
# boş pencere içine aşağıda tanımladığımız resmi ekledir.
"""
resmi renkli göstermek istersek: penceredeki renkle figure olarak gelen resimde farklılık oluyor çünkü
Opencv tarafından renkli görüntü BGR modunda. Ancak Matplotlib RGB modunda görüntülenir.
Dolasıyla, görüntü OpenCV ile okunduğunda renkli görüntüler Matplotlib'de doğru görüntülenmeyecektir.
"""

# resim bir matrixtir. sayılar verilere dönüşüyor.
cv2.imshow("resim penceresi", resim)
# resim göstermesi. ilk parametre açılan pencere ismi, 2. parametre neyi gösterecek resim değişkenini

plt.imshow(resim, cmap = "gray") # ilk parametre neyi göstericem, 2. parametre rengini gri ton ayarladık.
plt.show() # ekrana vermesi için

k = cv2.waitKey(0)
# resmin durması için. içine ms cinsinden bir parametre alıyor.
# biz sıfır yazıcaz çünkü klavyeden herhangi bir tuşa basana kadar beklesin diye
# bir değişkene eşitlesek ve print ile yazdırsak, q' ya bastık ve 131 yazdı.
# gelen sayı tuşun değeri
if k == 27:
    print("ESC tuşuna basıldı.")
# basit bir yol olarak elif içine böyle yazarakta yapılır.
elif k == ord("q"):
    print("q tuşuna basıldı , resim kayıt edildi")
    cv2.imwrite("kizkulesigri.jpg", resim)
    # resmi kaydetme yazma işlemi yapıcaz
    # 2. parametre kayıt olacak nesne

# cv2.destroyWindow("resim penceresi")
# pencereyi kapatmak için.
# hangi pencereyi kapatacaksak içine onu parametre olarak yazarız.

# eğer birden fazla görsel olsaydı onları kapatmak için de şu şekilde
cv2.destroyAllWindows()


