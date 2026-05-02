import cv2
import numpy as np

# Open video file (use raw string to avoid path error)
cap = cv2.VideoCapture(r"C:\Users\gowri\Desktop\input_video.mp4")

# Check if video opened
if not cap.isOpened():
    print("Error: Video not found")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw 4 reference points
    cv2.circle(frame, (114, 151), 5, (0, 0, 255), -1)
    cv2.circle(frame, (605, 89), 5, (0, 0, 255), -1)
    cv2.circle(frame, (72, 420), 5, (0, 0, 255), -1)
    cv2.circle(frame, (637, 420), 5, (0, 0, 255), -1)

    # Source points (from video frame)
    imgPts = np.float32([
        [114, 151],
        [605, 89],
        [72, 420],
        [637, 420]
    ])

    # Destination points (output view)
    objPts = np.float32([
        [0, 0],
        [420, 0],
        [0, 637],
        [420, 637]
    ])

    # Perspective transform matrix
    matrix = cv2.getPerspectiveTransform(imgPts, objPts)

    # Apply perspective transform
    warped = cv2.warpPerspective(frame, matrix, (420, 637))

    # Show output
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", warped)

    # Press ESC to exit
    if cv2.waitKey(25) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
