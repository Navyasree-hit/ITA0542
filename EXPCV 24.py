import cv2

image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

if image is None:
    print("Image not found")
    exit()

blur = cv2.GaussianBlur(image, (0,0), 5)

k = 2  # boost factor
high_boost = cv2.addWeighted(image, k, blur, -(k-1), 0)

cv2.imshow("Original", image)
cv2.imshow("High Boost", high_boost)
cv2.waitKey(0)
cv2.destroyAllWindows()
