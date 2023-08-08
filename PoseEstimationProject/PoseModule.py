import cv2
import time
import mediapipe as mp

class poseDetector():
    def __init__(self,mode=False,complexity=1,smoothLandmarks=True,enable=False,smooth=True,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.complexity=complexity
        self.smoothLandmarks=smoothLandmarks
        self.enable=enable
        self.smooth=smooth
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose(self.mode,self.complexity,self.smoothLandmarks,self.enable,self.smooth,self.detectionCon,self.trackCon)

    def findPose(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self,img,draw=True):
        lmList=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                # print(lmList)
                cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
        return lmList


        #创建姿态检测对象
# mpPose=mp.solutions.pose
# pose=mpPose.Pose()
#
#
# mpDraw=mp.solutions.drawing_utils
#
#
# cap =cv2.VideoCapture('PoseVideos/BigPowerKing.mp4')
# pTime=0
#
# while True:
#     success, img=cap.read()
#     imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     results=pose.process(imgRGB)
#
#     if results.pose_landmarks:
#         mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
#
#         for id, lm in enumerate(results.pose_landmarks.landmark):
#             h,w,c=img.shape
#             cx,cy=int(lm.x*w),int(lm.y*h)
#             cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
#
#     img=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
#     cTime=time.time()
#     fps=1/(cTime-pTime)
#     pTime=cTime
#     cv2.putText(img,str(int(fps)),(10,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
#     cv2.imshow('Image',img)
#     cv2.waitKey(1)


def main():
    cap = cv2.VideoCapture('PoseVideos/BigPowerKing.mp4')
    pTime = 0
    detector=poseDetector()

    while True:
        success, img = cap.read()
        img=detector.findPose(img)
        lmList=detector.findPosition(img)
        print(lmList)


        img=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        cv2.imshow('Image',img)
        cv2.waitKey(1)

if __name__=='__main__':
    main()