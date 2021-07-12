import subprocess
import smbus
import RPi.GPIO as GPIO
from time import sleep

bus = smbus.SMBus(1)

def adt7410():
    block = bus.read_i2c_block_data(0x48, 0x00, 2) #
    data = (block[0] << 8 | block[1]) >> 3
    if (data >= 4096):
        data -= 8192
    temp = data * 0.0625
    return temp

time_start, time_end, min, max = map(int, input().split())
    
try:
    sleep(time_start)
    while True:
        value = adt7410()
        if value >= min and value <= max:
            subprocess.call("curl http://172.16.2.236/iot/recv.php?temp=" + str(value), shell=True)
        sleep(time_end)
    
        
except KeyboardInterrupt:
    pass