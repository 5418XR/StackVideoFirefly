import subprocess

def split_xavc(video_path, output_prefix, start_time, duration):
    output_file_pattern = f"{output_prefix}_%03d.mp4"  # Output file pattern with sequential numbering

    # Run ffmpeg command to split the video
    command = [
        "ffmpeg",
        "-i", video_path,
        "-ss", start_time,
        "-t", duration,
        "-c", "copy",
        output_file_pattern
    ]
    subprocess.call(command)

# Example usage
video_path = "C0043.mp4"
output_prefix = "outputVideos"
start_time = "00:00:00"  # Start time in HH:MM:SS format
duration = "00:00:05"   # Split duration in HH:MM:SS format

split_xavc(video_path, output_prefix, start_time, duration)