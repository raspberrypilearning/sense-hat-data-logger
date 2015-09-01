import time
from sense_hat import SenseHat

sense = SenseHat()

while True:
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    pressure = sense.get_pressure()
    yaw,pitch,roll = sense.get_orientation().values()
    x,y,z = sense.get_accelerometer_raw()
    print (temp,hum,pressure,yaw,pitch,roll)

    time.sleep(0.2)

