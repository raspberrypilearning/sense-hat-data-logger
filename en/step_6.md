## Adding a header to the CSV file

You're collecting many different types of data in the CSV file. So that you know which type of data each column contains, it would be useful to add a header row to the CSV file.

To do this you can simply write an additional row to the CSV file before you start the infinite loop.

- Add this line after you create your `writer` object and before the `while True` loop starts:

```python
data_writer.writerow(['temp','pres','hum',
	                  'yaw','pitch','roll',
                      'mag_x','mag_y','mag_z',
                      'acc_x','acc_y','acc_z',
                      'gyro_x', 'gyro_y', 'gyro_z', 
                      'datetime'])
```

- Make sure the headers are in the same order as the data produced by your `get_sense_data()` function.
