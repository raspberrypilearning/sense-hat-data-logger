# Building a Sense-HAT datalogger (part 2)

In the first part of this activitiy you build a data logger that logs all data from the Sense-HAT, as often as it can and starts when your Raspberry Pi starts. If you follow this worksheet you'll be able to extend your data logger to add some optional features such as:

  - Being able to select which data your program logs from the Sense-HAT
  - Adding the ability to log data at a fixed interval (every 10 seconds for example)
  - Being able to start and stop logging using the Sense-HAT joystick.

## Optionally choosing which pieces of data to log.
Sometimes you may not want to log data from every sensor on the Sense-HAT depending on what your investigating. To just capture some of the sensor data you need to make a few changes to your code.

  - You'll need to add some variables to our settings section so that you can specify which data to log.
  - Your file_setup function will need to be adapted in order to add only the headers you want.
  - You will have to adapt your get_sense_data function to only capture the required data.

1. For each piece of data you want to log you will need a **Boolean** (one that can either be *True* or *False*) variable to your settings section. In the code below these have been capitalised to make them stand out and for now have been set to True.

  ```python3
  ## Logging Settings
  TEMP_H=True
  TEMP_P=False
  HUMIDITY=True
  PRESSURE=True
  ORIENTATION=True
  ACCELERATION=True
  MAG=True
  GYRO=True

  BASENAME = "Fall"
  WRITE_FREQUENCY = 1
  ```

1. You then need to update your **file_setup** function to only append the headings that are set to `True`

  ```python3
  def file_setup(filename):
      header =[]
      if TEMP_H:
          header.append("temp_h")
      if TEMP_P:
          header.append("temp_p")
      if HUMIDITY:
          header.append("humidity")
      if PRESSURE:
          header.append("pressure")
      if ORIENTATION:
          header.extend(["pitch","roll","yaw"])
      if MAG:
          header.extend(["mag_x","mag_y","mag_z"])
      if ACCELERATION:
          header.extend(["accel_x","accel_y","accel_z"])
      if GYRO:
          header.extend(["gyro_x","gyro_y","gyro_z"])
      header.append("timestamp")

      with open(filename,"w") as f:
          f.write(",".join(str(value) for value in header)+ "\n")
  ```

    In this new version of the function you start with an empty list for the header
    ```python3
    header =[]
    ```
    Then each setting is checked and if that setting is set to `True` then the related data is either appended (if it's a item).
    ```python3
    if TEMP_H:
        header.append("temp_h")
    ```
    Or extended if it's multiple items of data.
    ```python3
    if ORIENTATION:
        header.extend(["pitch","roll","yaw"])
    ```

1. The final change to make is to the **get_sense_data** function which is a similar change to the one made to the **file_setup** function.
  Your code which did look like this:

  ```python3
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
    ```
    Will need to be adapted to have each piece of Sense-HAT data wrapped in a `if` statement which will check whether the corresponding setting is set to `True`

    ```python3
    def get_sense_data():
        sense_data=[]

        if TEMP_H:
            sense_data.append(sense.get_temperature_from_humidity())

        if TEMP_P:
            sense_data.append(sense.get_temperature_from_pressure())

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
    ```

    You can find a complete code listing [here](code/Sense_Logger_v3.py).

    Now when you run your code you should be able to switch the collection of different pieces of data **on/off** by changing the settings at the top to **True/Flase**

    ## Logging data at a fixed interval
