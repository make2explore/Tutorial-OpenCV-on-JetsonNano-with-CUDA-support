# ---------------------------------- make2explore.com -------------------------------------------------------#
# Tutorial          - Installation of OpenCV on JetsonNano with CUDA support
# Created By        - info@make2explore.com
# Last Modified     - 14/09/2024 17:36:00 @admin
# Software          - Python3, OpenCV
# Hardware          - NVIDIA Jetson Nano 4GB, Webcam, CSI Camera      
# Source Repo       - github.com/make2explore
# ===========================================================================================================#
# This code is a 'test code' to verify the installtion of OpenCV
# This python program tracks Red Ball in camera frame in live video, with bounding box

import cv2
import numpy as np

print(cv2.__version__)

dispW = 640
dispH = 480
flip = 0

# Uncomment these next two lines for Pi Camera
camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method=' + str(flip) + ' ! video/x-raw, width=' + str(dispW) + ', height=' + str(dispH) + ', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
CSIcam = cv2.VideoCapture(camSet)

# Or, if you have a WEB cam, uncomment the next line
Webcam = cv2.VideoCapture(1)
Webcam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
Webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

# Function to detect and track the red ball
def detect_red_ball(frame):
    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the red color range in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    # Mask to extract red color
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Find contours of the red objects
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Get the bounding box around the largest contour
        area = cv2.contourArea(contour)
        if area > 500:  # Filter by area size
            x, y, w, h = cv2.boundingRect(contour)
            # Draw the rectangle around the red ball
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Red Ball', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    return frame

while True:
    ret, frame1 = CSIcam.read()
    ret, frame2 = Webcam.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Detect and track the red ball in both frames
    frame1 = detect_red_ball(frame1)
    frame2 = detect_red_ball(frame2)
    
    # Display the frames
    cv2.imshow('CSIcam', frame1)
    cv2.imshow('Webcam', frame2)
    
    # Move windows side by side
    cv2.moveWindow('CSIcam', 0, 0)
    cv2.moveWindow('Webcam', 640, 0)

    # Exit condition
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close windows
CSIcam.release()
Webcam.release()
cv2.destroyAllWindows()

