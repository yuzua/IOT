import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
count, second = map(int, input().split())

try:
    for i in range(count):
        GPIO.output((20, 21), (GPIO.HIGH, GPIO.LOW))
        sleep(second)
        GPIO.output((20, 21), (GPIO.LOW, GPIO.HIGH))
        sleep(second)

except KeyboardInterrupt:
    pass

GPIO.cleanup()