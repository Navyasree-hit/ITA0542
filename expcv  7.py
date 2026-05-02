import cv2

# Open webcam
cap = cv2.VideoCapture(0)

speed_factor = 1.0  # initial speed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam Video", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('+'):
        speed_factor += 0.5

    elif key == ord('-'):
        speed_factor = max(0.5, speed_factor - 0.5)

    elif key == ord('q'):
        break

    # control speed using delay
    delay = int(30 / speed_factor)
    cv2.waitKey(delay)

cap.release()
cv2.destroyAllWindows()
