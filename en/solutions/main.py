from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()
sense.color.gain = 60
sense.color.integration_cycles = 64

timestamp = datetime.now()
delay = 1

def get_sense_data():
    sense_data = []
    # Get environmental data
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())
    # Get colour sensor data (version 2 Sense HAT only)
    red, green, blue, clear = sense.colour.colour
    sense_data.append(red)
    sense_data.append(green)
    sense_data.append(blue)
    sense_data.append(clear)
    # Get oriendation dara
    orientation = sense.get_orientation()
    sense_data.append(orientation["yaw"])
    sense_data.append(orientation["pitch"])
    sense_data.append(orientation["roll"])
    # Get compass data
    mag = sense.get_compass_raw()
    sense_data.append(mag["x"])
    sense_data.append(mag["y"])
    sense_data.append(mag["z"])
    # Get accerometer data
    acc = sense.get_accelerometer_raw()
    sense_data.append(acc["x"])
    sense_data.append(acc["y"])
    sense_data.append(acc["z"])
    #Get gyroscop data
    gyro = sense.get_gyroscope_raw()
    sense_data.append(gyro["x"])
    sense_data.append(gyro["y"])
    sense_data.append(gyro["z"])
    # Get date and time
    sense_data.append(datetime.now())
    return sense_data


with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp', 'pres', 'hum',
                          'red', 'green', 'blue', 'clear', #only for Sense HAT version 2
                          'yaw', 'pitch', 'roll',
                          'mag_x', 'mag_y', 'mag_z',
                          'acc_x', 'acc_y', 'acc_z',
                          'gyro_x', 'gyro_y', 'gyro_z', 
                          'datetime'])
    while True:
        data = get_sense_data()
        time_difference = data[-1] - timestamp
        if time_difference.seconds > delay:
            data_writer.writerow(data)
            timestamp = datetime.now()
