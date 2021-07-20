# ライブラリのインポート
import cv2

# 画像の読み込み
image = cv2.imread("/home/pi/Desktop/opencv/cat1.jpg")

# カスケードファイルの指定
casceade_file = "/home/pi/Desktop/opencv/haarcascade_frontalcatface.xml"

# カスケードファイルの読み込み
cascade = cv2.CascadeClassifier(casceade_file)

# 矩形に変更して表示をリスト化
face_list = cascade.detectMultiScale(image)

# 顔を囲う枠の色を指定
color = (0, 0, 255)

# 顔を認識した箇所に枠を描画する処理
if len(face_list) > 0:
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=2)
else:
    print("顔が認識できませんでした。")

# 顔認識した画像を表示する処理
cv2.imshow('Frame',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
