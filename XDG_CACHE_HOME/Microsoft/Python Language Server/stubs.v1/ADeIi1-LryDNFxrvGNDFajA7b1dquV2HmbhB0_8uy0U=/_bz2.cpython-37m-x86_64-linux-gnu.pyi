import builtins as _mod_builtins

class BZ2Compressor(_mod_builtins.object):
    'Create a compressor object for compressing data incrementally.\n\n  compresslevel\n    Compression level, as a number between 1 and 9.\n\nFor one-shot compression, use the compress() function instead.'
    __class__ = BZ2Compressor
    def __getstate__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        'Create a compressor object for compressing data incrementally.\n\n  compresslevel\n    Compression level, as a number between 1 and 9.\n\nFor one-shot compression, use the compress() function instead.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def compress(self, data):
        "Provide data to the compressor object.\n\nReturns a chunk of compressed data if possible, or b'' otherwise.\n\nWhen you have finished providing data to the compressor, call the\nflush() method to finish the compression process."
        pass
    
    def flush(self):
        'Finish the compression process.\n\nReturns the compressed data left in internal buffers.\n\nThe compressor object may not be used after this method is called.'
        pass
    

class BZ2Decompressor(_mod_builtins.object):
    'Create a decompressor object for decompressing data incrementally.\n\nFor one-shot decompression, use the decompress() function instead.'
    __class__ = BZ2Decompressor
    def __getstate__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        'Create a decompressor object for decompressing data incrementally.\n\nFor one-shot decompression, use the decompress() function instead.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def decompress(self, data, max_length):
        "Decompress *data*, returning uncompressed data as bytes.\n\nIf *max_length* is nonnegative, returns at most *max_length* bytes of\ndecompressed data. If this limit is reached and further output can be\nproduced, *self.needs_input* will be set to ``False``. In this case, the next\ncall to *decompress()* may provide *data* as b'' to obtain more of the output.\n\nIf all of the input data was decompressed and returned (either because this\nwas less than *max_length* bytes, or because *max_length* was negative),\n*self.needs_input* will be set to True.\n\nAttempting to decompress data after the end of stream is reached raises an\nEOFError.  Any data found after the end of the stream is ignored and saved in\nthe unused_data attribute."
        pass
    
    @property
    def eof(self):
        'True if the end-of-stream marker has been reached.'
        pass
    
    @property
    def needs_input(self):
        'True if more input is needed before more decompressed data can be produced.'
        pass
    
    @property
    def unused_data(self):
        'Data found after the end of the compressed stream.'
        pass
    

__doc__ = None
__file__ = '/usr/lib/python3.7/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_bz2'
__package__ = ''
