import os
import shutil
import filecmp

source_dir = "D:\Projects\GTA Mods\Silent Car Crashes\pedfiles"
destination_dir = "D:\Projects\GTA Mods\Silent Car Crashes\PED AUDIO Folders\PED AUDIO MALE"

for root, dirs, files in os.walk(destination_dir):
    for filename in files:
        # Get the full path of the destination file
        destination_file = os.path.join(root, filename)
        # Get the full path of the source file
        source_file = os.path.join(source_dir, filename)

        # Check if the source file exists and if it's different than the destination file
        if os.path.exists(source_file) and not filecmp.cmp(source_file, destination_file):
            # Copy the source file to the destination folder
            shutil.copy2(source_file, root)
            print(f"{filename} has been replaced in {root}")