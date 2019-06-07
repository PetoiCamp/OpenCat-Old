import subprocess
import time

print("If the usb uploader was connected before this program ran, please plug it out and re-run the program\n")

out1 = subprocess.Popen(['ls', '/sys/class/tty/'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)

stdout1,stderr1 = out1.communicate()

stdout1=stdout1.split()


print("If not, please plug in the USB uploader quickly \n")
choice = input("Type y and hit enter once the usb uploader is connected: \n")

while choice!="y": choice=input("Please press y: ")

out2 = subprocess.Popen(['ls', '/sys/class/tty/'], 
       stdout=subprocess.PIPE, 
       stderr=subprocess.STDOUT)
stdout2,stderr2= out2.communicate()
stdout2=stdout2.split()
stuff=list(set(stdout2) - set(stdout1))

print("\n")
print("\n")

print(stuff[0].decode("utf-8"))
print("\n")
print("Please add this name as the 2 value of USBuploader key in the port_reference_dictionary dictionary in Py_commander.py\n\n")


choice2=input("Plug in the bluetooth uploader onto your Cat and power the cat on\n Press y after doing that and hit enter \n")

while choice!="y": choice2=input("Please press y and hit enter:")

out3 = subprocess.Popen(['hcitool', 'scan'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)

stdout3,stderr3 = out3.communicate()

stdout3=stdout3.decode("utf-8")
stdout3=stdout3[13:]
stdout3=stdout3.split('\n\t')
print("\n")
print(stdout3)
print("\n")

print("Please find the mac address of your bluetooth device from here. The device is named Nybble-something and the address is of the form xx:xx:xx:xx:xx:xx. Don't copy over the tabs and newline charecters. Change the bluetooth address in the os.system functions (different from the dictionary) inside the Py_commander.py file")