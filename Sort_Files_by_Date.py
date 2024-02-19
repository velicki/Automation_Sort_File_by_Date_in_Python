import os
import shutil
import sys
from datetime import datetime

def is_valid_folder_path(path):
    return os.path.isdir(path)

def sort_files_by_modified_date(source_folder, destination_folder):
    
    file_count = 0
    folder_count = 0
    num_files_in_folder = 0
    max_num_files_in_folder = 0

    # Get a list of all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for file in files:
        file_count += 1
        num_files_in_folder += 1

        file_path = os.path.join(source_folder, file)

        # Get the modification time of the file
        modification_time = os.path.getmtime(file_path)
        modification_date = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d')

        # Create the destination folder if it doesn't exist
        dest_folder = os.path.join(destination_folder, modification_date)
        if not os.path.exists(dest_folder):
            if num_files_in_folder > max_num_files_in_folder:
                max_num_files_in_folder = num_files_in_folder
            num_files_in_folder = 0
            os.makedirs(dest_folder)
            folder_count += 1

        # Move the file to the destination folder
        shutil.move(file_path, os.path.join(dest_folder, file))
        print(f"Moved {file} to {dest_folder}")
    return file_count, folder_count, max_num_files_in_folder

if __name__ == "__main__":
    source_folder = input("Enter source folder path ")
    if not is_valid_folder_path(source_folder):
        print(f"Source folder: {source_folder} is not a valid folder path.")
        sys.exit()

    destination_folder = input("Enter destination folder path ")
    if not is_valid_folder_path(destination_folder):
        print(f"Destination folder: {destination_folder} is not a valid folder path.")
        sys.exit()

    file_count, folder_count, max_num_files_in_folder = sort_files_by_modified_date(source_folder, destination_folder)
    print(f"Number of created folders: {folder_count}")
    print(f"Number of file moved into the folders: {file_count}")
    print(f"The folder with the most files has {max_num_files_in_folder} files in it")
    if folder_count == 0:
        print("Avereg nuber of files per folders are: 0")
    else:
        print(f"Avereg nuber of files per folders are: {file_count / folder_count}")
