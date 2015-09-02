from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()

def get_sense_data():
    #Get the temperature and round the figure to 2 decimal places
    temperature = round(sense.get_temperature(),2)

    #Get the humidity and round the figure to 2 decimal places
    humidity = round(sense.get_humidity(),2)

    #Get the pressure and round the figure to 2 decimal places
    pressure = round(sense.get_pressure())

    #Get the yaw,pitch,roll data from the orientation sensor
    yaw,pitch,roll = sense.get_orientation().values()

    #Round the yaw,pitch,roll data to 2 decimal places
    yaw = round(yaw,2)
    pitch = round(pitch,2)
    roll = round(pitch,2)

    #Get the acceleration in the 3 axes and then round them to 2 decimal places
    x,y,z = sense.get_accelerometer_raw().values()
    x = round(x,2)
    y = round(y,2)
    z = round(z,2)

    #Get the compass data and round to 2 decimal places
    compass = round(sense.get_compass(),2)

    return datetime.now(),temperature,humidity,pressure,yaw,pitch,roll,x,y,z,compass

while True:
    sensor_values = ",".join(str(bit) for bit in get_sense_data())
    print(sensor_values)
    with open("sense-data.csv","a") as f:
        f.write(sensor_values + "\n")

