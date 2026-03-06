import os
import time

def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' does not exist.")
    with open (path, "rb") as f:
        return f.read()
    
def write_file(path, data):
    with open(path, "wb") as f:
        f.write(data)
        
def format_size(size_bytes):
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

def compression_ratio(original, compressed):
    return round((1- compressed/original)*100 ,2)

def time_function(func, *args, **kwargs):
    start= time .time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, round (end - start, 4)