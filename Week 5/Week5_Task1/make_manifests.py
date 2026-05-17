import os

# Get script's directory
base_dir = os.path.dirname(os.path.abspath(__file__))

def generate_manifest(split_name, filename):
    folder = os.path.join(base_dir, "images", split_name)
    if not os.path.exists(folder):
        print(f"Directory {folder} does not exist. Skipping {filename}.")
        return
    
    files = sorted([f for f in os.listdir(folder) if f.endswith(".jpg")])
    filepath = os.path.join(base_dir, filename)
    
    with open(filepath, "w") as f:
        for fname in files:
            # Write relative path from the dataset directory (where data.yaml is)
            f.write(f"images/{split_name}/{fname}\n")
            
    print(f"{filename} created with {len(files)} entries.")

# Generate manifests
generate_manifest("train", "train.txt")
generate_manifest("val", "val.txt")
generate_manifest("test", "test.txt")
