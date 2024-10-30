import cv2

img = cv2.imread(r"C:\Users\jayka\Downloads\Screenshot 2024-09-09 192021.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()