###### Import Libraries ######
from sense_hat import SenseHat
from datetime import datetime

###### Settings ######
TEMPERATURE=True
HUMIDITY=True
PRESSURE=True
ORIENTATION=True
ACCELERATION=True
MAG=True
GYRO=True
BASENAME = ""


###### Functions ######
def file_setup(filename):
    header =[]
    if TEMPERATURE:
        header.extend(["temp_h","temp_p"])
    if HUMIDITY:
        header.append("humidity")
    if PRESSURE:
        header.append("pressure")
    if ORIENTATION:
        header.extend(["pitch","roll","yaw"])
    if ACCELERATION:
        header.extend(["mag_x","mag_y","mag_z"])
    if MAG:
        header.extend(["accel_x","accel_y","accel_z"])
    if GYRO:
        header.extend(["gyro_x","gyro_y","gyro_z"])
    header.append("timestamp")

    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")

def get_sense_data():   
  sense_data=[]
    
  if TEMPERATURE:
      sense_data.extend([sense.get_temperature_from_humidity(),sense.get_temperature_from_pressure()])
      
  if HUMIDITY:
      sense_data.append(sense.get_humidity())
   
  if PRESSURE:
      sense_data.append(sense.get_pressure())
      
  if ORIENTATION:
      yaw,pitch,roll = sense.get_orientation().values()        
      sense_data.extend([pitch,roll,yaw])

  if MAG:
      mag_x,mag_y,mag_z = sense.get_compass_raw().values()
      sense_data.extend([mag_x,mag_y,mag_z])

  if ACCELERATION:
      x,y,z = sense.get_accelerometer_raw().values()
      sense_data.extend([x,y,z])

  if GYRO:
      gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()
      sense_data.extend([gyro_x,gyro_y,gyro_z])
  
  sense_data.append(datetime.now())
   
  return sense_data    

###### Main Program ######
sense = SenseHat()
filename = "SenseLog-" + str(datetime.now()) + ".csv"
file_setup(filename)

while True:
  sense_data = get_sense_data()
  output_string = ",".join(str(value) for value in sense_data)
  print(output_string)

  with open(filename,"a") as f:
    f.write(output_string + "\n")
