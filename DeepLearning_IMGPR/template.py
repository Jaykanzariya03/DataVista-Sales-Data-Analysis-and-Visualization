import cv2

img = cv2.imread(r"C:\Users\jayka\Downloads\wp1848195-your-lie-in-april-wallpapers.png")
template = cv2.imread(r"C:\Users\jayka\Downloads\Screenshot 2024-09-09 192021.png", 1)
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

cv2.imshow('Detected Template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()