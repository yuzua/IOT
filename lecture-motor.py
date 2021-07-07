import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
led = GPIO.PWM(21, 50)
led.start(0)

try:
    while True:
        led.ChangeDutyCycle(25)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
