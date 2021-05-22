import cv2
import numpy as np

# ses açıp kısma işlemini ayarlamaya denir.

# bu fonksiyon hiçbir işlem yapmıyor.
# bize 0 ile 255 arasında biz trackbarı oynattığımızda  trackbarın hangi değerde olduğunu geri döndüren bir ifade döndürüyor.
def nothing(x):
    pass


img = np.zeros((512, 512, 3), np.uint8)  # siyah bir görüntü

cv2.namedWindow("resim")  # boş bir çerçeve oluşturdum.

"""
çerçeve içine trackbar dahil ediyorum.
ilk alacağı isim için RGB olarak renkleri kontrol edicez
2. ifade resim içinde yer alacak.
3. ifade değerinin başlangıcı 0 ile başlayıp 255'e kadar artacak
4. fonksiyon girdik.
"""
cv2.createTrackbar("R", "resim", 0, 255, nothing)
cv2.createTrackbar("G", "resim", 0, 255, nothing)
cv2.createTrackbar("B", "resim", 0, 255, nothing)

# bir switch oluşturuyorum.
cv2.createTrackbar("ON/OF", "resim", 0, 1, nothing)  # 0 ile 1 aralğında aç kapa olacak

# döngüye koyarız çünkü görüntü sürekli ekranda kalsın diye
while (1):
    cv2.imshow("resim", img)
    # 27:ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break
    # renkleri ayarlamak için
    r = cv2.getTrackbarPos("R", "resim")
    g = cv2.getTrackbarPos("G", "resim")
    b = cv2.getTrackbarPos("B", "resim")

    switch = cv2.getTrackbarPos("ON/OF", "resim")  # böyle switch değerini okuyorum.
    # 1 ise beyaz ekran çıkar
    if switch:
        img[:] = [b, g, r]
    # 0 ise siyah ekran çıkar
    else:
        img[:] = 0

    # img görselimi eklemem gerekiyor.
    # img tüm piksellerine eşitliyorum
    # img[:] = [b, g, r]

cv2.destroyAllWindows()