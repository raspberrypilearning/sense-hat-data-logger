##### Libraries #####
from sense_hat import SenseHat

##### Logging Settings #####


## Function to collect data from the sense hat and build a string
def get_sense_data():
    sense_data=[]
    
    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())
    
    yaw,pitch,roll = sense.get_orientation().values()        
    sense_data.extend([pitch,roll,yaw])

    mag_x,mag_y,mag_z = sense.get_compass_raw().values()
    sense_data.extend([mag_x,mag_y,mag_z])

    x,y,z = sense.get_accelerometer_raw().values()
    sense_data.extend([x,y,z])

    gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()
    sense_data.extend([gyro_x,gyro_y,gyro_z])
    
    sense_data.append(datetime.now())
     
    return sense_data

## Main Program
sense = SenseHat()

while True:
    sense_data = get_sense_data()
    print(sense_data)
    
    
