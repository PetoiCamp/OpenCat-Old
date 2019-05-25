#!/usr/bin/python
import serial
import struct
import sys
import time
import math
import numpy as np
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
    #rtscts=True,
#    dsrdtr=True        
)


def serialWriteByte(token, var=[]):
#    print("Token "+token+" var "+str(var))
    if (token == 'c' or token == 'm') and len(var)>=2:
        instrStr=""
        for element in var:
            instrStr=instrStr +element+" "
        print(instrStr)
    elif token == 'l' or token=='i':
        if(len(var[0])>1):
            var.insert(1,var[0][1:])       
        var[1:]=list(map(lambda x:int(x), var[1:]))
        print(var)
        instrStr = token+struct.pack('b' * len(var[1:]), *var[1:])+'~'

    elif token == 'w' or token == 'k':
        instrStr = var[0] + '\n'
    else:
        instrStr = token
 #   print(instrStr)
    ser.write(instrStr)

if __name__ == '__main__':
#    serialWriteByte('k',"sit")
    #time.sleep(2)
    counter=0
    
    if len(sys.argv) >= 2:
#        print(sys.argv[1][0], sys.argv[1:])        #remove later
        serialWriteByte(sys.argv[1][0], sys.argv[1:])

    else:
        while True:
            for a in np.arange(0, 2 * math.pi, 0.2):
                print (a)
                serialWriteByte('l', [0, math.sin(a) * 30])
                serialWriteByte('l', [1, math.cos(a) * 30])
                serialWriteByte('l', [2, math.cos(a) * 30])
                time.sleep(0.04)

    while True:
        time.sleep(0.01)
        counter=counter+1
        if counter>1000:
            break
        #print("number of chars:" +str(ser.in_waiting))
        if ser.in_waiting>0:
            x = ser.readline()
            if x != "":
                print (x),
