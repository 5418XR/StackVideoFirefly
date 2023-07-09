import os
import numpy as np
from PIL import Image
import h5py

# 如果不存在，创建文件夹
if not os.path.exists('output/'):
    os.makedirs('output/')

# 定义图片路径列表
image_paths = [f'output_frames/keyframe_{i}.png' for i in range(1, 1177)]
 # 大量的图片

# 读取第一张图片以获取基本信息
base_image = Image.open(image_paths[0])
width, height = base_image.size
channels = len(base_image.getbands())

# 创建一个HDF5文件来存储堆叠后的图片
with h5py.File('output/stacked_images.h5', 'w') as f:
    # 创建一个数据集，用于存储堆叠后的图片
    stacked_images = f.create_dataset('stacked_images', (len(image_paths), height, width, channels), dtype='uint8')

    # 将图片逐一读取，转换为numpy数组，然后存储到HDF5文件中
    for i, path in enumerate(image_paths):
        img = Image.open(path)
        # 确保所有图片尺寸一致
        img = img.resize(base_image.size, Image.ANTIALIAS)
        img_np = np.array(img)
        stacked_images[i] = img_np
