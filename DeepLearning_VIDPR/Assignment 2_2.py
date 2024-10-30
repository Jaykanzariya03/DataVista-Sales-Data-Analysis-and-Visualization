import cv2

# Open the webcam for live stream
cap_live = cv2.VideoCapture(0)

# Open the two saved video files
cap_video1 = cv2.VideoCapture(r"C:\Users\jayka\Downloads\855564-hd_1920_1080_24fps.mp4")
cap_video2 = cv2.VideoCapture(r"C:\Users\jayka\Downloads\855564-hd_1920_1080_24fps.mp4")

if not cap_live.isOpened():
    print("Error: Could not open the webcam.")
    exit()

if not cap_video1.isOpened():
    print("Error: Could not open video1.mp4.")
    exit()

if not cap_video2.isOpened():
    print("Error: Could not open video2.mp4.")
    exit()

while True:
    # Read frames from webcam (live stream)
    ret_live, frame_live = cap_live.read()
    if not ret_live:
        print("Error: Could not capture frame from live stream.")
        break

    # Read frames from the first saved video
    ret_video1, frame_video1 = cap_video1.read()
    if not ret_video1:
        print("Error: Could not read frame from video1.mp4.")
        break

    # Read frames from the second saved video
    ret_video2, frame_video2 = cap_video2.read()
    if not ret_video2:
        print("Error: Could not read frame from video2.mp4.")
        break

    # Display each stream in a separate window
    cv2.imshow('Live Stream', frame_live)
    cv2.imshow('Video 1', frame_video1)
    cv2.imshow('Video 2', frame_video2)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all resources
cap_live.release()
cap_video1.release()
cap_video2.release()
cv2.destroyAllWindows()
