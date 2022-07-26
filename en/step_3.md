## Writing the data to a file

The program you have produced so far is able to continually check the Sense HAT sensors and write this data to the screen.

It would be more useful to write this data to a Comma Separated Values (CSV) file, which you can examine once your logging program has finished. To create this file, you will need to do the following:
  - Create the file
  - Add a header row for each sensor reading
  - Write the data to the file

--- task ---

Import the `csv` `writer` class.

--- code ---
---
language: python
filename: main.py
line_numbers: 1
line_number_start: 
highlight_lines: 3
---
from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()
--- /code ---

--- /task ---

--- task ---

Remove your current `while True` loop. Replace this with these lines to open a new `.csv` file and let you write to the file.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 47
highlight_lines: 47-48
---
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
--- /code ---

--- /task ---

--- task ---

Create a variable to hold the data from the function call within a new `while True` loop, and write that data to the new file.

--- code ---
---
language: python
filename: main
line_numbers: true
line_number_start: 47
highlight_lines: 50-52
---
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
	
	while True:
        data = get_sense_data()
        data_writer.writerow(data)
--- /code ---

--- /task ---

--- task ---

Run your program for a few minutes. You can stop the program and you should be able to find the `.csv` file in your file manager.

The first line should look something like this:
```python
36.324222564697266,1024.387939453125,32.6043815612793,0,0,0,1,138.03485829553443,12.164214303276808,353.07380995988177,-10.638025283813477,-9.077208518981934,1.978834867477417,-0.20660144090652466,-0.11602965742349625,0.9455438256263733,-0.005754658952355385,-0.00629773736000061,0.00323345884680748,2022-07-26 11:12:45.316169
```
--- /task ---

