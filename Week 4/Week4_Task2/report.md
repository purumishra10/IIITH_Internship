# Project Report: Car Traffic Detection System (Week 4 Task 2)

## 📌 Objective
Detect cars in traffic in real-world video footage using the **YOLOv8** object detection framework. This involved building a fully labeled dataset from scratch using **Label Studio**.

---

## ⚙️ Steps Performed
- **Environment Setup**: Installed Label Studio in an isolated Python virtual environment (`ls_venv`) separate from the Ultralytics environment.
- **Data Acquisition**: Downloaded real cars footage video from YouTube using `yt-dlp`.
- **Frame Extraction**: Extracted frames from the video at 10 fps using `FFmpeg`, generating ~600 images stored in `all_frames/`.
- **Dataset Splitting**: Wrote a Python script (`split_frames.py`) to automatically distribute frames:
    - **100** to train
    - **40** to val
    - Remainder to test (ensuring temporal separation between splits).
- **Annotation**: Labeled all 100 training images and 40 validation images in Label Studio using bounding boxes around every visible car in each frame.
- **Data Export**: Exported annotations from Label Studio in YOLO format (`.txt` files with normalized class `cx`, `cy`, `w`, `h` values).
- **Label Organization**: Placed label files into `labels/train/` and `labels/val/` matching their corresponding images.
- **Configuration**: Created `data.yaml` with dataset path, split directories, class count, and class name.
- **Manifest Generation**: Generated `train.txt` and `val.txt` using a Python script (`make_txts.py`) listing absolute paths to all images in each split.
- **Version Control**: Pushed all metadata files (labels, yaml, txt files) to GitHub, excluding raw images and video using `.gitignore`.

---

## 📊 Observations
- **Classes**: Dataset contains 2 classes: `car` and `truck`.
- **Label Statistics**: Total labeled images: **140** (100 train + 40 val).
- **Diversity**: Frames were selected at regular intervals across the video timeline to ensure visual diversity in lighting, angle, and car position.
- **Quality Control**: Label quality was maintained by drawing tight bounding boxes around car bodies, skipping frames where cars were absent or too blurry to identify.
- **Storage**: Images are intentionally excluded from the GitHub repo due to size constraints — they remain locally in `images/train/`, `images/val/`, and `images/test/`.

---

## 📁 Files & Structure
- `images/` — Extracted and split frames (train / val / test), stored locally.
- `labels/` — YOLO format `.txt` annotation files for train and val splits.
- `all_frames/` — All raw extracted frames before splitting, stored locally.
- `data.yaml` — YOLO dataset configuration (path, splits, class names).
- `train.txt` — Absolute paths to all 100 training images.
- `val.txt` — Absolute paths to all 40 validation images.
- `split_frames.py` — Script used to distribute frames across splits.
- `make_txts.py` — Script used to generate `train.txt` and `val.txt`.
- `raw_video.mp4` — Source car footage video, stored locally.
- `.gitignore` — Excludes images, video, and raw frames from version control.

---

## 🔧 Tools Used
- **Label Studio** — Browser-based image annotation tool for drawing bounding boxes.
- **FFmpeg** — Command-line tool for extracting video frames at a specified frame rate.
- **yt-dlp** — Command-line tool for downloading video from YouTube.
- **Python 3.11.9** — Scripting for frame splitting and txt file generation.
- **Git + GitHub** — Version control and remote hosting of dataset metadata.

---

## 🔜 Next Steps
1. **Model Training**: Use `data.yaml` to train a YOLOv8 model on Google Colab (free GPU).
2. **Evaluation**: Evaluate model performance on the test split.
3. **Dataset Expansion**: Expand dataset size for improved accuracy — more labeled images generally lead to better detection.