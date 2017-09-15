## Recording at specific time intervals

At the moment your script records data as quickly as it possibly can. This is very useful for some experiments, but you may prefer to record data once per second, or even less frequently.

Normally in such situations you would use a `sleep()` function to pause the script. However, this can result in inaccurate readings from some of the Sense HAT's orientation sensors, which need to be regularly polled.

To get around this, you can use `timedelta` to check the time difference between two readings.

[[[generic-python-datetime-timedelta]]]

To use this approach to collect data you would need to do the following:
	- At the start of your script, create a `timestamp` variable set to `datetime.now()`
	- Decide how long you want the interval between data records to be (in seconds), and create a variable called `delay` to store that number
	- Within your infinite loop, if the difference between the `timestamp` and the time of the reading returned by your `get_sense_data()` function is greater than `delay`, write data and reset `timestamp`
	
- Have a go at adding a one-second delay to your data writing intervals, and use the hints below if you get stuck.

--- hints --- --- hint ---
Start by setting the `timestamp` and `delay` variables near the top of your script:

```python
timestamp = datetime.now()
delay = 1
```
--- /hint --- --- hint ---
The time the reading was taken is the **last** item in the list created by your `get_sense_data()` function, so you can now calculate the time difference like this:

```python
while True:
	data = get_sense_data()
	dt = data[-1] - timestamp
```
--- /hint --- --- hint ---
If that `dt` variable is greater than the `delay` you specified, then the data can be written and `timestamp` can be reset.
```python
while True:
	data = get_sense_data()
	dt = data[-1] - timestamp
	if dt.seconds > delay:
		data_writer.writerow(data)
		timestamp = datetime.now()
```
--- /hint --- --- /hints ---

- Have a go at trying different values for the `delay` each time you run your script.

- Can you set a `microsecond` delay?
