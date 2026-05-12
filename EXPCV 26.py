# 26. Insert Watermark to the Image using OpenCV

import cv2

# Read main image
img = cv2.imread(r"C:\Users\gowri\Desktop\lion.jpg")

# Read watermark image
logo = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

# Resize watermark image (optional)
logo = cv2.resize(logo, (150, 150))

# Get dimensions
h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape

# Position of watermark (bottom-right corner)
top_y = h_img - h_logo - 10
left_x = w_img - w_logo - 10
bottom_y = top_y + h_logo
right_x = left_x + w_logo

# Blend images
roi = img[top_y:bottom_y, left_x:right_x]

result = cv2.addWeighted(roi, 0.7, logo, 0.3, 0)

# Place blended image back
img[top_y:bottom_y, left_x:right_x] = result

# Save output image
cv2.imwrite(r"C:\Users\gowri\Desktop\watermarked_output.jpg", img)

# Show output
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
