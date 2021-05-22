
# * ***ÇİZGİ ÇİZME***

import cv2
import numpy as np # boş bir siyah görüntü elde etmek için kullanıyorum.

img = np.zeros((512, 512, 3), np.uint8)
# 3 renk uzayına sahip olması için 3 ekledim.
# poztif int sayılar kullanacağımı da ekledim.


cv2.line(img, (50,400), (400,50), (0,255,0), 10)
# sol alt köşeden başlaıyor
# 2. gideceği kordinat sağ üst köşeden bir yer
# 3. parametrede rengi yeşil yaptık
# kalınlığı 10

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()













