import cv2 as cv
from util import get_limits
from PIL import Image

capture = cv.VideoCapture(1)

yellow = (0,255,255) #BGR yellow
lowerLimit, upperLimit = get_limits(yellow)
while True:
    isTrue, frame = capture.read()
    cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #inRange return a mask with the location of the object colored with the intrested color
    mask = cv.inRange(frame,lowerLimit,upperLimit)
    mask_ = cv.merge([mask,mask,mask])
    test = cv.bitwise_and(mask_,frame)
    cv.imshow('Stream',test)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break

capture.release()
cv.destroyAllWindows()