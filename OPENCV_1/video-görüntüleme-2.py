import cv2

# bir videoda örnek olarak saniyede 60 resim var. art arda hareket edince video oluyor.

cam = cv2.VideoCapture(0)  # kamera ismi tanımlandı. içine pc'nin dahili kamerasını kullandığım için 0 girdim.

print(cam.get(3))
print(cam.get(4))

cam.set(3, 320)  # genişlik
cam.set(4, 240)  # uzunluk
 # set al demek. get değiştirmek için.
print(cam.get(3))
print(cam.get(4))

# kamerayı kontrol için
# not dedik çünkü false derse koşulun içine girecek.
if not cam.isOpened():
    print("kamera tanınmadı")
    exit()  # tüm kodların çıkması için

"""
döngü başlatıyoruz. kameradan resim çekicez.
kamerayı oku dediğimizde bize iki değer döndürüyor.
biri ret, diğeri frame 
ret: True ya da False değeri döndürüyor, yani görüntünün okunup okunamadığıyla alakalı
frame: resmin çerçevesini veriyor, direk ordan okuyabiliyoruz.
sonra bir güvenlik kodu koymalıyım. ardından aldığım görüntüyü frame gösteriyorum."""

while True:
    ret, frame = cam.read()

    # rengini değiştirmek için
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # burada koruma kodu yazdık
    if not ret:
        print("kameradan görüntü okunamıyor")
        break  # döngüden çıkması için

    cv2.imshow("kamera", frame)

    # 1 yazdığım yere daha büyük bir sayı yazarsam bekleme süresi olacağı için video yavaşlatılmış gibi gözükecek.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("görüntü sonlandırıldı.")
        break
# koddan çıkacağı zaman ise
cam.release()  # kamerayı kapattık

cv2.destroyAllWindow() # penceryi kapattık

