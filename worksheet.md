# Building a Sense-HAT datalogger

During the Astro Pi mission a pair of Raspberry Pi with Sense HATs attached will be capturing and logging a range of data about life on board the International Space Station.

In this activity you will use a Raspberry Pi, Sense hat and some Python Code to create your own datalogging tool, which you can use to capture interesting data and perform experiments.

In preparation for this resource, attach your Sense HAT to your Raspberry Pi and install the software by following this [guide](https://www.raspberrypi.org/learning/astro-pi-guide/assemble.md).

## Getting data from the Sense-HAT

1. First we'll write a short script to get data from the Sense-HAT and output it to the screen, using the sensors we can capture the following data:

  - [Temperature](https://www.raspberrypi.org/learning/astro-pi-guide/sensors/temperature.md) (This can be read by two different sensors)
  - [Humidity](https://www.raspberrypi.org/learning/astro-pi-guide/sensors/humidity.md)
  - [Pressure](https://www.raspberrypi.org/learning/astro-pi-guide/sensors/pressure.md)
  - [Movement](https://www.raspberrypi.org/learning/astro-pi-guide/sensors/movement.md) (This is actually made up of 12 different sensor readings)

  To begin your script you need to boot you Raspberry Pi into desktop mode and run Idle for Python 3 from the menu. You can find it under the *Programming* section.

  Once Idle has loaded you will need to select **File** and then **New File** which will load a separate window in which you can write your code.

  ![Ilde3](images/idle3.png)

  The window on the right is where you should write your code and on the left is where the code will run. Let's begin by writing a program to collect data from the Sense-HAT sensors.

1. In you right hand window add the following lines of python code, the lines starting with a `#` symbol are called **comments** and are ignored by the computer. You should use comments here to break you code into 4 sections, this will help make it easier to build your program as it gets more complex.

  ![Code Snippet 1](images/code1.png)

  - The first section **Libraries** is where you will import code that will give your program extra abilities. The line `from sense_hat import SenseHat` allows your program to use the Sense-HAT hardware.
  - The section headed **Logging Settings** is where you will be able to control different features of your logger program.
  - The third section **Functions** will contain short "chunks" of reusable code that do a specific job such as writing the current data to a file.
  - The final section **Main Program** is the part of you code which uses each of the functions in the right sequence to run then whole program.

1. In order to get a data from the Sense-HAT you will need to write a function called **get_sense_data** which will check each sensor in turn and store the sensor data in a list. The function should be added to the **Functions** section.

  ```python
def get_sense_data():
    sense_data=[]

    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())
```
  The first line defines your function name, and the second sets up an empty **list** structure into which you will add your collected data.

  The next 4 lines get data from some of the sensors and add them (append) to the **sense_data** list.

  ```python
    yaw,pitch,roll = sense.get_orientation().values()
    sense_data.extend([pitch,roll,yaw])
```

  The rest of the sensors are a bit more complex as they each give 3 values back, in the lines above you are asking the Sense-HAT for the 3 orientation values (yaw,pitch,roll) and the second line extends the sense_data list by those three values.

  ```python
    mag_x,mag_y,mag_z = sense.get_compass_raw().values()
    sense_data.extend([mag_x,mag_y,mag_z])

    x,y,z = sense.get_accelerometer_raw().values()
    sense_data.extend([x,y,z])

    gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()
    sense_data.extend([gyro_x,gyro_y,gyro_z])


    sense_data.append(datetime.now())

    return sense_data
```
  The final part of the function adds three more sensor values (magnetometer, accelorometer and gyroscope), and then the current time. The final line of the function **returns** (or sends) the **sense_data** list to where the main program will ask for it.

1. Next you'll need to add some lines to your **Main Program** Section, this will need to do 2 things:
  - create a sense object, which represents the Sense-HAT
  - repeatedly **get_sense_data** from the sensors and display it.

  Add the following code to your **Main rogram**

  ```python
sense = SenseHat()

while True:
    sense_data = get_sense_data()
    print(sense_data)
```

  Your final program should look like this:
  ![Complete code](images/code2.png)

1. You can now test you logger by first of all saving it, by pressing **Ctrl+S** and giving you program a name such as `Sense_Logger_v1.py` once saved you can run the program by pressing **F5**. You should see lots of text scrolling past as shown below.

  ![Sense data being output to the console](images/run1.png)

  The highlighted section shows a single line of data bundled together into a list, you should be able to tell which sensor data is which.

  To stop the program running you can press **Ctrl+c** to cancel the execution.

## Writing the data to a file

The program you have produced so far is able to continually check the Sense-HAT sensors and write this data to the screen, however unless you're a very fast reader this is not very helpful.

What would be more useful is to write this data to a CSV file (comma seperated values) which you can examine once your logging program has finished. To do create this file you will need to:
- specify the filename for this file
- add a header row to the start of the file
- convert each list of data into a line in the file
- every so often write a batch of data out to the file

1. The first thing you need to do is to add 2 lines to your **Settings** section. these are:

  ```python
FILENAME = ""
WRITE_FREQUENCY = 50
```

  The first line here will be used to choose an filename for the outputted data and the second will set how often the program will write data out to the file. In this case it will collect 50 lines of data and then add these to the file in one go.

1. Next you will need to add a **log_data** function, which will convert the **sense_data** to a line of comma seperated values ready to be written to the file. The line of text will be added to a list called **batch data**, which will store the data until it is written to the file.

  Add the following code after the **Functions** heading and before the **get_sense_data** function.

  ```python
def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)
```

  The first line takes each value in the **sense_data** list and converts them to **strings** (text) and the joins them together with the `,` symbol. So a line like this:

  > [26.7224178314209, 25.068750381469727, 53.77205276489258, 1014.18017578125, 3.8002126669234286, 306.1720338870328, 0.3019065275890227, 71.13333892822266, 59.19926834106445, 39.75812911987305, 0.9896639585494995, 0.12468399852514267, -0.004147999919950962, -0.0013064055237919092, -0.0006561130285263062, -0.0011542239226400852, datetime.datetime(2015, 9, 23, 11, 53, 9, 267584)]

  gets converted to:

  > 26.7224178314209,25.068750381469727,53.77205276489258,1014.18017578125,3.8002126669234286,306.1720338870328,0.3019065275890227,71.13333892822266,59.19926834106445,39.75812911987305,0.9896639585494995,0.12468399852514267,-0.004147999919950962,-0.0013064055237919092,-0.0006561130285263062,-0.0011542239226400852,2015-09-23 11:53:09.267584

1. Another function you will need is the **file_setup** function which you're going to make create a list of headings that will be written to the file before any data. The function is shown below and needs to be added to your **Functions** section.


  ```python
def file_setup(filename):
    header  =["temp_h","temp_p","humidity","pressure","pitch","roll","yaw","mag_x","mag_y","mag_z","accel_x","accel_y","accel_z","gyro_x","gyro_y","gyro_z","timestamp"]

    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")
```

  This function is slightly differently to the previous as it needs an input in order to work, in this case an input the has been called `filename`. When the main program calls this function it must also give the function the name of the file to write to. If it where called like this `file_setup("output.csv")` the function whould create `output.csv`

  The function itself creates a list of header names called header. It then opens a file in write mode (w) which overwrite any previous data and refers to that file as f. whilst the file (f) is open it joins all the list headings together using commas and writes that line to the file.

1. The two functions and the settings you added now need to be used in the main program.

  Straight after the lines that read:

  ```python
##### Main Program #####
sense = SenseHat()
```

  add the following:

  ```python
batch_data= []

if FLIENAME == "":
    filename = "SenseLog-"+str(datetime.now())+".csv"
else:
    filename = FILEAME+"-"+str(datetime.now())+".csv"

file_setup(filename)
```

  The first line here creates and empty list that the program will keep adding sense_data lines to until it reaches 50 (or whatever value is set by WRITE_FREQUENCY).

  The if/else block checks whether a FILENAME has been set, if it hasn't then the default of "SenseLog" is used. The current date and time is added to the filename.

  Finally the **file_setup** functions is called and given the filename that was decided upon in the previous if / else block.

1. The last step is to change some of the logic inside the `while True:` loop.
  - You need to make it collect **sense_data**
  - Then use the **log_data** function to convert the sense_data into csv form and add the the current **batch_data**.
  - Once the data is logged the program checks whether the size of **batch_data** exceedds the WRITE_FREQUENCY setting, if so the data is written to a file and **batch_data** is reset.

  Your `while True:` loop should be updated to look like this:

  ```python
while True:
    sense_data = get_sense_data()
    log_data()

    if len(batch_data) >= WRITE_FREQUENCY:
        print("Writing to file..")
        with open(filename,"a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []
```

  - The line `print("Writing to file..")` is optional, but it will show whenever data is being written.
  - The line `with open(filename,"a") as f:` opens the file in **append** mode which adds the data at the end point of the file rather than overwriting.

  You can check your code against a full code listing [here](code/Sense_Logger_v2.py).

  When you running the program you should simply see the messages saying `Writing to file..` every so often.

  ![Writing to a file](images/run2.png)

  You can stop logging by pressing **Ctrl+c**

## Starting you datalogger on boot.
It's quite likely that you will not want to have a screen, keyboard and mouse handy everytime you want to log data. A handy way to avoid this is to have you program run whenever your Raspberry Pi boots up.
To do this you will first need to open a terminal window like the one below.

## Collect your data
The data logger created in this activity will log data from all the sensor as often as it can, there are a number of things you could try next.
- Conduct an experiment the should involve a change in on of conditions measure and collect data You could:

## What's Next
