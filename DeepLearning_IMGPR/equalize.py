import cv2

img = cv2.imread(r"C:\Users\jayka\Downloads\wp1848195-your-lie-in-april-wallpapers.png", 0)
equalized = cv2.equalizeHist(img)

cv2.imshow('Equalized Image', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()