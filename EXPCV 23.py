import cv2

image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

if image is None:
    print("Image not found")
    exit()

blur = cv2.GaussianBlur(image, (0,0), 5)
sharp = cv2.addWeighted(image, 1.5, blur, -0.5, 0)

cv2.imshow("Original", image)
cv2.imshow("Unsharp Masking", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
