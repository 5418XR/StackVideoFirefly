# import cv2
# import numpy as np
# import os

# def stack_images(start_index, end_index, base_path, output_path):
#     stacked_image = None

#     for i in range(start_index, end_index+1, 1):
#         img_path = base_path + 'keyframe_{}.png'.format(i)
        
#         # 检查文件是否存在，如果不存在则跳过
#         if not os.path.isfile(img_path):
#             print("Image at path '{}' not found, skipping...".format(img_path))
#             continue

#         img = cv2.imread(img_path)
#         if img is None:
#             print("Failed to read image at path '{}', skipping...".format(img_path))
#             continue

#         if stacked_image is None:
#             stacked_image = np.zeros_like(img, dtype=np.float32)

#         stacked_image = np.maximum(stacked_image, img)  # 保留每个像素的最大值
        

#     if stacked_image is None:
#         print("No valid images found!")
#         return

#     # 将数据类型从 float32 转回 uint8（图片）
#     stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)

#     cv2.imwrite(output_path, stacked_image)

# # 使用示例
# start_index = 1  # 起始图片序号
# end_index = 4000  # 结束图片序号
# base_path = "output_frames\\"  # 图片的基本路径
# output_path = "stacked_image7.png"  # 输出图片路径
# stack_images(start_index, end_index, base_path, output_path)

import cv2
import numpy as np
import os
import time

# def stack_images(start_index, end_index, base_path, output_path):
#     stacked_image = None

#     start_time = time.time()  # Start the timer

#     for i in range(start_index, end_index+1, 10):
#         img_path = base_path + 'keyframe_{}.png'.format(i)
        
#         # Check if the file exists; if not, skip it
#         if not os.path.isfile(img_path):
#             print("Image at path '{}' not found, skipping...".format(img_path))
#             continue

#         img = cv2.imread(img_path)
#         if img is None:
#             print("Failed to read image at path '{}', skipping...".format(img_path))
#             continue

#         if stacked_image is None:
#             stacked_image = np.zeros_like(img, dtype=np.float32)

#         stacked_image = np.maximum(stacked_image, img)  # Keep the maximum value for each pixel

#     end_time = time.time()  # Stop the timer
#     execution_time = end_time - start_time
#     print("Execution time: {:.2f} seconds".format(execution_time))

#     if stacked_image is None:
#         print("No valid images found!")
#         return

#     stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)  # Convert data type back to uint8 (image)
#     cv2.imwrite(output_path, stacked_image)

# # Example usage
# start_index = 1  # Starting image index
# end_index = 4000  # Ending image index
# base_path = "output_frames\\"  # Base path of the images
# output_path = "stacked_image8.png"  # Output image path
# stack_images(start_index, end_index, base_path, output_path)

def stack_images(start_index, end_index, base_path, segment_paths):
    start_time = time.time()  # Start the timer

    for segment_index, segment in enumerate(segment_paths):
        stacked_image = None

        for i in range(start_index, end_index+1, 10):
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
            output_path = os.path.join(base_path, segment, 'stacked_image.png')
            cv2.imwrite(output_path, stacked_image)

    end_time = time.time()  # Stop the timer
    execution_time = end_time - start_time
    print("Execution time: {:.2f} seconds".format(execution_time))

# Example usage
start_index = 1  # Starting image index
end_index = 4000  # Ending image index
base_path = "outputFrame2"  # Base path of the images
segment_paths = ["segment{}".format(i) for i in range(16)]  # List of segments from "segment0" to "segment15"
stack_images(start_index, end_index, base_path, segment_paths)