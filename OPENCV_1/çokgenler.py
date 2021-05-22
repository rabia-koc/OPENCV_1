# * ***ÇOKGENLER***

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# çokgenin koordinatları için bir matrix oluşturuyoruz. 4 tane nokta verdik
pts = np.array([[20,30], [100,120], [255,255], [10,400]], np.int32)

# shape:(4,2) olduğundan dolayı dönüştürme yaptık.
pts2 = pts.reshape(-1,1,2)
# böyle yapınca 0. ve 1. sutünlardan sırayla aldı : 20,30
# diğer türlü olsaydı :reshape(1,1,2) sonucunda 20,100 alırdı ve hata verirdi o yüzden -1 kullandık

cv2.polylines(img, [pts], True, (255,255,255), 3)
# 2. ifade noktalarım
# 3. ifade ise kapalı mı açık mı (True olursa çokgen , False olursa sadece çizgiler olışcaktı.)
# 4. ifade renk
# 5. ifade kalınlık

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

