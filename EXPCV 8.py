import cv2

# Read image (your path added)
image = cv2.imread("C:/Users/gowri/Desktop/bird.jpeg")

# Check if image loaded
if image is None:
    print("Error: Image not loaded. Check path!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 30, 100)

    # Show results
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edges", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
