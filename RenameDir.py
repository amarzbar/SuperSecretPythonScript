import os
import shutil
from pathlib import Path

def list_files(directory):
    files = (entry for entry in os.scandir(directory) if entry.is_file())
    return sorted(files, key=lambda file: file.stat().st_ctime)

def rename_files(directory):
    files = list_files(directory)
    for idx, file in enumerate(files, start=1):
        new_name = f"{idx:04d}{Path(file.name).suffix}"
        os.rename(file.path, os.path.join(directory, new_name))

if __name__ == "__main__":
    directory = "."  # Current directory
    rename_files(directory)
