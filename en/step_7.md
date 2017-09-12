## Recording at specific time intervals

At the moment your script records data as quickly as it possibly can. This is very useful for some experiments, but you may prefer to record data once per second, or even less.

Normally in such situations you would use a `sleep()` function to pause the script. This can result in inaccurate readings from some of the Sense HAT's orientation sensors though, which need to be regularly polled.

To get around this, you can use `timedelta` to check the time difference between two readings.

[[[generic-python-timedelta]]]

To use this to write data, every one second for example, you would need to do the following.
	- Create a timestamp at the start of your script, set to `datetime.now()`
	- Create a variable called `delay` to store the number of seconds interval between data being written to the CSV
	- Within your infinite loop, if the difference between the `timestamp` and the time returned by your function, is greater than the delay, data can be written and the timestamp reset.
	
- Have a go at adding a one second delay to your data writing intervals, and use the hints below if you get stuck.

--- hints --- --- hint ---
Start by setting the `timestamp` and `delay` variables near the top of your script

```python
timestamp = datetime.now()
delay = 1
```
--- /hint --- --- hint ---
The time the reading was taken is the **last** item in the `data` list. So you can now calculate the time difference.

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
		timestamp = datetime.now()
		data_writer.writerow(data)
```
--- /hint --- --- /hints ---

- Have a go at trying different values for the `delay` each time you run your script.

- Can you set a `microsecond` delay?
