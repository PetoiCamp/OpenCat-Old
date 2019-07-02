#!/usr/bin/python3
import os
import time
import serial
from ardSerial import *
from Py_commander import *
import speech_recognition as sr
import pocketsphinx
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from operator import itemgetter

def mic_opener():
    mic = sr.Microphone()
    return mic

def recogniser():
    return sr.Recognizer()

port=Port_Opener("UsbSerial");

mic=mic_opener();
r=recogniser();

with mic as source:
    print("Say something that i am giving up on you");
    r.listen(mic,snowboy_configuration=('/home/big_z/Desktop/snowboy/snowboy/examples/Python3',['/home/big_z/Documents/Academic/ComputerScience/PeotiInternship/OpenCat/SerialMasterPython/Hey_Nybble.pmdl']))
    print("Given Up");
    port.write('b 100 100') #command to start working