import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
            
try:
    while True:
        GPIO.output((20, 21), (GPIO.HIGH, GPIO.LOW))
        sleep(0.5)
        GPIO.output((20, 21), (GPIO.LOW, GPIO.HIGH))
        sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

