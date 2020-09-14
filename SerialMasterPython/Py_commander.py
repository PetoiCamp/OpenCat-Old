#!/usr/bin/python
import os
import serial
from ardSerial import *
import time

#keys UsbSerial might be different over differenet OS/computers
#Bluetooth might have its can of worms over differeent OS that we didnt discover yet.tested only on Linux based operating systems
port_reference_dictionary={"PiSocket":"ttyS0","Bluetooth":"rfcomm0","usb":"ttyUSB0"} 

def Port_Opener(key):
    '''
    Will need the particular bluetooth address of the bluetooth device of the form->xx:xx:xx:xx:xx:xx
    Assumes sudo will not ask for the password
    key is bool..0 represents serial port, 1 represents bluetooth
    Might only work for linux
    rfcomm0 is the name of the bluetooth port..could be changed
    ttyS0 is the name of the RaspPi/Arduino port
    '''

    if key=="Bluetooth":
        os.system("sudo rfcomm bind 0 00:18:E4:40:00:06") #bluetooth mac address of the device..might be different for non-linux opearting systems

    port = serial.Serial(port='/dev/'+port_reference_dictionary[key],baudrate=57600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
    if key=="Bluetooth": time.sleep(10)

    return port


def Port_Closer(key,port):
    '''
    Only the Bluetooth connection case needs to be handled. If not disconnected properly, the bluetooth device will think that it 
    is still connected to the PC even though it might not be.
    '''
    if key=="Bluetooth":
        port.close()
        os.system("sudo rfcomm release 0 00:18:E4:40:00:06") #bluetooth mac address of the device
        print ("Bluetooth Port Successfully Closed")

if __name__ == '__main__':#1,9,13
    try:
        if len(sys.argv)==1:
            port=Port_Opener("usb");
            angle=50
            schedule = [['i',[8,angle,9,angle,10,angle,11,angle,12,angle,13,angle,14,angle,15,angle],5],\
#            schedule = [['m',[12,angle],5],\
                        ['kwk',5]]
            for task in schedule:
                wrapper(port,task)
#            Port_Closer("Bluetooth",port);
        else:
            port=Port_Opener(sys.argv[1])
            if len(sys.argv)==3:
                wrapper(port,[sys.argv[2],0]) #wrapper(port,[token, time])
            else:
                wrapper(port,[sys.argv[2][0],sys.argv[2:],0]) #wrapper(port,[token,['m','2','1'],time])....wrapper(['k',['k','balance'],0])
            Port_Closer(sys.argv[1],port)
    except Exception as a:
        print(a)
        os.system("sudo python2 Emergency_port_closer.py")
        print("There is some problem with port connectivity.\nProgram shut down\n Good hunting :)")