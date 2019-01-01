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
    timeout=1
)


def serialWriteByte(token, var=""):

    if token == 'c' or token == 't':  # data
        instrStr = token + str(var[0]) + ',' + str(var[1]) + '\n'
    elif token == 'l':  # use binary to reduce packet size
        ser.write('l' + str(len(var)))
        instrStr = struct.pack('b' * len(var), *var)
    elif token == 'w' or token == 'k':
        instrStr = token + var + "\n"
    else:
        instrStr = token
    ser.write(instrStr)


if __name__ == '__main__':
    serialWriteByte('k',"sit")
    time.sleep(2)
    if len(sys.argv) == 2:
        serialWriteByte(sys.argv[1][0], sys.argv[1][1:])
    else:
        while True:
            for a in np.arange(0, 2 * math.pi, 0.2):
                print (a)
                serialWriteByte('l', [0, math.sin(a) * 30])
                serialWriteByte('l', [1, math.cos(a) * 30])
                serialWriteByte('l', [2, math.cos(a) * 30])
                time.sleep(0.04)

    while ser.in_waiting:
        x = ser.readline()
        if x != "":
            print (x + "\n")
