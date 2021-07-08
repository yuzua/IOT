import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup((20, 21), GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
led1 = GPIO.PWM(20, 50)
led2 = GPIO.PWM(21, 50)
led1.start(0)
led2.start(0)
flg = 0
i = 0
loop = [0]
        
try:
    while True:
        if i == 0:
            flg = 1
        elif i == 100:
            flg = 0
        led1.ChangeDutyCycle(i)
        led2.ChangeDutyCycle(100-i)
        sleep(0.01)
        if flg == 1:
            i += 1
        elif flg == 0:
            i -= 1
            

except KeyboardInterrupt:
    pass

GPIO.cleanup()