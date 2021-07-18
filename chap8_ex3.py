# ライブラリのインポート
import cv2

# 画像の読み込み
im_file = input('画像ファイル名 = ')
image = cv2.imread(im_file)

# カスケードファイルの指定 
# 顔（正面）
cascade_name_face = "haarcascade_frontalface_alt.xml"
# 上半身
cascade_name_eye = "haarcascade_eye.xml"

# カスケードファイルの読み込み
# 顔（正面）
cascade_face = cv2.CascadeClassifier(cascade_name_face)
# 全身
cascade_eye = cv2.CascadeClassifier(cascade_name_eye)

# 矩形に変更して表示をリスト化
# 顔（正面）
face_list = cascade_face.detectMultiScale(image)
# 上半身
eye_list = cascade_eye.detectMultiScale(image)

# 顔を囲う枠の色を指定
color_face = (0, 0, 255)
# 上半身を囲う枠の色を指定
color_eye = (255, 0, 0)

# 顔を認識した箇所に枠を描画する処理
if len(face_list) > 0:
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color_face, thickness=2)
else:
    print("顔が認識できませんでした。")

# 目を認識した箇所に枠を描画する処理
if len(eye_list) > 0:
    for eye in eye_list:
      x, y, w, h = eye
      cv2.rectangle(image, (x, y), (x+w, y+h), color_eye, thickness=2)
else:
    print("目が認識できませんでした。")

# 顔認識した画像を表示する処理
cv2.imshow('Frame',image)
cv2.waitKey(0)
cv2.destroyAllWindows()