# * ***VİDEO ÇEKME İŞLEMİ***

import cv2

cam = cv2.VideoCapture(0)  # kamerayı belirle

fourrc = cv2.VideoWriter_fourcc(*'XVID')  # görüntü çekiyorum ve bunun kodey  işlemi gerekiyor
# içine mp4 dosyası formatında olmuş oluyor.
# sonra boş bir şablon oluşturuyoruz ki aldığımız görüntüyü yazalım.

out = cv2.VideoWriter("dronegri.avi", fourrc, 30.0, (640, 480))
# 1.parametre dosya ismi.
# 2. parametre dosya uzantısı
# 3. parametre konumu
# 4. ise saniyedeki çerçeve sayısı ve çözünürlüğü

# görüntüyü açıyoruz.
while cam.isOpened():
    ret, frame = cam.read() # kameradan görüntü okudu.

    if not ret:
        print("kameradan görüntü alınamadı")
        break
    out.write(frame)  # boş şablon içine frame görüntüsünü kaydediyorum.

    cv2.imshow("kamera", frame) # kendi görüntümüzü gösteriyor.

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("videodan ayrıldınız")
        break

cam.release()
out.release()
cv2.destroyAllWindows()
