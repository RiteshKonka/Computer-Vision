import cv2
import pickle


width,height = 107,48

try : 
    with open('RectPos','rb') as f:
        positionList = pickle.load(f)
except:
    positionList=[]


def mouseClick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        positionList.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(positionList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y1+height:
                positionList.pop(i)

    with open('RectPositions','wb') as f:
        pickle.dump(positionList,f)


while True:
    img = cv2.imread("carParkImg.png")
    for pos in positionList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(0,0,255),thickness=2)

    cv2.imshow('image',img)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)  