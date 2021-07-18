import RPi.GPIO as GPIO
from time import sleep

# 初期化
GPIO.setmode(GPIO.BCM) # ピン番号ではなくGPIOの番号で指定
GPIO.setup(20, GPIO.OUT) # GPIO 20を出力として指定
GPIO.setup(21, GPIO.OUT) # GPIO 21を出力として指定

# 繰り返し処理
try:
    for count in range(5):
         GPIO.output(20, GPIO.HIGH) # GPIO 20をHIGHに変更
         sleep(1.0) # 1秒回転
         GPIO.output(20, GPIO.LOW) # GPIO 20をLOWに変更
         sleep(1.0) # 1秒停止
         GPIO.output(21, GPIO.HIGH) # GPIO 21をHIGHに変更
         sleep(1.0) # 1秒回転
         GPIO.output(21, GPIO.LOW) # GPIO 21をLOWに変更
         sleep(1.0) # 1秒停止

except KeyboardInterrupt:
    pass

# GPIOをリセット
GPIO.cleanup()
