# * ***DİKDÖRTGEN ÇİZME***

import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(img, (50,50), (300,300), (0,0,255), 5)
# 1. 50'ye 50'den başlıyor
# 2. sağ alt köşesi 300'e 300 bitiyor.
# 3. renk olarak kırmızı
# kalınlık 5 ve içini doldurmak için -1 yazıcaz sonra
# içini dolduma işlemi yapıyoruz.
cv2.rectangle(img, (300,300), (511,511), (0,0,255), -1)

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()