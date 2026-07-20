import os
import shutil

folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"]
}

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        for category, extensions in file_types.items():
            if extension in extensions:
                destination = os.path.join(folder, category)

                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, file))
                print(f"Moved {file} to {category}")
                break

print("File organization completed.")
