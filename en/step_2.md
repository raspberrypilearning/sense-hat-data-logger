## Getting data from the Sense HAT

Using the Sense HAT, you can capture the data from the following sensors:

- Temperature sensor
- Humidity sensor
- Pressure sensor
- Orientation sensor
- Acceleration sensor
- Gyroscope
- Magnetic field sensor
- Colour sensor (V2 Sense HAT only)

First, write a short script to get readings from the HAT's sensors and output them to the screen. 

--- task ---

Attach your Sense HAT to you Raspberry Pi.

[[[rpi-sensehat-attach]]]

--- /task ---

--- task ---

- Once your Sense HAT is attached, boot up your Pi.

--- /task ---

--- task ---

- Open Thonny, and create a new file to work in.

--- /task ---

--- task ---

To begin this script, your will need to import the Python modules to control your Sense HAT and to fetch the data and time from the Raspberry Pi. Start by adding these three lines of code:

--- code ---
---
language: python
filename: main.py
line_numbers: 
line_number_start: 
highlight_lines: 
---
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

--- /code ---

--- /task ---

--- task ---

If you have a version 2 Sense HAT then you need to set up the colour sensor with the following extra lines of code.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1 
highlight_lines: 5-6
---
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
sense.color.gain = 60
sense.color.integration_cycles = 64

--- /code ---

--- /task ---

--- task ---

Create a function which will fetch **all** the sensor data and return it all as a list. Start by defining your function and creating an empty list.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
highlight_lines: 
---
def get_sense_data():
	sense_data = []
--- /code ---

--- /task ---

The tasks below shows you how to collect the data from the different sensors. In each case you want to append the data to the `sense_data`list. Finish the function by returning the `sense_data` list.

--- task ---

You can read all the sensors on the Sense HAT, and then append the data to your list.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
highlight_lines: 11-40
---
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
--- /code ---

--- /task ---

--- task ---

Finish off your data capture by adding the current data and time to the list.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 41 
highlight_lines: 41-43
---
    # Get the date and time
    sense_data.append(datetime.now())

--- /code ---

--- /task ---

--- task ---

The function should return the `sense_data` list at the end.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 41 
highlight_lines: 44
---
    # Get the date and time
    sense_data.append(datetime.now())

    return sense_data
--- /code ---

--- /task ---



--- task ---

To finish off, you can look at the data by printing out the list within an infinite loop. Add the following to the end of your script, and then save and run the code.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 46
highlight_lines: 
---
while True:
	print(get_sense_data())
--- /code ---

--- /task ---

You should see a continuous stream of data in the the shell, with each line looking something like this:

```
[38.94975280761719, 1012.20166015625, 32.560699462890625, 17, 10, 11, 20, 144.1204202422324, 12.432924190508864, 355.4826729655122, -33.784427642822266, -23.137866973876953, 3.40659761428833, -0.19746851921081543, -0.054034601897001266, 0.9491991996765137, -0.014246762730181217, 0.009623102843761444, -0.010858062654733658, datetime.datetime(2022, 7, 25, 14, 26, 51, 341250)]
```
