# 27. Cropping, Copying and Pasting Image using OpenCV

import cv2

# Read main image
main_image = cv2.imread(r"C:\Users\gowri\Desktop\lion.jpg")

# Read second image
paste_image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

# Check images loaded correctly
if main_image is not None and paste_image is not None:

    # Resize paste image
    paste_image = cv2.resize(paste_image, (400, 400))

    # Crop region from main image
    cropped_region = main_image[50:250, 50:250]

    # Resize cropped region to match paste area
    cropped_region = cv2.resize(cropped_region, (150, 150))

    # Position to paste
    start_y = 100
    start_x = 100

    # Paste cropped image
    paste_image[start_y:start_y+150, start_x:start_x+150] = cropped_region

    # Save output image
    cv2.imwrite(r"C:\Users\gowri\Desktop\output.jpg", paste_image)

    # Display result
    cv2.imshow("Result", paste_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error: Could not load images.")
