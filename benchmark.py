from compressor import compress_lzma, compress_zlib , compress_bz2
from utils import time_function

def benchmark(data):
    results = {}
    
    algorithms= {
        "LZMA (.xz style)": compress_lzma,
        "ZLIB (gzip style)": compress_zlib,
        "BZ2": compress_bz2
    }
    
    for name, func in algorithms.items():
        compressed, elapsed = time_function(func, data)
        results[name] ={
            "time_sec": elapsed,
            "compressed_size": len(compressed)
        }
    return results