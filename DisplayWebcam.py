#Python 2.7, Numpy, OpenCV and SciPy REQUIRED TO RUN


import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:

#Capture frames
ret, frame = cap.read()

#operations on frame come here
gray = cv2.cvtColor(frame, cv2.Color_BGR_BGR2GRAY)




    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
cap.release()