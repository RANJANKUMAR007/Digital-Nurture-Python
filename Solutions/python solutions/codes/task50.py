import os
import shutil

def log_message(msg):
    with open("backup.log", "a") as log_file:
        log_file.write(msg + "\n")

def backup_files(src_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            log_message(f"Created destination directory: {dest_dir}")
        
        src_files = set(os.listdir(src_dir))
        dest_files = set(os.listdir(dest_dir))
        
        for file in src_files:
            src_path = os.path.join(src_dir, file)
            dest_path = os.path.join(dest_dir, file)
            
            if os.path.isdir(src_path):
                continue
            
            if file in dest_files:
                log_message(f"Skipped duplicate: {file}")
                continue
            
            shutil.copy2(src_path, dest_path)
            log_message(f"Successfully copied: {file}")
            
    except FileNotFoundError as e:
        log_message(f"Error: {e}")
        print(f"Error: Directory not found. {e}")
    except PermissionError as e:
        log_message(f"Error: {e}")
        print(f"Error: Permission denied. {e}")

os.makedirs("src_test", exist_ok=True)
with open("src_test/file1.txt", "w") as f:
    f.write("hello")
with open("src_test/file2.txt", "w") as f:
    f.write("world")

os.makedirs("dest_test", exist_ok=True)
with open("dest_test/file1.txt", "w") as f:
    f.write("hello")

backup_files("src_test", "dest_test")
