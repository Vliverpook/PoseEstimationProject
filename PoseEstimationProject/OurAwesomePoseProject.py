import cv2
import mediapipe as mp
import time
import PoseModule

cap = cv2.VideoCapture('PoseVideos/BigPowerKing.mp4')
pTime = 0
detector = PoseModule.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    # print(lmList)

    img = cv2.resize(img, (int(img.shape[1] / 4), int(img.shape[0] / 4)))
    if len(lmList)!=0:
        print(lmList[9])
        cv2.circle(img,(int(lmList[9][1]/4),int(lmList[9][2]/4)),3,(0,0,255),cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow('Image', img)
    cv2.waitKey(1)