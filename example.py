import screenpoint
import cv2

# Load input images.
screen = cv2.imread('example/screen.png', 0)
view = cv2.imread('example/view.jpg', 0)

# Project centroid.
x, y, img_debug = screenpoint.project(view, screen, True)

# Write debug image.
cv2.imwrite('example/match_debug.png', img_debug)