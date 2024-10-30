import cv2

# Capture from the webcam (live stream)
live_stream = cv2.VideoCapture(0)

# Capture two saved videos
video1 = cv2.VideoCapture(r"C:\Users\jayka\Downloads\855564-hd_1920_1080_24fps.mp4")
video2 = cv2.VideoCapture(r"C:\Users\jayka\Downloads\855564-hd_1920_1080_24fps.mp4")

# Function to play a video (live stream or saved)
def play_video(video, window_name):
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Display the current frame
        cv2.imshow(window_name, frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



# Play each video one by one
print("Playing live stream...")
play_video(live_stream, 'Live Stream')

print("Playing first saved video...")
play_video(video1, 'Saved Video 1')

print("Playing second saved video...")
play_video(video2, 'Saved Video 2')



live_stream.release()
video1.release()
video2.release()
cv2.destroyAllWindows()
