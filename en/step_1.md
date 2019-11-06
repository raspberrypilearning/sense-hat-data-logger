## What you will make

In this activity, you will learn how to use the Sense HAT hardware to build a data-logging device which can capture a range of information about its immediate environment.

Once you've created your data logger, you will be able to use it to conduct your own experiments and record data. Things we've tried with our data logger include:

- Dropping it from a four-storey building
- Putting it in a fridge and observing temperature changes
- Sending it to the edge of space with a helium balloon

--- collapse ---
---
title: What you will learn
---

- How to collect data from multiple sensors and add it to a list structure
- To write and append data to a text file from within a Python program
- To capture and respond to input from the Sense HAT joystick
- About using threads to allow multiple parts of a program to run at once

--- /collapse ---

--- collapse ---
---
title: What you will need
---

### Hardware

- A Raspberry Pi computer
- A Sense HAT

**If you do not have a Sense HAT, you can use the emulator program available on your Raspberry Pi**

### Software

You will need the [latest version of Raspbian](https://www.raspberrypi.org/downloads/), which already includes the following software packages:

- Python 3
- Sense HAT for Python 3

If for any reason you need to install a package manually, follow these instructions:

[[[rpi-install-software]]]

Type this command into the terminal to install the Sense HAT package:

```bash
sudo apt-get install sense-hat
```

--- /collapse ---