## Writing the data to a file

The program you have produced so far is able to continually check the Sense HAT sensors and write this data to the screen, however, unless you're a very fast reader this is not very helpful.

What would be more useful would be to write this data to a CSV (comma separated values) file, which you can examine once your logging program has finished. To create this file you will need to do the following:
  - specify the filename for this file
  - add a header row to the start of the file
  - periodically write a batch of data out to the file

- You can start by learning how to write list data to a csv in Python.

[[[generic-python-writing-csv]]]

- Now you can alter your code to continuously write the data from your `get_sense_data()` function to a CSV file. Here's one way to proceed:
  1. Before your loop starts, open a `csv` file and create your writer
  1. Within your loop write the returned data from the function to the file.
  
--- hints --- --- hint ---
Import the `writer` class and then open the file and create a `writer` object
```python
from csv import writer ## this line is at the top of your code

## this comes after your get_sense_data() function
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
	
	while True:
```
--- /hint --- --- hint ---
Create a variable to hold the data from the function call
```python
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
	
	while True:
		data = get_sense_data()
```
--- /hint --- --- hint ---
Now just write that data to the file
```python
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
	
	while True:
		data = get_sense_data()
		data_writer.writerow(data)
```
--- /hint --- --- /hints ---
