import cv2 as cv
import numpy as np

def cross(x):
    pass

img = np.zeros([300, 512, 3], np.uint8)
cv.namedWindow("Color Picker")

s1 = "0:OFF\n1:ON"
cv.createTrackbar(s1, "Color Picker", 0, 1, cross)

cv.createTrackbar("R", "Color Picker", 0, 255, cross)
cv.createTrackbar("G", "Color Picker", 0, 255, cross)
cv.createTrackbar("B", "Color Picker", 0, 255, cross)

while True:
    cv.imshow("Color Picker", img)
    if cv.waitKey(1) & 0xFF == ("q"):
        break

    s = cv.getTrackbarPos(s1, "Color Picker")
    r = cv.getTrackbarPos("R", "Color Picker")
    g = cv.getTrackbarPos("G", "Color Picker")
    b = cv.getTrackbarPos("B", "Color Picker")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r, g, b]

cv.destroyAllWindows()