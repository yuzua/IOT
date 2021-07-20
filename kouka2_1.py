import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
led = GPIO.PWM(21, 50)
led.start(0)

GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)

count, time = map(int, input().split())

try:
    for i in range(count):
        led.ChangeDutyCycle(30)
        sleep(time)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
