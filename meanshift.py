import cv2
import numpy as np


print ('Welcome to meanshift tracking! Please choose from the following videos(Enter number): 1, goldfish.avi 2, goldfish2.avi ')
imgnum=input() #enable the users to choose the video they want to apply meanshift algorithm
   
if imgnum=='1':
            cap=cv2.VideoCapture("goldfish.avi")
            x1, y1, x2, y2 = 400, 375,300,275 #initialize the original positions of tracker

if imgnum=='2':
            cap=cv2.VideoCapture("goldfish2.avi")
            x1, y1, x2, y2 = 400, 400,300,300


w=x1-x2 #width of tracking window
h=y1-y2 #height of tracking window

fx=x2+w/2
x1=fx
fy=y2+h/2
y1=fy

ret,img1=cap.read()

while(ret):#loop from the first frame to last frame in video
    img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)#convert the frame to grayscale
    if ret==0:
        break
    while(1):
        roi=img2[int(fy-(y1-y2)/2):int(fy+(y1-y2)/2),int(fx-(x1-x2)/2):int(fx+(x1-x2)/2)]#读取窗口内数据
        m10=0#initialize the moments
        m01=0
        m00=0
        for i in range(0,roi.shape[0]):#calculate the new moment
            for j in range(0,roi.shape[1]):
                ax=roi[i][j]
                m10+=j*ax
                m01+=i*ax
                m00+=ax
        try:
            fx_new=int(m01/m00)+fy-(y1-y2)/2#calculate new center of mass
            fy_new=int(m10/m00)+fx-(x1-x2)/2
            if(fx_new==fy and fy_new==fx):#check if new center of mass matches the old one
                fy=fx_new
                fx=fy_new
                break
            else:
                fy=fx_new
                fx=fy_new
        except:
            break
            
    #show the title for the tracker       
    cv2.putText(img1,'fish1',(int(fx-(x1-x2)/2),int(fy-(y1-y2)/2)), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
    #show the frame of tracker
    cv2.rectangle(img1,(int(fx-(x1-x2)/2),int(fy-(y1-y2)/2)),(int(fx+(x1-x2)/2),int(fy+(y1-y2)/2)),(0,255,255),2)
    #show the current frame
    cv2.imshow('image',img1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    #load the next frame
    ret,img1=cap.read()

cap.release()
cv2.destroyAllWindows()