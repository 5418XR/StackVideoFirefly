import cv2
import os
import numpy as np

# Directory containing images to be checked
dir_path = "output_frames"

# Arbitrary threshold for sharpness, below this images will be considered blurry
sharpness_threshold = 10.0

# Iterate over the range of image numbers
for i in range(1, 3841):
    filename = f"keyframe_{i}.png"
    file_path = os.path.join(dir_path, filename)

    # Read the image
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)

    # Check if the image was properly loaded
    if image is not None:

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Measure the sharpness
        fm = cv2.Laplacian(gray, cv2.CV_64F).var()
        print(f"Sharpness of {filename}: {fm}")

        # If the image is blurry
        if fm < sharpness_threshold:
            print(f"Deleting {filename} due to low sharpness...")
            os.remove(file_path)
    else:
        print(f"Image {filename} could not be opened.")