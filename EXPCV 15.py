import cv2
import numpy as np

# Open video file
cap = cv2.VideoCapture(r"C:\Users\gowri\Desktop\input_video.mp4")

# Check if video opened
if not cap.isOpened():
    print("Error: Video not found")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # Source points (from original frame)
    pts1 = np.float32([
        [50, 50],
        [w-50, 50],
        [50, h-50],
        [w-50, h-50]
    ])

    # Destination points (changed perspective)
    pts2 = np.float32([
        [100, 100],
        [w-100, 80],
        [120, h-100],
        [w-120, h-120]
    ])

    # Get perspective transform matrix (DLT)
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply transformation
    transformed = cv2.warpPerspective(frame, M, (w, h))

    # Display output
    cv2.imshow("Original Video", frame)
    cv2.imshow("DLT Transformed Video", transformed)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
