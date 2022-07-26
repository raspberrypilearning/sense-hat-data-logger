## Recording at specific time intervals

At the moment your script records data as quickly as it possibly can. This is very useful for some experiments, but you may prefer to record data once per second, or even less frequently.

Normally you would use a `sleep()` function to pause the script. This can cause inaccurate readings from some of the IMU sensor. Instead you can use `timedelta` to check the time difference between two readings.

--- task ---

At the top of your program, set the length of delay between readings in seconds, and get the current date and time.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1 
highlight_lines: 9-10
---
from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()
sense.color.gain = 60
sense.color.integration_cycles = 64

timestamp = datetime.now()
delay = 1
--- /code ---

--- /task ---

--- task ---

Within your `while` loop, you can calculate the difference in time, between the current time and the time stored in the `data` list.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 58
highlight_lines: 60
---
    while True:
	    data = get_sense_data()
	    time_difference = data[-1] - timestamp
--- /code ---

--- /task ---

--- task ---

Lastly, if the `time_difference` is greater than the delay that you have set, the `data` can be written to the file.

--- code ---
---
language: python
filename: main
line_numbers: true
line_number_start:58 
highlight_lines: 61-63
---
    while True:
        data = get_sense_data()
        time_difference = data[-1] - timestamp
        if time_difference.seconds > delay:
            data_writer.writerow(data)
            timestamp = datetime.now()
--- /code ---

--- /task ---

--- task ---

Run your program for a few seconds, then stop the program and have a look at the `.csv` file. You should see that the file is only being written to periodically. You can adjust the delay time you have set, to write more frequently or less frequently.

```python
temp,pres,hum,red,green,blue,clear,yaw,pitch,roll,mag_x,mag_y,mag_z,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z,datetime
36.108428955078125,1024.423095703125,32.416011810302734,49,38,38,90,138.01520101110313,12.227523326693655,352.8891865315218,-29.801549911499023,-25.660537719726562,5.958069324493408,-0.20684826374053955,-0.11651210486888885,0.9470059275627136,-0.002123238518834114,0.0003891065716743469,-0.0002552233636379242,2022-07-26 11:27:05.983233
36.23430633544922,1024.432373046875,33.37968826293945,49,38,38,90,137.72729487720875,12.181723493214136,352.9463897927074,-29.705188751220703,-25.5445613861084,6.508992671966553,-0.20660144090652466,-0.11795946210622787,0.9484680891036987,0.0003636479377746582,0.0006903782486915588,-3.945082426071167e-06,2022-07-26 11:27:08.091969
```

--- /task ---

