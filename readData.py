import cv2
import os

# 打开视频文件
video = cv2.VideoCapture('C0043.mp4')  # 替换为你的视频文件路径

frame_count = 0
keyframes = []

output_directory = "output_frames"  # 输出关键帧的文件夹路径
if not os.path.exists(output_directory):  # 如果文件夹不存在，则创建文件夹
    os.makedirs(output_directory)

while True:
    # 读取下一帧
    ret, frame = video.read()

    # 如果读取失败（例如已经到了视频末尾），则退出循环
    if not ret:
        break

    # 获取当前帧的ID
    frame_id = int(video.get(cv2.CAP_PROP_POS_FRAMES))

    # 获取当前帧是否为关键帧
    is_keyframe = int(video.get(cv2.CAP_PROP_POS_FRAMES))

    if is_keyframe:
        output_path = os.path.join(output_directory, f"keyframe_{frame_id}.png")  # 输出图像的路径
        cv2.imwrite(output_path, frame)  # 将帧保存为图像文件
        print(f'关键帧 ID: {frame_id} 已保存为 {output_path}')

    frame_count += 1

# 关闭视频文件
video.release()
