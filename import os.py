import os

label_dir = "D:/Yolov7n/Yolov7n/train/labels/"

for file in os.listdir(label_dir):
    if file.endswith(".txt"):
        path = os.path.join(label_dir, file)
        with open(path, "r") as f:
            lines = f.readlines()
        unique_lines = list(set(lines))  # Elimina duplicados
        if len(lines) != len(unique_lines):
            print(f"Cleaning duplicates in {file}")
        with open(path, "w") as f:
            f.writelines(unique_lines)
