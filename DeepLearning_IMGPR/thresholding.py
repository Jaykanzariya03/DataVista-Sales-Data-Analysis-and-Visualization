import cv2

img = cv2.imread(r"C:\Users\jayka\Downloads\wp1848195-your-lie-in-april-wallpapers.png", 0)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold Image', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()