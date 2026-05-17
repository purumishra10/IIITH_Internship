import subprocess
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(SCRIPT_DIR, "raw_video.mp4")
output_dir = os.path.join(SCRIPT_DIR, "all_frames")
os.makedirs(output_dir, exist_ok=True)

command = [
    "ffmpeg",
    "-i", video_path,
    "-vf", "fps=10",
    os.path.join(output_dir, "frame_%04d.jpg")
]

subprocess.run(command)
print("Frame extraction complete.")
print(f"Frames saved to: {output_dir}")