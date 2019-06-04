import serial
import os

#Assumes that rfcomm was already bound to the mac address of the usb device 

#Opening and Closing the serial channel from python
port = serial.Serial(port='/dev/rfcomm0',baudrate=57600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
port.close()


#Closing the port from the OS. Tested only on linux 
os.system("sudo rfcomm release 0 00:18:E4:40:00:06") #bluetooth mac address of the device