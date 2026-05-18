import os

base = r"D:\Puru_VNR\Projects\IIITH\Internship\Week5_Task2"

for split in ["train", "val", "test"]:
    folder = os.path.join(base, "images_resized", split)
    out_path = os.path.join(base, split + ".txt")
    files = sorted([f for f in os.listdir(folder) if f.endswith(".jpg")])
    with open(out_path, "w") as f:
        for fname in files:
            f.write(base.replace("\\", "/") + "/images_resized/" + split + "/" + fname + "\n")
    print(split + ".txt updated with " + str(len(files)) + " entries")