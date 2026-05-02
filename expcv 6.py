import cv2

def play_video(video_path, speed=1.0):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        delay = int(1000 / (fps * speed))
        if cv2.waitKey(delay) & 0xFF == 27:  # Press ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()


# 👉 Your video path added here
play_video("C:/Users/gowri/Desktop/input_video.mp4", speed=1.0)
