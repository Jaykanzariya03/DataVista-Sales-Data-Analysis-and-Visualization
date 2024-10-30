import cv2

img = cv2.imread(r"C:\Users\jayka\Downloads\wp1848195-your-lie-in-april-wallpapers.png")
resized = cv2.resize(img, (300, 300))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()