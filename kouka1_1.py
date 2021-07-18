import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
number, count, time = map(int, input().split())
GPIO.setup(number, GPIO.OUT)
            
try:
    for i in range(count):
        GPIO.output(number, GPIO.HIGH)
        sleep(time)
        GPIO.output(number, GPIO.LOW)
        sleep(time)

except KeyboardInterrupt:
    pass

GPIO.cleanup()