import smbus
from time import sleep

bus = smbus.SMBus(1)

def adt7410():
    block = bus.read_i2c_block_data(0x48, 0x00, 2) #
    data = (block[0] << 8 | block[1]) >> 3
    if (data >= 4096):
        data -= 8192
    temp = data * 0.0625
    return temp

min, max = map(float, input().spliit())
    
try:
    while True:
        value = adt7410()
        if value >= min and value <= max:
            print(value)
        sleep(0.5)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
