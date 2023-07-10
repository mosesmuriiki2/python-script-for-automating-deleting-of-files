import os
import time

folder_path = r"C:\Users\Moses\Downloads"
threshold_days = 60

# Get the current timestamp
current_time = time.time()

# Iterate over the files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Check if the file is a regular file (not a folder or symlink)
    if os.path.isfile(file_path):

        # Get the last modified timestamp of the file
        last_modified_time = os.path.getmtime(file_path)

        # Calculate the difference in days
        time_diff_days = (current_time - last_modified_time) / (24 * 365 * 365)

        # Delete the file if it exceeds the threshold days
        if time_diff_days >= threshold_days:
            os.remove(file_path)
            print(f"Deleted file: {file_name}")
