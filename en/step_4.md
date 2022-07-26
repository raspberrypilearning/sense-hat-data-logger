## Adding a header to the CSV file

You're collecting many different types of data in the CSV file. So that you know which type of data each column contains.

To do this you can write an additional row to the CSV file before you start the infinite loop.

--- task ---

Add these lines after you create your `writer` object and before the `while True` loop starts:

--- code ---
---
language: python
filename: main
line_numbers: true
line_number_start: 47
highlight_lines: 49-55
---
with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp', 'pres', 'hum',
                          'red', 'green', 'blue', 'clear', #only for Sense HAT version 2
                          'yaw', 'pitch', 'roll',
                          'mag_x', 'mag_y', 'mag_z',
                          'acc_x', 'acc_y', 'acc_z',
                          'gyro_x', 'gyro_y', 'gyro_z', 
                          'datetime'])
    while True:
        data = get_sense_data()
        data_writer.writerow(data)
--- /code ---

--- /task ---

**Tip** Make sure the headers are in the same order as the data produced by your `get_sense_data()` function.
