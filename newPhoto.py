import cv2
import numpy as np

def stack_images(start_index, end_index, base_path, output_path):
    image_paths = [base_path + 'keyframe_{}.png'.format(i) for i in range(start_index, end_index+1, 1)]
    images = [cv2.imread(x) for x in image_paths]

    # 假设所有图片的大小都是相同的
    stacked_image = np.zeros_like(images[0], dtype=np.float32)

    for img in images:
        stacked_image = np.maximum(stacked_image, img)   # 平均每个像素

    # 将数据类型从 float32 转回 uint8（图片）
    stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)

    cv2.imwrite(output_path, stacked_image)

# 使用示例
start_index = 1  # 起始图片序号
end_index = 1176  # 结束图片序号
base_path = "output_frames\\"  # 图片的基本路径
output_path = "stacked_image.png"  # 输出图片路径
stack_images(start_index, end_index, base_path, output_path)

