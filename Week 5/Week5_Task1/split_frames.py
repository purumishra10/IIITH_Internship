import os
import shutil

base = os.path.dirname(os.path.abspath(__file__))
all_frames_dir = os.path.join(base, "all_frames")
train_dir = os.path.join(base, "images", "train")
val_dir   = os.path.join(base, "images", "val")
test_dir  = os.path.join(base, "images", "test")

# Get all frames sorted by name
all_frames = sorted([f for f in os.listdir(all_frames_dir) if f.endswith(".jpg")])
total = len(all_frames)
print(f"Total frames found: {total}")

train_frames = []
val_frames   = []
test_frames  = []

for i, fname in enumerate(all_frames):
    if i % 6 == 0 and len(train_frames) < 100:
        train_frames.append(fname)
    elif i % 6 == 3 and len(val_frames) < 40:
        val_frames.append(fname)
    else:
        test_frames.append(fname)

# Copy to respective folders
def copy_frames(frame_list, src_dir, dst_dir, split_name):
    for fname in frame_list:
        shutil.copy(os.path.join(src_dir, fname), os.path.join(dst_dir, fname))
    print(f"{split_name}: {len(frame_list)} frames copied")

copy_frames(train_frames, all_frames_dir, train_dir, "Train")
copy_frames(val_frames,   all_frames_dir, val_dir,   "Val")
copy_frames(test_frames,  all_frames_dir, test_dir,  "Test")

print("\nDone! Summary:")
print(f"  Train : {len(train_frames)} images")
print(f"  Val   : {len(val_frames)} images")
print(f"  Test  : {len(test_frames)} images")
print(f"  Total : {len(train_frames)+len(val_frames)+len(test_frames)}")