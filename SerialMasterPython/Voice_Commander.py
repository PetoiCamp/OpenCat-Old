#!/usr/bin/python
import os
import time
import serial
from ardSerial import *
from Py_commander import *
import speech_recognition as sr
import pocketsphinx


#A lot of help was taken from this article: https://realpython.com/python-speech-recognition/

Command_list=['d','kwk','kbalance','ktr','ksit']

def mic_opener():
    #returns an audio mic obj.
    mic = sr.Microphone()
    return mic

def recogniser():
    return sr.Recognizer()

def voice_recorder(mic,recognizeer):
    #returns a string
    with mic as source:
        recognizeer.adjust_for_ambient_noise(source,duration=2)
        print "recording audio"
        audio = recognizeer.listen(source,timeout=5)
        print "Done recording audio"
        return audio #needs to wait for the audio to return

def classifier(audio, recognizeer):
    '''
    Extracts and classifies commands from the input string
    Returns a string
    '''
    try:
        print "Abt to call google API"
        st=recognizeer.recognize_sphinx(audio)#, language='en-IN'))
        st=st.lower();
        print "str: "+st
        cmd=["not valid",0.0]
        if st=="wake up" or st=="balance":
            cmd=['kbalance',0.0]
        elif st=="walk" or st=="move" or st=="apple":
            cmd=['kwk',0.0]
        elif st=="str" or st=="orange":
            cmd=["kstr",0.0]
        elif st=="trot" or st=="water":
            cmd=['ktr',0.0]
        elif st=="sleep" or st=="banana":
            cmd=['d',0.0]
        return cmd
    except sr.UnknownValueError:
        print "Either nothing was recorded or we didnt understand what you said. Please repeat"
        return "Exception"
    except sr.RequestError:
        print "Either your API requests aren't working or you ran out of them for the day"
    else:
        return ['d',0]

def commander(mic,recogniseer,waker):
    '''
    waker 0 for commanding, waker 1 for waking
    Waking waits for the waking up call. Then writes 'kbalance' to the serial port and returns true
    Commanding listens and performs the command
    '''
    while True:
        time.sleep(2)

        audio=voice_recorder(mic,r);#record audio
        cmd=classifier(audio,r);#Extract text from the audio

        if cmd[0] in Command_list:
            if (waker and cmd[0]=="kbalance") or not waker:
                wrapper(port,cmd)
                if waker or cmd[0]=='d':
                    break
        else:
            if not waker:
                port.write('u')
if __name__ == '__main__':
    port=Port_Opener("Bluetooth");

    mic=mic_opener();
    r=recogniser();

    commander(mic,r,1)#wait for the cat to wake up
    commander(mic,r,0)#wait for the cat to goto sleep

    Port_Closer("Bluetooth",port);