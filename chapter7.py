import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup((20, 21), GPIO.OUT)

try:
    while True:
        GPIO.output(20, GPIO.HIGH)
        sleep(5.0)
        GPIO.output(20, GPIO.LOW)
        sleep(5.0)
        GPIO.output(21, GPIO.HIGH)
        sleep(5.0)
        GPIO.output(21, GPIO.LOW)
        sleep(5.0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()