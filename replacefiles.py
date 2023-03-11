import os
import shutil
import customtkinter

def replace_files(source_dir_var, destination_dir_var, button):
    source_dir = source_dir_var.get()
    destination_dir = destination_dir_var.get()
    for root, dirs, files in os.walk(destination_dir):
        for filename in files:
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(root, filename)
            if os.path.isfile(source_file):
                shutil.copyfile(source_file, destination_file)
                button.configure(text="Working...")
                print(f"{filename} has been replaced in {destination_file}")