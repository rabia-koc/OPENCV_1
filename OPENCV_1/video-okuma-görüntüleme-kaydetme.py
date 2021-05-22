import cv2
import numpy as np

# pikselleri gösterdi.

sifir = np.zeros([300,300])  # sıfırlardan oluşan matrix(siyah)
bir = np.ones([300,300])     # birlerden oluşan matrix(beyaz)

cv2.namedWindow("sifir", cv2.WINDOW_NORMAL)
cv2.namedWindow("bir", cv2.WINDOW_NORMAL)

cv2.imshow("sifir", sifir)
cv2.imshow("bir", bir)

cv2.waitKey(0)
cv2.destroyAllWindow()

