import subprocess
import time
import os
import platform
#print (os.name)
#print(platform.system())
"""
    Linux: Linux
    Mac: Darwin
    Windows: Windows
    """
#print(platform.release())

if platform.system()=="Linux":
    serialLocation="/sys/class/tty/"
elif platform.system()=="Darwin":
    serialLocation="/dev/"
elif platform.system()=="Windows":
    serialLocation="I don't know. Help me."
else: #exception
    serialLocation="???"
print("Checking device list in: "+serialLocation)
# find usb serial port
proc1 = subprocess.Popen(['ls', serialLocation], stdout=subprocess.PIPE)
proc2 = subprocess.Popen(['grep', 'USB\|usb'], stdin=proc1.stdout,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
out, err = proc2.communicate()
usbList= out.decode("utf-8").split('\n')
usbList=list(filter(None,usbList))
usbName=list(map(lambda x:x.split('.')[-1],usbList))

#print (usbName)
#print (set(usbName))
if len(set(usbName))==1:
    print(usbList)

else:
    out1 = subprocess.Popen(["ls", serialLocation],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    stdout1,stderr1 = out1.communicate()
    list1=set(stdout1.decode("utf-8").split('\n'))
    print("Please plug in（or unplug）the USB uploader you want to use.")
    choice = input("Wait for 3 seconds. Ready? (Y/n): ")
    while choice.lower()!="y":
        choice=input("Please press 'Y': ")
    out2 = subprocess.Popen(["ls", serialLocation],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    stdout2,stderr2= out2.communicate()
    list2=set(stdout2.decode("utf-8").split('\n'))
    usbList= list(list1-list2 or (list2-list1))
    print(usbList)