import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
            
try:
    while True:
        GPIO.output(12, GPIO.HIGH)
        sleep(1.0)
        GPIO.output(12, GPIO.LOW)
        sleep(1.0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()