import cv2
import numpy as np
import os
import time
from concurrent.futures import ThreadPoolExecutor
# def stack_images(start_index, end_index, base_path, segment_paths):
#     start_time = time.time()  # Start the timer

#     for segment_index, segment in enumerate(segment_paths):
#         stacked_image = None

#         for i in range(start_index, end_index+1):
#             img_path = os.path.join(base_path, segment, 'keyframe_{}.png'.format(i))
            
#             if not os.path.isfile(img_path):
#                 print("Image at path '{}' not found, skipping...".format(img_path))
#                 continue

#             img = cv2.imread(img_path)
#             if img is None:
#                 print("Failed to read image at path '{}', skipping...".format(img_path))
#                 continue

#             if stacked_image is None:
#                 stacked_image = np.zeros_like(img, dtype=np.float32)

#             stacked_image = np.maximum(stacked_image, img)  # Keep the maximum value for each pixel

#         if stacked_image is not None:
#             stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)  # Convert data type back to uint8 (image)
#             output_path = os.path.join(base_path, segment, 'stacked_image.png')
#             cv2.imwrite(output_path, stacked_image)

#     end_time = time.time()  # Stop the timer
#     execution_time = end_time - start_time
#     print("Execution time: {:.2f} seconds".format(execution_time))

# # Example usage
# start_index = 1  # Starting image index
# end_index = 500  # Ending image index
# base_path = "outputFrame2\\"  # Base path of the images
# segment_paths = ["segment_{}".format(i) for i in range(16)]  # List of segments from "segment_0" to "segment_15"
# stack_images(start_index, end_index, base_path, segment_paths)
def stack_images(start_index, end_index, base_path, segment_paths):
    start_time = time.time()  # Start the timer

    for segment_index, segment in enumerate(segment_paths):
        stacked_image = None

        for i in range(start_index, end_index+1):
            img_path = os.path.join(base_path, segment, 'keyframe_{}.png'.format(i))
            
            if not os.path.isfile(img_path):
                print("Image at path '{}' not found, skipping...".format(img_path))
                continue

            img = cv2.imread(img_path)
            if img is None:
                print("Failed to read image at path '{}', skipping...".format(img_path))
                continue

            if stacked_image is None:
                stacked_image = np.zeros_like(img, dtype=np.float32)

            stacked_image = np.maximum(stacked_image, img)  # Keep the maximum value for each pixel

        if stacked_image is not None:
            stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)  # Convert data type back to uint8 (image)
            output_path = os.path.join(base_path, "{}.png".format(segment))
            cv2.imwrite(output_path, stacked_image)

    end_time = time.time()  # Stop the timer
    execution_time = end_time - start_time
    print("Execution time: {:.2f} seconds".format(execution_time))

# Example usage
start_index = 1  # Starting image index
end_index = 500  # Ending image index
base_path = "outputFrame\\"  # Base path of the images
segment_paths = ["segment_{}".format(i) for i in range(36)]  # List of segments from "segment_0" to "segment_15"
stack_images(start_index, end_index, base_path, segment_paths)
