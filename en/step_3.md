## Getting data from the Sense HAT

Using the Sense HAT, you can capture the data from the following sensors:

- Temperature sensor
- Humidity sensor
- Pressure sensor
- Orientation sensor
- Acceleration sensor
- Gyroscope
- Magnetic field sensor

First, write a short script to get readings from the HAT's sensors and output them to the screen. 

- Attach your Sense HAT to you Raspberry Pi.

[[[rpi-sensehat-attach]]]

- Once your Sense HAT is attached, boot up your Pi.

- Open IDLE, and create a new file to work in.

[[[rpi-gui-idle-opening]]]

- To begin this script, your will need to import the Python modules to control your Sense HAT and to fetch the data and time from the Raspberry Pi. Start by adding these three lines of code:


```python
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
```

- Now you're going to create a function which will fetch **all** the sensor data and return it all as a list. Start by defining your function and creating an empty list.

```python
def get_sense_data():
	sense_data = []
```

- The section below shows you how to collect the data from the different sensors. In each case you want to append the data to the `sense_data`list. Finish the function by returning the `sense_data` list.

--- collapse ---
---
title: Reading all the sensors
---
- To read the environmental sensors, you can use the following three commands:
```python
sense.get_temperature()
sense.get_pressure()
sense.get_humidity()
```
- To read the orientation of the Sense HAT, use the following three lines:
```
orientation = sense.get_orientation()
orientation["yaw"]
orientation["pitch"]
orientation["roll"]
```
- You can get the raw compass readings using the following code:
```python
mag = sense.get_compass_raw()
mag["x"]
mag["y"]
mag["z"]
```
- You can get the raw accelerometer reading using the following code:
```python
acc = sense.get_accelerometer_raw()
acc["x"]
acc["y"]
acc["z"]
```
- Finally you can get the raw gyroscope readings using the following code:
```python
gyro = sense.get_gyroscope_raw()
gyro["x"]
gyro["y"]
gyro["z"]
```
--- /collapse ---

- The only other data that you need is the date and time. To find this out, you can use the following code:

```python
datetime.now()
```

[[[generic-python-append-list]]]

--- hints --- --- hint ---
To begin with, fetch the environmental sensor readings within your function and add them to the list:
```python
def get_sense_data():
	sense_data = []
	sense_data.append(sense.get_temperature())
	sense_data.append(sense.get_pressure())
	sense_data.append(sense.get_humidity())

	return sense_data
```
--- /hint --- --- hint ---
- You can get the three orientation readings and add them to the list.
```python
def get_sense_data():
	sense_data = []
	sense_data.append(sense.get_temperature())
	sense_data.append(sense.get_pressure())
	sense_data.append(sense.get_humidity())

	orientation = sense.get_orientation()
	sense_data.append(orientation["yaw"])
	sense_data.append(orientation["pitch"])
	sense_data.append(orientation["roll"])
	
	return sense_data
```
--- /hint --- --- hint ---

- Get the remaining sensor readings along with the data and time by adding the following lines to your function:
```python
mag = sense.get_compass_raw()
sense_data.append(mag["x"])
sense_data.append(mag["y"])
sense_data.append(mag["z"])

acc = sense.get_accelerometer_raw()
sense_data.append(acc["x"])
sense_data.append(acc["y"])
sense_data.append(acc["z"])

gyro = sense.get_gyroscope_raw()
sense_data.append(gyro["x"])
sense_data.append(gyro["y"])
sense_data.append(gyro["z"])

sense_data.append(datetime.now())
```
--- /hint --- --- /hints ---

- To finish off, you can look at the data by printing out the list within an infinite loop. Add the following to the end of your script, and then save and run the code.

```python
while True:
	print(get_sense_data())
```

- You should see a continuous stream of data in the the shell, with each line looking something like this:

```
[26.7224178314209, 25.068750381469727, 53.77205276489258, 1014.18017578125, 3.8002126669234286, 306.1720338870328, 0.3019065275890227, 71.13333892822266, 59.19926834106445, 39.75812911987305, 0.9896639585494995, 0.12468399852514267, -0.004147999919950962, -0.0013064055237919092, -0.0006561130285263062, -0.0011542239226400852, datetime.datetime(2015, 9, 23, 11, 53, 9, 267584)]
```
