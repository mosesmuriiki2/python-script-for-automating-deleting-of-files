import os
import send2trash
from datetime import datetime, timedelta

downloads_path = os.path.expanduser("~\\")
current_time = datetime.now()
time_threshold = current_time - timedelta(hours=72)

for root, dirs, files in os.walk(downloads_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path):
            deletion_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if deletion_time >= time_threshold:
                send2trash.send2trash(file_path)
                print(f"Restored: {file_path}")
