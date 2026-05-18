import os
import subprocess

input_base  = r"D:\Puru_VNR\Projects\IIITH\Internship\Week5_Task1"
output_base = r"D:\Puru_VNR\Projects\IIITH\Internship\Week5_Task2"

splits = ["train", "val", "test"]

for split in splits:
    input_dir  = os.path.join(input_base, "images", split)
    output_dir = os.path.join(output_base, "images_resized", split)
    os.makedirs(output_dir, exist_ok=True)

    images = sorted([f for f in os.listdir(input_dir) if f.endswith(".jpg")])
    print(f"\nResizing {len(images)} images in {split}...")

    for i, fname in enumerate(images):
        input_path  = os.path.join(input_dir, fname)
        output_path = os.path.join(output_dir, fname)

        subprocess.run([
            "ffmpeg",
            "-i", input_path,
            "-vf", "scale=384:-1",
            "-q:v", "2",
            output_path,
            "-y",
            "-loglevel", "error"
        ])

        if (i + 1) % 20 == 0:
            print(f"  {i+1}/{len(images)} done...")

    print(f"{split} done — {len(images)} images saved.")

print("\nAll splits resized successfully!")