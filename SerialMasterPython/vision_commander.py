import numpy as np
import cv2
import math
import time
from ardSerial import *
from Py_commander import *

def skin_col_range(frame,coordinates):
        '''
        Finds the avg. of the pixels in the box and sends back an acceptable range 
        '''
        top=coordinates[0][0]+2
        down=coordinates[1][0]-2
        left=coordinates[0][1]+2
        right=coordinates[1][1]-2

        #Extracting the frame
        myimg=frame[left:right,top:down]

        #Calculating the avg.
        avg_color_per_row = np.average(myimg, axis=0)
        avg=np.average(avg_color_per_row, axis=0)

        #Please change these params below for your skin color and light, environmental conditions
        Color_wavelength_range=6#Increase to have a higher color range.
        Saturation_brightness=0.3#increase to constrict the sauration and brightness ranges for filteration.
        return [(avg[0]-Color_wavelength_range,int(avg[1]*(1-Saturation_brightness)),10),(avg[0]+Color_wavelength_range,int(avg[1]*(1+Saturation_brightness)),225)]

def skin_finder(cap):
        '''
        Puts a box on the image and asks the user to put their skin in it and press r or l depending on which arm to measure from
        Please when you see the image, make sure that the skin color is significantly different from the back fround.
        '''
        while(True):
                ret, frame = cap.read()

                #setting up the rectangle
                upper_left_coord=(frame.shape[1]//2-12,frame.shape[0]//4-12)
                lower_righ_coord=(frame.shape[1]//2+12,frame.shape[0]//4+12)
                cv2.rectangle(frame,upper_left_coord,lower_righ_coord,(100,150,200),1)
                
                cv2.putText(frame,'Put your skin in the rectangle above and press r or l',(10,450),cv2.FONT_HERSHEY_SIMPLEX, 0.75,(100,200,100),1,cv2.LINE_AA)
                
                #Making the RGB and HSV frames appear side by side
                HSVimage=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                res = np.hstack((frame,HSVimage))
                cv2.imshow("Image ", res)
                
                key=cv2.waitKey(1)
                if key == ord('r'):
                        return ("r",skin_col_range(HSVimage, (upper_left_coord,lower_righ_coord)))
                        break
                if key == ord('l'):
                        return ("l",skin_col_range(HSVimage, (upper_left_coord,lower_righ_coord)))
                        break

def getAngle(a, b, c):
        '''
        Uses the scalar/dot product to calculate the angle
        '''
        ba = [a[0] - b[0],a[1] - b[1]]
        bc = [c[0] - b[0],c[1] - b[1]]

        divisor=np.linalg.norm(ba) * np.linalg.norm(bc)
        cosine_angle=0
        if divisor!=0:
                cosine_angle = np.dot(ba, bc) / (divisor)
        ang = int(np.degrees(np.arccos(cosine_angle))) - 90
        if ang < -70:
                ang = -70
        elif ang>70:
                ang = 70
        return ang

def line_drawer(centroid,pnt,frame,key):
        '''
        Draws 2 lines: Between highest point on the contour and the centroid, and the horizontal. 
        Also calculates that angle and returns it
        '''
        cv2.circle(frame,centroid,10,[200,0,0],-1)
        cv2.circle(frame,pnt,10,[100,0,0],-1)
        cv2.line(frame,centroid,pnt,(255,0,0),10)

        #We need a horizontal line with the same y value as the centroid. 
        #The direction of the line will be left or right depending on which arm the user chooses
        new_pointx=frame.shape[1]
        if key=="l":
                new_pointx=0

        angle=getAngle(pnt,centroid,(new_pointx,centroid[1]))
        cv2.line(frame,centroid,(new_pointx,centroid[1]),(255,0,0),10)
        return angle

def getCentroid(contour):
        M = cv2.moments(contour)
        if M['m00']!=0:
                centroid_x = int(M['m10']/M['m00'])
                centroid_y = int(M['m01']/M['m00'])
                return (centroid_x,centroid_y)
        return (0,0)

def angle_writer(cap,key,skin_range,port):
    while(True):
        ret, frame = cap.read()

        #Gaussian blur
        frame=cv2.GaussianBlur(frame,(11,11),11)
        
        #Filteration
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame=cv2.inRange(frame,skin_range[0],skin_range[1])

        #Morphological transformations
        kernel = np.ones((5,5),np.uint64)
        frame = cv2.morphologyEx(frame,cv2.MORPH_CLOSE, kernel)
        frame = cv2.dilate(frame,kernel,iterations = 2)#increase the interations to increase the contour areas.

        #Finding contours
        frame = cv2.Laplacian(frame,cv2.CV_8UC1) ##Using canny was a bit more complex for what i wanted to do
        angle=0
        contours,hierarchy = cv2.findContours(frame,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        #Sometimes no contours in the image
        if len(contours) > 0:
                cnts = sorted(contours, key = cv2.contourArea, reverse = True)

                #This if statement is in there to make sure that if the user isn't in the frame, then the program doesn't start reading the
                #noise and sending signals
                if cv2.contourArea(cnts[0])>6000:
                        #By 3 I mean the left, right arms and the elbow. 
                        #It is assumed that they will have the highest area in the picture
                        number_to_be_analysed=3 if len(cnts)>3 else len(cnts)

                        #We will find the left most or the right most contour depending on which one the user wants to be read
                        center=(0,0)
                        contour_no=0
                        if key=="r":
                                center=frame.shape
                        for i in range(number_to_be_analysed):
                                center2 = getCentroid(cnts[i])
                                if (key=="r" and center2[0]<center[0]) or (key=="l" and center2[0]>center[0]):
                                        center=center2
                                        contour_no=i

                        #this if statement had to be put in to prevent a null point error from happening
                        if center[0]!=0:
                                cnt=cnts[contour_no]
                                topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
                                angle=line_drawer(center,topmost,frame,key)
        cv2.putText(frame,str(angle),(10,450),cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,0,0),2,cv2.LINE_AA)
        cv2.imshow("Lo and behold!!",frame)

        #Getting the angles and writing them to the serial port.
        wrapper(port,['i',[8,angle,9,angle,10,-1*angle,11,-1*angle,12,angle,13,angle,14,-1*angle,15,-1*angle],0.002])

        #to allow the user to switch between angles
        x=cv2.waitKey(1)
        if x == ord('q'):
            break
        elif x== ord('r'):
            key="r"
        elif x == ord('l'):
            key="l"

def main():

    port=Port_Opener("usb");
    cap = cv2.VideoCapture(0)

    skin_values=skin_finder(cap);
    
    cv2.destroyAllWindows()
    
    angle_writer(cap,skin_values[0],skin_values[1],port);
    cap.release()
    
    cv2.destroyAllWindows()

main()