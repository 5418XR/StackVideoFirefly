# import cv2
# import numpy as np
# import os
# from concurrent.futures import ThreadPoolExecutor

# def process_image(i, base_path):
#     img_path = base_path + 'keyframe_{}.png'.format(i)

#     # 检查文件是否存在，如果不存在则跳过
#     if not os.path.isfile(img_path):
#         print("Image at path '{}' not found, skipping...".format(img_path))
#         return None

#     img = cv2.imread(img_path)
#     if img is None:
#         print("Failed to read image at path '{}', skipping...".format(img_path))
#         return None

#     return img

# def stack_images(start_index, end_index, base_path, output_path, num_threads=10):
#     stacked_image = None

#     with ThreadPoolExecutor(max_workers=num_threads) as executor:
#         futures = [executor.submit(process_image, i, base_path) for i in range(start_index, end_index+1, 10)]

#         for future in futures:
#             img = future.result()
#             if img is None:
#                 continue

#             if stacked_image is None:
#                 stacked_image = np.zeros_like(img, dtype=np.float32)

#             stacked_image = np.maximum(stacked_image, img)  # 保留每个像素的最大值

#     if stacked_image is None:
#         print("No valid images found!")
#         return

#     # 将数据类型从 float32 转回 uint8（图片）
#     stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)

#     cv2.imwrite(output_path, stacked_image)

# # 使用示例
# start_index = 1  # 起始图片序号
# end_index = 1176  # 结束图片序号
# base_path = "output_frames\\"  # 图片的基本路径
# output_path = "stacked_imageMulty.png"  # 输出图片路径
# num_threads = 10  # 线程数量
# stack_images(start_index, end_index, base_path, output_path, num_threads)
import cv2
import numpy as np
import os
import time
from concurrent.futures import ThreadPoolExecutor

def process_image(i, base_path):
    img_path = base_path + 'keyframe_{}.png'.format(i)

    # 检查文件是否存在，如果不存在则跳过
    if not os.path.isfile(img_path):
        print("Image at path '{}' not found, skipping...".format(img_path))
        return None

    img = cv2.imread(img_path)
    if img is None:
        print("Failed to read image at path '{}', skipping...".format(img_path))
        return None

    return img

def stack_images(start_index, end_index, base_path, output_path, num_threads=10):
    start_time = time.time()

    stacked_image = None

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(process_image, i, base_path) for i in range(start_index, end_index+1, 10)]

        for future in futures:
            img = future.result()
            if img is None:
                continue

            if stacked_image is None:
                stacked_image = np.zeros_like(img, dtype=np.float32)

            stacked_image = np.maximum(stacked_image, img)  # 保留每个像素的最大值

    if stacked_image is None:
        print("No valid images found!")
        return

    # 将数据类型从 float32 转回 uint8（图片）
    stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)

    cv2.imwrite(output_path, stacked_image)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"The program finished in {elapsed_time} seconds.")

# 使用示例
start_index = 1  # 起始图片序号
end_index = 4000  # 结束图片序号
base_path = "output_frames\\"  # 图片的基本路径
output_path = "stacked_imageMulty3.png"  # 输出图片路径
num_threads = 10  # 线程数量
stack_images(start_index, end_index, base_path, output_path, num_threads)