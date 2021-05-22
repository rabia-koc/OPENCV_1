# ***YAZI YAZMAK***

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV', (10,400), font, 4, (0,255,255), 2, cv2.LINE_AA)
# 2. ifade yazının ne olacağı
# 3. ifade yazının sol alt köşede hangi koordinatlarda yer alacağı
# 4. fontu 4 boyut
# 5. renk
# 6. kalınlık
# 7. daha iyi görüntü sağlaması için

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

