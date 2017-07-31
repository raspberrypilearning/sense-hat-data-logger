## Logging data at a fixed interval

Currently the data logger you have written will collect data as fast as it can (multiple times a second). This is great for many situations, particularly when the environment is changing rapidly. However, you may sometimes want to collect data less frequently, when change is more gradual. To make this work, you will need to develop your code in a few ways.

  - Add some libraries to your code to enable extra functionality.
  - Set the interval between logging events
  - Write a function which will be run at the start of the program, before the loop, to log data and then wait for the specified interval.
  - Amend part of the code inside the `while` loop so that the loop skips logging there if an interval has been set.

- The first step is to import the two library elements at the top of your code:
  - The **sleep** function from the **time** library allows you code to pause between lines of code.
  - A **Thread**, from the **threading** library allows a separate chunk of code to be run at the same time as another. We need one thread to continually check the sensors, and another to log the data every so many seconds.

  Your import section should now look like this:

    ```python3
    from datetime import datetime
    from sense_hat import SenseHat
    from time import sleep
    from threading import Thread
    ```

- With these libraries imported you can now add a setting to your setting section which will set the DELAY between logging. If you set it to zero the program will behave as it has so far and log as often as possible. Anything higher than zero will use a separate `timed_log` function which you'll write in the set step.

  Add the line `DELAY=5` to you settings section for a five second delay, as shown below.

    ```python3
    ##### Logging Settings #####
    FILENAME = ""
    WRITE_FREQUENCY = 100
    TEMP_H=True
    TEMP_P=False
    HUMIDITY=True
    PRESSURE=True
    ORIENTATION=True
    ACCELERATION=True
    MAG=True
    GYRO=True
    DELAY=5
    ```

2. You'll now need to add a function for handling the `timed_log`, this will run in the background and call `log_data` every 5 seconds. Add the following definition to your `functions` section.

    ```python3
    def timed_log():
        while True:
          log_data()
          sleep(DELAY)
    ```

3. Now that your imports, settings, and functions have been added you'll now need to adjust your main program to include them.

  First add these two lines above the `while True:` line:

  ```python3
  if DELAY > 0:
      sense_data = get_sense_data()
      Thread(target= timed_log).start()
  ```

  This checks whether a delay has been set and, if so, starts a separate thread which launches the `timed_log` function in the background.

4. The final step is to adjust a line inside the `while True:` loop so that if a delay is set then the loop doesn't log any data and simply handles the writing out of data to the file. Find the line that says `log_data` and replace it with:

    ```python3
    if DELAY == 0:
      log_data()
    ```

  This only logs data inside the while loop if the value of DELAY is 0.

  With these changes made you should be able specify the delay between logging events and log data at whatever interval you want. You can see the full code [here](resources/Sense_Logger_v4.py)

