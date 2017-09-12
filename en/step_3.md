## Getting data from the Sense HAT

First you can write a short script to get data from the Sense HAT and output it to the screen. Using the sensors, you can capture the following data:

- Temperature
- Humidity
- Pressure
- Orientation
- Acceleration
- Gyroscope
- Magnetic Field

- Attach your Sense HAT to you Raspberry Pi.

[[[rpi-sensehat-attach]]]

- Once your Sense HAT is attached, boot your Raspberry Pi.

- Open Idle on your Raspberry Pi and create a new file to work in.

[[[rpi-gui-idle-opening]]]

- To begin this project, your will need to import the code to control your Sense HAT and you will also need a module to fetch the data and time from the Raspberry Pi. Start by adding these two lines of code.

```python
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
```

- You're now going to create a function which will fetch **all** the sensor data from the Sense HAT and return it all as a list. Start by defining your function and creating an empty list.

```python
def get_sense_data():
	sense_data = []
```

- The section below shows you how to collect the data from the sensors. In each case you want to append this data to the list, and finish off the function by returning the `sense_data` list.

--- collapse ---
---
title: Reading all the sensors
---
- To read the environmental sensors you can use the following three code snippets.
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

- The only other data that you need is the date and time. To find this out you can use the following code:

```python
datetime.now()
```

- Now complete your function, add each individual bit of data to the `sense_data` list, and finish by returning the list.

[[[generic-python-append-list]]]

--- hints --- --- hint ---
To begin with fetch the environmental sensor readings within your function and add them to the list:
```python
def get_sense_data():
	sense_data = []
	sense_data.append(sense.get_temperature())
	sense_data.append(sense.get_pressure())
	sense_data.append(sense.get_humidity())

	return sense_data
```
--- /hint --- --- hint ---
- You can add the three orientation readings and add them to the list.
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
- Get the remaining sensor readings along with the data and time, by adding the following to your function:
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

- To finish off you can look at the data by printing out the list within an infinite loop. Add this to the end of your script and then run the code.

```python
while True:
	print(get_sense_data())
```
