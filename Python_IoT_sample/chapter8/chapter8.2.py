# ライブラリのインポート
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# ウインドウやフレームレートの設定
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

# カメラから映像を取得する処理
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    # フレームを表示
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # 次のフレームを表示
    rawCapture.truncate(0)

    # ［Q］キーでストップ
    if key == ord("q"):
        break

cv2.destroyAllWindows()