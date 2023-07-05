import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('carPark.mp4')

width,height = 107,48
with open('RectPos','rb') as f:
    positionList = pickle.load(f)

def checkParkingSpace(imgProcess):
    yes = 0
    for pos in positionList:
        x,y = pos
        imgCrop = imgProcess[y:y+height,x:x+width]
        # cv2.imshow(str(x*y),imgCrop)
        count = cv2.countNonZero(imgCrop)
        # cvzone.putTextRect(img,str(count),(x,y+height-10),scale=1,thickness=2) 

        if count<850:
            color = (0,255,0)
            thickness = 4
            yes+=1
        else : 
            color = (0,0,255)
            thickness = 2
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),color,thickness)

    cvzone.putTextRect(img,f"Free : {str(yes)}/{len(positionList)}",(400,50),scale=2,thickness=4)
        
        

while True:
    success,img = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian,kernel,iterations=1)
    checkParkingSpace(imgDilate)
    cv2.imshow("image",img)
    cv2.waitKey(10)