
import time
import adafruit_adxl37x
import board
#import busio
#import adafruit_adxl34x
#import digitalio

#spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

#cs = digitalio.DigitalInOut(board.CE0)

i2c = board.I2C()
accelerometer = adafruit_adxl37x.ADXL375(i2c)
#accelerometer = adafruit_adxl37x.ADXL375(spi, cs)

#x = accel.x
#y = acel.y
#z = accel.z

#print(x,y,z)

while True:
	print("%f %f %f" %accelerometer.acceleration)
	time.sleep(0.2)
