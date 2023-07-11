
# import subprocess

# def split_xavc(video_path, output_prefix, start_time, duration):
#     output_file_pattern = f"{output_prefix}_%03d.mp4"  # Output file pattern with sequential numbering

    # Run ffmpeg command to split the video
    # command = [
    #     "ffmpeg",
    #     "-i", video_path,
    #     "-ss", start_time,
    #     "-t", duration,
    #     "-c:v", "copy",
    #     "-c:a", "aac",
    #     output_file_pattern
    # ]
    # subprocess.call(command)

# # Example usage
# video_path = "C0043.MP4"
# output_prefix = "outputvideos"
# start_time = "00:00:10"  # Start time in HH:MM:SS format
# duration = "00:01:00"   # Split duration in HH:MM:SS format

# split_xavc(video_path, output_prefix, start_time, duration)


# import subprocess
# import json
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# import math
# import os

# def get_video_duration(video_path):
#     command = [
#         '-i', video_path,
#         '-c:v', 'copy',
#         '-c:a', 'copy',
#         '-segment_time', "duration",
#         '-f', 'segment',
#         '-reset_timestamps', '1',
#         '-map', '0',
#         video_path
#     ]
#     output = subprocess.check_output(command).decode("utf-8")
#     data = json.loads(output)
#     duration = float(data["format"]["duration"])
#     return duration

# # 获取视频的总时长
# video_path = "C0043.mp4"
# duration = get_video_duration(video_path)

# # 计算需要切割的段数
# segment_duration = 5
# num_segments = math.ceil(duration / segment_duration)

# # 获取当前脚本的绝对路径
# current_dir = os.path.dirname(os.path.abspath(__file__))

# for i in range(num_segments):
#     start_time = i * segment_duration
#     end_time = min((i + 1) * segment_duration, duration)  # 确保结束时间不超过视频总时长
#     output_file = os.path.join(current_dir, "outputVideos", f"segment_{i}.mp4")
#     ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=output_file)
import subprocess
import json
import math
import os

def get_video_duration(video_path):
    command = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "format=duration",
        "-of", "json",
        video_path
    ]
    output = subprocess.check_output(command).decode("utf-8")
    data = json.loads(output)
    duration = float(data["format"]["duration"])
    return duration

def extract_and_transcode(video_path, start_time, duration, output_file):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-ss", str(start_time),
        "-t", str(duration),
        "-c:v", "copy",
        "-c:a", "aac",
        output_file
    ]
    subprocess.call(command)

# 获取视频的总时长
video_path = "C0090.mp4"
total_duration = get_video_duration(video_path)

# 计算需要切割的段数
segment_duration = 5
num_segments = math.ceil(total_duration / segment_duration)

# 获取当前脚本的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 创建输出目录
output_dir = os.path.join(current_dir, "outputVideos")
os.makedirs(output_dir, exist_ok=True)

for i in range(num_segments):
    start_time = i * segment_duration
    end_time = min((i + 1) * segment_duration, total_duration)
    segment_duration = end_time - start_time  # 计算实际段长
    output_file = os.path.join(output_dir, f"segment_{i}.mp4")
    extract_and_transcode(video_path, start_time, segment_duration, output_file)

