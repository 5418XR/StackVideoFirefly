import cv2
import numpy as np
import os

def stack_images(start_index, end_index, base_path, output_path):
    stacked_image = None

    for i in range(start_index, end_index+1, 1):
        img_path = base_path + 'keyframe_{}.png'.format(i)
        
        # 检查文件是否存在，如果不存在则跳过
        if not os.path.isfile(img_path):
            print("Image at path '{}' not found, skipping...".format(img_path))
            continue

        img = cv2.imread(img_path)
        if img is None:
            print("Failed to read image at path '{}', skipping...".format(img_path))
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

# 使用示例
start_index = 1  # 起始图片序号
end_index = 4000  # 结束图片序号
base_path = "output_frames\\"  # 图片的基本路径
output_path = "stacked_image7.png"  # 输出图片路径
stack_images(start_index, end_index, base_path, output_path)

