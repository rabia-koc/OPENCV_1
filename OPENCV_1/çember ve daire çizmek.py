# * ***ÇEMBER VE DAİRE ÇİZME***

import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

cv2.circle(img, (255,255), 60, (120,120,120), 2)
# ilk parametre kaydedeceği görüntü
# 2. si çizeceğimiz dairenin merkezi
# 3. yarıçapı 60 piksel
# 4. renk
# 5. kalınlık

# daire için
cv2.circle(img, (100,100), 90, (255,50,50), -1)

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
