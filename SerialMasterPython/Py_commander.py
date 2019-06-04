#!/usr/bin/python
import os
import serial
from ardSerial import *


#keys UsbSerial might be different over differenet OS/computers
#Bluetooth might have its can of worms over differeent OS that we didnt discover yet.tested only on Linux based operating systems
port_reference_dictionary={"PiSocket":"ttyS0","Bluetooth":"rfcomm0","UsbSerial":"ttyUSB0"} 

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

    port = serial.Serial(port='/dev/'+port_reference_dictionary[key],
                        baudrate=57600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)

    if key=="Bluetooth": time.sleep(10)

    return port


def Port_Closer(key):
    if key=="Bluetooth":
        port.close()
        os.system("sudo rfcomm release 0 00:18:E4:40:00:06") #bluetooth mac address of the device

if __name__ == '__main__':
        if len(sys.argv)==1:
            try:
                port=Port_Opener("Bluetooth");
                schedule = [['ktr',5],\
                            ['kbalance',3],\
                            ['ksit',2],\
                            ['ktr',3],\
                            ['kwk',3],\
                            ['d',2]]
                for task in schedule:
                    wrapper(port,task)
                Port_Closer("Bluetooth");
            except Exception as a:
                print(a)
                os.system("sudo python2 Emergency_port_closer.py")
                print("There is some problem with port connectivity.\nProgram shut down\n Good hunting :)")
        else:
            port=Port_Opener(sys.argv[1])
            if len(sys.argv)==3:
                wrapper(port,[sys.argv[2],0]) #wrapper(port,[token, time])
            else:
                wrapper(port,[sys.argv[2][0],sys.argv[2:],0]) #wrapper(port,[token,['m','2','1'],time])....wrapper(['k',['k','balance'],0])
            Port_Closer(sys.argv[1])