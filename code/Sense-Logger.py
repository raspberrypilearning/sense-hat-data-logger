from datetime import datetime
from sense_hat import SenseHat
from collections import OrderedDict

sense = SenseHat()

sense_setting={"TEMPERATURE":True,"HUMIDITY":False,"PRESSURE":False,"ORIENTATION":True,"ACCELERATION":True,"COMPASS":True}
sense_data = OrderedDict()
filename = str(datetime.now()) + "-SenseLog.csv"

def get_sense_data():
    sense_data["Timestamp"] = datetime.now()
    #Get the temperature and round the figure to 2 decimal places
    if sense_setting["TEMPERATURE"]:
        sense_data["Temperature"]=round(sense.get_temperature(),2)
        

    #Get the humidity and round the figure to 2 decimal places
    if sense_setting["HUMIDITY"]:
        sense_data["Humidity"] = round(sense.get_humidity(),2)
        

    #Get the pressure and round the figure to 2 decimal places
    if sense_setting["PRESSURE"]:
        sense_data["Pressure"]=round(sense.get_pressure())
        

    #Get the yaw,pitch,roll data from the orientation sensor
    if sense_setting["ORIENTATION"]:
        yaw,pitch,roll = sense.get_orientation().values()
        #Round the yaw,pitch,roll data to 2 decimal places
        sense_data["Yaw"] = round(yaw,2)
        sense_data["Pitch"] = round(pitch,2)
        sense_data["Roll"] = round(roll,2)

    #Get the acceleration in the 3 axes and then round them to 2 decimal places
    if sense_setting["ACCELERATION"]:
        x,y,z = sense.get_accelerometer_raw().values()
        sense_data["X_Acceleration"] = round(x,2)
        sense_data["Y_Acceleration"] = round(y,2)
        sense_data["Z_Acceleration"] = round(z,2)

    #Get the compass data and round to 2 decimal places
    if sense_setting["COMPASS"]:
        sense_data["compass"] = round(sense.get_compass(),2)

     
    return sense_data

def write_header():
    headerstring = ",".join(str(bit) for bit in get_sense_data().keys())
    with open(filename,"w") as f:
        f.write(headerstring + "\n")


write_header()

while True:
    output_string = ""
    sense_data = get_sense_data()
    for item in sense_data:
        output_string = ",".join((output_string,str(sense_data[item])))

    print(output_string)

    with open(
        filename,"a") as f:
        f.write(output_string + "\n")


