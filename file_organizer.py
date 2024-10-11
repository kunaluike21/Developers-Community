import os
import shutil

# Define the directory to organize
directory = "path/to/your/directory"

# Define the mapping of file extensions to folder names
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar.gz", ".7z"]
}

# Create the folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to corresponding folders
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1]
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))

print("Files organized successfully!")
