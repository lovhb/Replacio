import os
import shutil

def replace_files(source_dir_var, destination_dir_var):
    # Copies files from source directory to destination directory, replacing any existing files with the same name and skipping any file that doesn't match an existing file.
    
    # Get the source and destination directories from the StringVars
    source_dir = source_dir_var.get()
    destination_dir = destination_dir_var.get()
    
    # Loop through the files in the destination directory
    for root, dirs, files in os.walk(destination_dir):
        for filename in files:
            # Create paths to the source and destination files
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(root, filename)
            
            # If the source file exists and is a file (not a directory), replace the source file with it
            if os.path.isfile(source_file) and os.path.exists(destination_file):
                try:
                    shutil.copyfile(source_file, destination_file)
                    print(f"{filename} has been replaced in {destination_file}")
                except (FileNotFoundError, PermissionError) as e:
                    print(f"Error occurred while replacing {filename}: {e}")
            else:
                print(f"{filename} not found in {source_dir} or {destination_file} not found in {destination_dir}")

def copy_files(source_dir_var, destination_dir_var):
    # Copies files from the source directory to each folder in the destination directory.
    
    # Get the source and destination directories from the StringVars
    source_dir = source_dir_var.get()
    destination_dir = destination_dir_var.get()
    
    # Loop through the folders in the destination directory
    for foldername in os.listdir(destination_dir):
        # If the folder is actually a directory, copy files from the source directory to it
        if os.path.isdir(os.path.join(destination_dir, foldername)):
            destination = os.path.join(destination_dir, foldername)
            for filename in os.listdir(source_dir):
                source = os.path.join(source_dir, filename)
                # If the file exists and is a file (not a directory), copy it to the destination folder
                if os.path.isfile(source) and os.path.exists(destination):
                    try:
                        shutil.copy2(source, destination)
                        print(f"{filename} has been copied to {destination}")
                    except (FileNotFoundError, PermissionError) as e:
                        print(f"Error occurred while copying {filename}: {e}")
                else:
                    print(f"{filename} not found in {source_dir} or {destination} not found in {destination_dir}")