import cv2

# yapacağımız işlem paint benzeri bir işlem olacak.
# kullanacğım event ifadesi geçen cümleler geldi.
for i in dir(cv2):
    if 'EVENT' in i:
        print(i)

import cv2
import numpy as np

# eventte şurdaki olaylar hangisi yer alacak.
def draw(event, x, y, flags, param):
    # fareye 2 defa tıklayınca içi dolu daire çizdi.
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)  # 50 yarıçapı


img = np.ones((512, 512, 3), np.uint8) # bir görüntü oluşturuyorum.

# boş bir pencere oluştutup içine de paint diyoruz.
cv2.namedWindow("paint")

cv2.setMouseCallback("paint", draw)
# ilk pencere ismii
# 2.si draw fonksiyonu: klavye hareketlerini tanımlayacğımız fonksiyon

# döngü açıp görüntümü gösteriyorum.
while (1):
    cv2.imshow("paint", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()


