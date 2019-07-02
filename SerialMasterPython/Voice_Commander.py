#!/usr/bin/python
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

#A lot of help was taken from this article: https://realpython.com/python-speech-recognition/

Command_list=['d','kwk','kbalance','ktr','ksit','kstr','khi']

Valid_words=['wake up','balance','stretch','trot','sit','walk','sleep','Hi five','High five','five']

def mic_opener():
    mic = sr.Microphone()
    return mic

def recogniser():
    return sr.Recognizer()

def voice_recorder(mic,recognizeer):
    #returns a string
    with mic as source:
        recognizeer.adjust_for_ambient_noise(mic,duration=0.5)
        port.write('b 100 100') #command to start working
#        time.sleep(0.1)
        audio = recognizeer.record(source,duration=2.2)
        return audio

def Fuzzy_help(st):
    '''
    Uses fuzzy string comparison to help us reduce down the commands needed
    '''
    st=st.lower().split();
    List_of_possible_commands=[]
    print len(st)

    for element in st:
        List_of_possible_commands.append(process.extractOne(element,Valid_words))

    if len(List_of_possible_commands)>0:
        return max(List_of_possible_commands,key=lambda item:item[1])
    else:
        return ('nothing',100)  #doesn't matter what the inside command is as
                                #long as it is not in the Valid_words list

def classifier(audio, recognizeer):
    '''
    Extracts and classifies commands from the input string
    Returns a string
    '''
    try:
        words=recognizeer.recognize_google(audio_data=audio)    
        st_set=Fuzzy_help(words)
        st=st_set[0]

        cmd=["not valid",0.0]
        if st_set[1]<51:
            pass
        elif st=="wake up" or st=="balance":
            cmd=['kbalance',0.0]
        elif st=='walk':
            cmd=['kwk',0.0]
        elif st=="stretch":
            cmd=["kstr",0.0]
        elif st=="trot":
            cmd=['ktr',0.0]
        elif st=="sit":
            cmd=['ksit',0.0]
        elif st=='sleep':
            cmd=['d',0.0]
        elif st=='Hi five' or st=='High five'or st=='five':
            cmd=['khi',0.0]
        return cmd
    except sr.UnknownValueError:
        print ("Either nothing was recorded or we didnt understand what you said. Please repeat")
        return "Exception"
    except sr.RequestError:
        print ("Either your API requests aren't working or you ran out of them for the day")
    else:
        return ['d',0]

def commander(mic,recogniseer,waker):
    '''
    waker 0 for commanding, waker 1 for waking
    Waking waits for the waking up call. Then writes 'kbalance' to the serial port and returns true
    Commanding listens and performs the command
    '''
    while True:
        time.sleep(1.5)
        audio=voice_recorder(mic,recogniseer);#record audio
        cmd=classifier(audio,recogniseer);#Extract text from the audio

        if cmd[0] in Command_list:
            if (waker and cmd[0]=="kbalance") or not waker:
                wrapper(port,cmd)
                if waker or cmd[0]=='d':
                    break
        else:
            port.write('u0 10')



if __name__ == '__main__':
    port=Port_Opener("UsbSerial");

    mic=mic_opener();
    r=recogniser();

    commander(mic,r,1)#wait for the cat to wake up`
    commander(mic,r,0)#wait for the cat to goto sleep

    Port_Closer("Bluetooth",port);