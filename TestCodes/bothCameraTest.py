# ---------------------------------- make2explore.com -------------------------------------------------------#
# Tutorial          - Installation of OpenCV on JetsonNano with CUDA support
# Created By        - info@make2explore.com
# Last Modified     - 14/09/2024 17:36:00 @admin
# Software          - Python3, OpenCV
# Hardware          - NVIDIA Jetson Nano 4GB, Webcam, CSI Camera      
# Source Repo       - github.com/make2explore
# ===========================================================================================================#
# This code is a 'test code' to verify the installtion of OpenCV
# This python program check working of both cameras (webcam & CSI) with opencv (Simultaneously)

import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
CSIcam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
Webcam=cv2.VideoCapture(1)
Webcam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
Webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

while True:
    ret, frame1 = CSIcam.read()
    ret, frame2 = Webcam.read()
    cv2.imshow('CSIcam',frame1)
    cv2.imshow('Webcam',frame2)
    cv2.moveWindow('CSIcam',0,0)
    cv2.moveWindow('Webcam',640,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
