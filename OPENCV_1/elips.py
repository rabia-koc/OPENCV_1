#  ***ELİPS ÇİZMEK***

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, (255,100,0), 3)
# 2. si merkezi
# 3. ise uzunluğu
# 4. açısı
# 5. başlangıç açısı
# 6. bitiş açısı
# 7. rengi
# kalınlığı

# içi dolu hali
cv2.ellipse(img, (100,100), (100,50), 0, 0, 180, (255,100,0), -1)

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


