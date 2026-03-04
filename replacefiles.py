import os
import shutil

def replace_files(source_dir_var, destination_dir_var, log_func=print):
    # Copies files from source directory to destination directory, replacing any existing files
    # with the same name and skipping any file that doesn't match an existing file.

    source_dir = source_dir_var.get()
    destination_dir = destination_dir_var.get()

    replaced = 0
    skipped = 0

    # Walk the destination tree
    for root, dirs, files in os.walk(destination_dir):
        for filename in files:
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(root, filename)

            if os.path.isfile(source_file):
                try:
                    shutil.copyfile(source_file, destination_file)
                    log_func(f"Replaced: {destination_file}")
                    replaced += 1
                except (FileNotFoundError, PermissionError) as e:
                    log_func(f"Error replacing {filename}: {e}")
                    skipped += 1
            else:
                log_func(f"Skipped (not a regular file in source): {filename}")
                skipped += 1

    return replaced, skipped

def copy_files(source_dir_var, destination_dir_var, log_func=print):
    # Copies files from the source directory to each subfolder in the destination directory.

    source_dir = source_dir_var.get()
    destination_dir = destination_dir_var.get()

    copied = 0
    skipped = 0

    for foldername in os.listdir(destination_dir):
        folder_path = os.path.join(destination_dir, foldername)
        if os.path.isdir(folder_path):
            for filename in os.listdir(source_dir):
                source = os.path.join(source_dir, filename)
                if os.path.isfile(source):
                    try:
                        shutil.copy2(source, folder_path)
                        log_func(f"Copied: {filename} → {folder_path}")
                        copied += 1
                    except (FileNotFoundError, PermissionError) as e:
                        log_func(f"Error copying {filename}: {e}")
                        skipped += 1
                else:
                    log_func(f"Skipped (not a regular file in source): {filename}")
                    skipped += 1

    return copied, skipped