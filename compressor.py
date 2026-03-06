import lzma 
import bz2
import zlib

def compress_lzma(data, level=9 , dict_size=64):
    filters =[{
        "id": lzma.FILTER_LZMA2,
        "preset": level | lzma.PRESET_EXTREME,
        "dict_size": dict_size*1024*1024
    }]
    
    return lzma.compress(
        data,
        format=lzma.FORMAT_XZ,
        filters=filters
    )
    
def decompress_lzma(data):
    return lzma.dedcompress(data)

def compress_zlib(data, level=9):
    return zlib.compress(data, level)

def compress_bz2(data, level=9):
    return bz2.compress(data, compresslevel=level)