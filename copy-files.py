import os
import shutil

source_dir = "C:\Users\loveb\Desktop\Source"
destination_dir = "C:\Users\loveb\Desktop\Destination"

for foldername in os.listdir(destination_dir):
    if os.path.isdir(os.path.join(destination_dir, foldername)):
        destination = os.path.join(destination_dir, foldername)
        for filename in os.listdir(source_dir):
            source = os.path.join(source_dir, filename)
            if os.path.isfile(source):
                shutil.copy2(source, destination)