
def gotopeople ():
	for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      #grab the raw NumPy array representing the image, then initialize the timestamp and occupied/unoccupied text
      frame = image.array
      frame=cv2.flip(frame,1)
      global centre_x
      global centre_y
      centre_x=0.
      centre_y=0.
      hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      mask_red=segment_colour(frame)      #masking red the frame
      loct,area=find_blob(mask_red)
      x,y,w,h=loct
	  
	  
	   if (w*h) < 10:
            found=0
      else:
            found=1
            simg2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
            centre_x=x+((w)/2)
            centre_y=y+((h)/2)
            cv2.circle(frame,(int(centre_x),int(centre_y)),3,(0,110,255),-1)
            centre_x-=160
            centre_y-=120
            print 'X:',centre_x, 'Y:',centre_y
      initial=400
      flag=0
	  
	  
	   if(found==0):
            #if the person is not found and the last time it sees the person in which direction, it will start to rotate in that direction
            if flag==0:
                  Right()
                  time.sleep(0.05)
            else:
                  left()
                  time.sleep(0.05)
            stop()
            time.sleep(0.0125)
		elif(found==1):
            if(area<initial):
                  if(distance_to_camera<10):
                        #if Person is too far but it detects something in front of it,then it avoid it and go to people
                        if distanceR>=8:
                              Right()
                              time.sleep(0.00625)
                              stop()
                              time.sleep(0.0125)
                              forward()
                              time.sleep(0.00625)
                              stop()
                              time.sleep(0.0125)
                              #while found==0:
                              left()
                              time.sleep(0.00625)
                        elif distanceL>=8:
                              left()
                              time.sleep(0.00625)
                              stop()
                              time.sleep(0.0125)
                              forward()
                              time.sleep(0.00625)
                              stop()
                              time.sleep(0.0125)
                              Right()
                              time.sleep(0.00625)
                              stop()
                              time.sleep(0.0125)
                        else:
                              stop()
                              time.sleep(0.01)
                  else:
                        #otherwise it move forward
                        forward()
                        time.sleep(0.00625)
            elif(area>=initial):
                  initial2=6700
                  if(area<initial2):
                        if(distance_to_camera>10):
                              #it brings coordinates of the person to center of camera's imaginary axis.
                              if(centre_x<=-20 or centre_x>=20):
                                    if(centre_x<0):
                                          flag=0
                                          Right()
                                          time.sleep(0.025)
                                    elif(centre_x>0):
                                          flag=1
                                          left()
                                          time.sleep(0.025)
                              forward()
                              time.sleep(0.00003125)
                              stop()
                              time.sleep(0.00625)
                        else:
                              stop()
                              time.sleep(0.01)

                  else:
                      
                        time.sleep(0.1)
                        stop()
                        time.sleep(0.1)
      cv2.imshow("draw",frame)
      rawCapture.truncate(0)  # clear the stream in preparation for the next frame