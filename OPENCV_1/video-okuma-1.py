# * ***VİDEO OKUMA***

import cv2

cam = cv2.VideoCapture("drone.mp4")  # açacağım video ismini içine yazdım.

while cam.isOpened():
    ret, frame = cam.read()
    # RET ifadesi True ya da False  değerini döndürüyor.
    # True ya da False kameradan görüntünün okunup okunamadığı ile alakalı.
    # Frame : resim çerçevemizi veriyor. direk ordan okuyabiliyoruz.

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # güvenlik kodu koyuyoruz. ret ifadesi false gelirse döngünün içerisine girecek.
    if not ret:
        print("kameradan görüntü okunamıyor")
        break
    cv2.imshow("görüntü", frame)

    # videodan çıkabilmek için: 1 yazdık orası bekleme süresi
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("video kapatıldı.")
        break

cam.release() # kamerayı kapatmak için.

cv2.destroyAllWindow()
