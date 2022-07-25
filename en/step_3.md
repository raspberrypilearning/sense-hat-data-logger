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

Create a variable to hold the data from the function call within a new `while True` loop.

--- code ---
---
language: python
filename: main
line_numbers: true
line_number_start: 47
highlight_lines: 50-51
---
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
	
	while True:
        data_writer.writerow(data)
--- /code ---

--- /task ---
