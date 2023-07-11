# import subprocess
# import os

# def create_video(image_dir, video_file):
#     # 构建FFmpeg命令
#     command = f'ffmpeg -framerate 1 -i {image_dir}/segmet_%d.png -vf scale=3840:2160 -c:v libx264 -r 30 -pix_fmt yuv420p {video_file}'

#     # 运行命令
#     subprocess.run(command, shell=True)

# if __name__ == "__main__":
#     # 获取当前脚本所在的路径
#     #current_dir = os.path.dirname(os.path.realpath(__file__))

#     # 图片所在的目录，将当前脚本的路径和图片的子路径结合
#     #image_dir = os.path.join(current_dir, 'outputFrame2')
#     image_dir = 'C:\\videoProject\\outputFrame2'

#     # 输出视频文件的路径
#     video_file = os.path.join(current_dir, 'out.mp4')

#     # 创建视频
#     create_video(image_dir, video_file)
# import subprocess
# import os

# def create_video(image_dir, video_file):
#     # 构建FFmpeg命令
#     #command = f"ffmpeg -framerate 1 -i {image_dir}/segment_%d.png -vf \"zoompan=z='zoom+0.001':d=1:x='if(gte(zoom,1.5),x,x-1/a)':y='y':s=3840:-1,framerate=30\" -c:v libx264 -pix_fmt yuv420p -crf 0 {video_file}"
#     command = f"ffmpeg -framerate 1 -i {image_dir}/segment_%d.png -vf \"zoompan=z='zoom+0.001':d=1:x='if(gte(zoom,1.5),x,x-1/a)':y='y',framerate=30\" -c:v libx264 -pix_fmt yuv420p -crf 0 {video_file}"

#     # 运行命令
#     subprocess.run(command, shell=True)

# if __name__ == "__main__":
#     # 图片所在的目录
#     image_dir = 'C:\\videoProject\\outputFrame2'

#     # 输出视频文件的路径
#     video_file = 'C:\\videoProject\\out.mp4'

#     # 创建视频
#     create_video(image_dir, video_file)
# import cv2
# import os

# def make_video(image_folder, video_name, fps):
#     images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg")]
#     # 对图片进行排序，否则视频中的帧可能会乱序
#     images.sort()

#     # 读取第一张图片以获取图像尺寸
#     sample = cv2.imread(os.path.join(image_folder, images[0]))
#     height, width, layers = sample.shape

#     # 创建 VideoWriter 对象
#     video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

#     # 将每张图片写入视频文件
#     for image in images:
#         video.write(cv2.imread(os.path.join(image_folder, image)))

#     cv2.destroyAllWindows()
#     video.release()

# image_folder = 'C:\\videoProject\\outputFrame'  # 输入你的图片文件夹路径
# video_name = 'C:\\videoProject\\out1.mp4'  # 输出的视频文件名
# fps = 1.5 # 视频的帧率，可以根据需要修改

# make_video(image_folder, video_name, fps)
import cv2
import os
import numpy as np

def make_video(image_folder, video_name, fps, transition_frames):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg")]
    images.sort()

    sample = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = sample.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    prev_image = None
    for image in images:
        current_image = cv2.imread(os.path.join(image_folder, image))

        # If this isn't the first image, create transition from previous image
        if prev_image is not None:
            # Generate transition frames
            for t in np.linspace(0, 1, transition_frames):
                transition_image = cv2.addWeighted(prev_image, 1-t, current_image, t, 0)
                video.write(transition_image)

        video.write(current_image)
        prev_image = current_image

    cv2.destroyAllWindows()
    video.release()

image_folder = 'C:\\videoProject\\outputFrame'
video_name = 'C:\\videoProject\\out.mp4'
fps = 24
transition_frames = 10  # Number of frames for transition

make_video(image_folder, video_name, fps, transition_frames)