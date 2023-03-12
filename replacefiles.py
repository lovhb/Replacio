import os
import shutil

def replace_files(source_dir_var, destination_dir_var):
    source_dir = source_dir_var.get()
    destination_dir = destination_dir_var.get()
    for root, dirs, files in os.walk(destination_dir):
        for filename in files:
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(root, filename)
            if os.path.isfile(source_file):
                shutil.copyfile(source_file, destination_file)
                print(f"{filename} has been replaced in {destination_file}")

def copy_files(source_dir_var, destination_dir_var):
    source_dir = source_dir_var.get()
    destination_dir = destination_dir_var.get()
    for foldername in os.listdir(destination_dir):
        if os.path.isdir(os.path.join(destination_dir, foldername)):
            destination = os.path.join(destination_dir, foldername)
            for filename in os.listdir(source_dir):
                source = os.path.join(source_dir, filename)
                if os.path.isfile(source):
                    shutil.copy2(source, destination)
                    print(f"{filename} has been copied to {destination}")