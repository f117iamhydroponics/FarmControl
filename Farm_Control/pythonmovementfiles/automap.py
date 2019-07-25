import serial
import time
from decimal import *
from subprocess import call
import numpy as np
import cv2 as cv
#replace with custom cascade and create new ones

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# change to left veg
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
# change to right veg
# create center veg
# create end of row


# change to camera one and add second camera for weed detection

img = cv.imread('sachin.jpg')
# change to camera 0
# add camera two
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# add img2

# all weed detection will go within the for loop
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# create for loop for every cascade
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
	# change to weed detection
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv.imshow('img',img)


#if right_veg:
#	forward.py file
#elif == endofrow:
/*
	 def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write('AT'+'\r\n')            
rcv = port.read(100)
print rcv
time.sleep(.1)
 
port.write('AT+CGNSPWR=1'+'\r\n')             # to power the GPS
rcv = port.read(100)
print rcv
time.sleep(.1)
 
port.write('AT+CGNSIPR=115200'+'\r\n') # Set the baud rate of GPS
rcv = port.read(100)
print rcv
time.sleep(.1)
 
port.write('AT+CGNSTST=1'+'\r\n')    # Send data received to UART
rcv = port.read(100)
print rcv
time.sleep(.1)
 
port.write('AT+CGNSINF'+'\r\n')       # Print the GPS information
rcv = port.read(200)
print rcv
time.sleep(.1)
ck=1
while ck==1:
    fd = port.read(200)        # Read the GPS data from UART
    #print fd
    time.sleep(.5)
    if '$GNRMC' in fd:        # To Extract Lattitude and 
        ps=fd.find('$GNRMC')        # Longitude
        dif=len(fd)-ps
        if dif &gt; 50:
            data=fd[ps:(ps+50)]
            print data
            ds=data.find('A')        # Check GPS is valid
            if ds &gt; 0 and ds &lt; 20:
                p=list(find(data, ","))
                lat=data[(p[2]+1):p[3]]
                lon=data[(p[4]+1):p[5]]
 
# GPS data calculation
 
                s1=lat[2:len(lat)]
                s1=Decimal(s1)
                s1=s1/60
                s11=int(lat[0:2])
                s1 = s11+s1
 
                s2=lon[3:len(lon)]
                s2=Decimal(s2)
                s2=s2/60
                s22=int(lon[0:3])
                s2 = s22+s2
 
                print s1
                print s2
*/
#	 forward.py	()
#	 time.sleep(20);
#	 right.py ()
#	 time.sleep(20)
#	
#else
#	killmotor.py 




cv.waitKey(0)
cv.destroyAllWindows()