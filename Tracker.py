import numpy as np
import cv2 as cv

#Captures video and sets it to 1920x1080 res
cap = cv.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)



#This rescales the window
def rescale_frame(frame, percent=75): 
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

#Checks to see if the cameras resources are availible
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    

    
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)#Convert BGR to HSV color    
    lower_pink = np.array([120,90,200])
    upper_pink = np.array([170,130,240])
    mask = cv.inRange(hsv, lower_pink, upper_pink)

    
    
   

    kernal = np.ones((5,5),"uint8")

    mask = cv.dilate(mask, kernal)
    res = cv.bitwise_and(frame,frame, mask= mask)#and the pixles together 1&1
    
    

    contours, hierarchy = cv.findContours(mask,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv.boundingRect(contour)
            iframe = cv.rectangle(res, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 0)
            center_x = int(x+w/2)
            center_y = int(y+h/2)
            
            print(center_x,center_y) #prints current coordinates
            print("----------")
            
            cv.circle(iframe, (center_x,center_y),3,(255,0,0),-1)#draw center point




    frame = cv.flip(frame,1)#mirrors the window for visual accuracy
    #frame75 = rescale_frame(frame, percent=150)
    cv.imshow('Tracking', res)
   


    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
