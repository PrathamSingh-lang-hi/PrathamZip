import argparse
from compressor import compress_lzma , decompress_lzma
from benchmark import benchmark
from utils import (
    read_file,
    write_file,
    format_size,
    compression_ratio,
    time_function
)

def main():
    parser=argparse.ArgumentParser(
        description="PrathamZip: A simple file compressor and decompressor using LZMA algorithm"
    )
    
    parser.add_argument(
        "mode",
        choices=["compress", "decompress", "benchmark"]
    )
    
    parser.add_argument("input")
    parser.add_argument("output", nargs="?")
    
    parser.add_argument("--level", type=int, default=9)
    parser.add_argument("--dict", type=int, default=32*1024*1024)
    
    args = parser.parse_args()
    
    data = read_file(args.input)
    
    if args.mode == "compress":
        if not args.output:
            print("Output file is required for compression")
            return
        
        compressed, elapsed =time_function(compress_lzma, data, args.level, args.dict)
        write_file(args.output, compressed)
        
        original_size = len(data)
        compressed_size = len(compressed)   
        
        print("\n--- Compression Status ---")
        print("Time:", elapsed, "seconds")
        print("Original:", format_size(original_size))
        print("Compressed:", format_size(compressed_size))
        print(
            "Reduction:",
            compression_ratio(original_size, compressed_size),
            "%"
        )
    elif args.mode=="decompress":
        if not args.output:
            print("Output file is required for decompression")
            return
        
        decompressed, elapsed =time_function(
            decompress_lzma,
            data
        )
        
        write_file(args.output, decompressed)
        
        print("\nDecompressed successfully")
        print("Time:", elapsed, "seconds")
    elif args.mode == "benchmark":
        results = benchmark(data)
        
        print("\n--- Benchmark Results ---")
        for algo, info in results.items():
            print(f"\n{algo}:")
            print("Time:", info["time_sec"], "sec")
            print("Compressed Size:", format_size(info["compressed_size"]))
            
if __name__ == "__main__":
    main()
    