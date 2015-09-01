import time
from sense_hat import SenseHat

sense = SenseHat()

#temp = sense.get_temperature()
#hum = sense.get_humidity()
#pressure = sense.get_pressure()
yaw = sense.get_orientation()["pitch"]
print (yaw)

