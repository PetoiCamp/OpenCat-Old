The files in this folder help in different ways with serial port communication.
However, please read the description below of "Serial Connections set up.py" and run it before anything else.
Additionally, these programs have only been designed for and only tested on Linux/Debian.

The file names are listed below in the order of importance and later on with description of what they do.

1. ardSerial.py
2. Py_Commander.py
3. Voice_commander.py
4. Serial Connections set up.py
5. Emergency_port_closure.py

The first 3 files have a moduler architecture and can be imported into other python files to increase their 
functionalities. Py_Commander.py and Voice_commander.py import ardSerial.py to use it wrapper() and serial 
writer functions. Similarly, Voice_commander.py imports Py_Commander.py to help with port opening and closing. 
Please see the system_architecture.jpg image in this folder to develop a better understanding of the system.

1. ardSerial.py:

The functions in this file are responsible for handling incoming tasks and writing them to the serial port. A task is defined 
as [token, var=[], sleep_time]. The wrapper() will determine whether the variables are of numeric type or of string type and 
send them to the respective writeers.

An example of a numeric-type task is: . These tasks will be formed by the computer, like an AI process telling the cat what to do.
An example of a string-type task is: . These tasks will be formed if the command line is used to pass them.

The main function establishes a ttyS0 (Raspi<->NyBoard) serial connection. 
To run this file: "./ardSerial <command>".
Example: "./ardSerial m8 7" or "./ardSerial m 8 7" or "./ardSerial kbalance"

If no <command> argument is given, the cat will be made to sit.


2. Py_Commander.py:

This file's main purpose is to help establish a given type of a serial connection with the NyBoard (e.g. Bluetooth,  FTDI/USB, 
or 2x5 socket/Raspi<->NyBoard). It has 2 functions called Port_Opener() and Port_Closer() to help with this.

Like the ardSerial.py, the main function here can also be used to pass in commands via terminal. However, here you also need to 
specify a <connection type>. To run this file: "./Py_Commander <connection type> <command>".
Example: "./Py_Commander Bluetooth m8 7" or "./Py_Commander UsbSerial m 8 7" or "./Py_Commander PiSocket kbalance"

If no <connection type> and <command> argument is given, there is a built in schedule of tasks that the program will attempt
to send to the cat via a bluetooth connection.

3. Voice_commander.py:

This file's main purpose is to help a user give commands to the cat via a voice input.
It will assume that a bluetooth connection is to be used to connect the serial port with the cat.

It will use the CMU sphinx system to do decoding of our audio.

To run this file: "./Voice_Commander.py"

4. Serial Connections set up.py:

Please run this file before anything else and follow the instructions. Different computers will have different 
serial port names. It is meant to help one identify those names and set them up properly.

5. Emergency_port_closure.py:

This file is meant to help one safely close the bluetooth serial port in case of a problem. 
Might not solve the issues and you might have to restart the computer.