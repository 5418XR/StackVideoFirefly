# import cv2
# import os
# import concurrent.futures
# import glob

# def process_video(video_path):
#     video = cv2.VideoCapture(video_path)
#     frame_count = 0
#     keyframes = []

#     output_directory = f"output_frames_{os.path.basename(video_path).split('.')[0]}"  # create a unique output folder per video
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     while True:
#         ret, frame = video.read()
#         if not ret:
#             break

#         frame_id = int(video.get(cv2.CAP_PROP_POS_FRAMES))
#         is_keyframe = int(video.get(cv2.CAP_PROP_POS_FRAMES))

#         if is_keyframe:
#             output_path = os.path.join(output_directory, f"keyframe_{frame_id}.png")
#             cv2.imwrite(output_path, frame)
#             print(f'关键帧 ID: {frame_id} 已保存为 {output_path}')

#         frame_count += 1

#     video.release()

# # get the list of all mp4 files in the 'outputvideos' directory
# videos = glob.glob('outputvideos/segment_*.mp4')

# # use a ThreadPoolExecutor to process multiple videos concurrently
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(process_video, videos)
# import cv2
# import os
# import concurrent.futures
# import glob

# def process_video(video_path, output_directory):
#     video = cv2.VideoCapture(video_path)
#     frame_count = 0

#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     while True:
#         ret, frame = video.read()
#         if not ret:
#             break

#         frame_id = int(video.get(cv2.CAP_PROP_POS_FRAMES))

#         # assuming every frame is a keyframe for this example
#         output_path = os.path.join(output_directory, f"keyframe_{frame_id}.png")
#         cv2.imwrite(output_path, frame)
#         print(f'Keyframe ID: {frame_id} has been saved as {output_path}')

#         frame_count += 1

#     video.release()

# # get the list of all mp4 files in the 'outputvideos' directory
# videos = glob.glob('outputvideos/segment_*.mp4')

# # Specify your custom output directory here
# custom_output_directory = "output_frames1"  # 输出关键帧的文件夹路径
# if not os.path.exists(custom_output_directory):  # 如果文件夹不存在，则创建文件夹
#     os.makedirs(custom_output_directory)

# # use a ThreadPoolExecutor to process multiple videos concurrently
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(lambda video: process_video(video, custom_output_directory), videos)
import cv2
import os
import concurrent.futures
import glob

def process_video(video_path, output_directory):
    video = cv2.VideoCapture(video_path)
    frame_count = 0

    # Create a unique directory for each video
    video_directory = os.path.join(output_directory, os.path.basename(video_path).split('.')[0])
    if not os.path.exists(video_directory):
        os.makedirs(video_directory)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame_id = int(video.get(cv2.CAP_PROP_POS_FRAMES))

        # assuming every frame is a keyframe for this example
        output_path = os.path.join(video_directory, f"keyframe_{frame_id}.png")
        cv2.imwrite(output_path, frame)
        print(f'Keyframe ID: {frame_id} has been saved as {output_path}')

        frame_count += 1

    video.release()

# get the list of all mp4 files in the 'outputvideos' directory
videos = glob.glob('outputvideos/segment_*.mp4')

# Specify your custom output directory here
custom_output_directory = "outputFrame" 

# use a ThreadPoolExecutor to process multiple videos concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(lambda video: process_video(video, custom_output_directory), videos)
