import cv2

img = cv2.imread(r"C:\Users\jayka\Downloads\Screenshot 2024-09-09 192021.png")
blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()