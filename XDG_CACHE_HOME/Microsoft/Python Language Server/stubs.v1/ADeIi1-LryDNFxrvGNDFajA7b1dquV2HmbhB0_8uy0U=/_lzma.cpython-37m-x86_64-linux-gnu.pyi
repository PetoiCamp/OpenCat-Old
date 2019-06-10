import builtins as _mod_builtins

CHECK_CRC32 = 1
CHECK_CRC64 = 4
CHECK_ID_MAX = 15
CHECK_NONE = 0
CHECK_SHA256 = 10
CHECK_UNKNOWN = 16
FILTER_ARM = 7
FILTER_ARMTHUMB = 8
FILTER_DELTA = 3
FILTER_IA64 = 6
FILTER_LZMA1 = 4611686018427387905
FILTER_LZMA2 = 33
FILTER_POWERPC = 5
FILTER_SPARC = 9
FILTER_X86 = 4
FORMAT_ALONE = 2
FORMAT_AUTO = 0
FORMAT_RAW = 3
FORMAT_XZ = 1
class LZMACompressor(_mod_builtins.object):
    'LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)\n\nCreate a compressor object for compressing data incrementally.\n\nformat specifies the container format to use for the output. This can\nbe FORMAT_XZ (default), FORMAT_ALONE, or FORMAT_RAW.\n\ncheck specifies the integrity check to use. For FORMAT_XZ, the default\nis CHECK_CRC64. FORMAT_ALONE and FORMAT_RAW do not support integrity\nchecks; for these formats, check must be omitted, or be CHECK_NONE.\n\nThe settings used by the compressor can be specified either as a\npreset compression level (with the \'preset\' argument), or in detail\nas a custom filter chain (with the \'filters\' argument). For FORMAT_XZ\nand FORMAT_ALONE, the default is to use the PRESET_DEFAULT preset\nlevel. For FORMAT_RAW, the caller must always specify a filter chain;\nthe raw compressor does not support preset compression levels.\n\npreset (if provided) should be an integer in the range 0-9, optionally\nOR-ed with the constant PRESET_EXTREME.\n\nfilters (if provided) should be a sequence of dicts. Each dict should\nhave an entry for "id" indicating the ID of the filter, plus\nadditional entries for options to the filter.\n\nFor one-shot compression, use the compress() function instead.\n'
    __class__ = LZMACompressor
    def __getstate__(self):
        pass
    
    def __init__(self, format=FORMAT_XZ, check=-1, preset=None, filters=None):
        'LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)\n\nCreate a compressor object for compressing data incrementally.\n\nformat specifies the container format to use for the output. This can\nbe FORMAT_XZ (default), FORMAT_ALONE, or FORMAT_RAW.\n\ncheck specifies the integrity check to use. For FORMAT_XZ, the default\nis CHECK_CRC64. FORMAT_ALONE and FORMAT_RAW do not support integrity\nchecks; for these formats, check must be omitted, or be CHECK_NONE.\n\nThe settings used by the compressor can be specified either as a\npreset compression level (with the \'preset\' argument), or in detail\nas a custom filter chain (with the \'filters\' argument). For FORMAT_XZ\nand FORMAT_ALONE, the default is to use the PRESET_DEFAULT preset\nlevel. For FORMAT_RAW, the caller must always specify a filter chain;\nthe raw compressor does not support preset compression levels.\n\npreset (if provided) should be an integer in the range 0-9, optionally\nOR-ed with the constant PRESET_EXTREME.\n\nfilters (if provided) should be a sequence of dicts. Each dict should\nhave an entry for "id" indicating the ID of the filter, plus\nadditional entries for options to the filter.\n\nFor one-shot compression, use the compress() function instead.\n'
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
    

class LZMADecompressor(_mod_builtins.object):
    'Create a decompressor object for decompressing data incrementally.\n\n  format\n    Specifies the container format of the input stream.  If this is\n    FORMAT_AUTO (the default), the decompressor will automatically detect\n    whether the input is FORMAT_XZ or FORMAT_ALONE.  Streams created with\n    FORMAT_RAW cannot be autodetected.\n  memlimit\n    Limit the amount of memory used by the decompressor.  This will cause\n    decompression to fail if the input cannot be decompressed within the\n    given limit.\n  filters\n    A custom filter chain.  This argument is required for FORMAT_RAW, and\n    not accepted with any other format.  When provided, this should be a\n    sequence of dicts, each indicating the ID and options for a single\n    filter.\n\nFor one-shot decompression, use the decompress() function instead.'
    __class__ = LZMADecompressor
    def __getstate__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        'Create a decompressor object for decompressing data incrementally.\n\n  format\n    Specifies the container format of the input stream.  If this is\n    FORMAT_AUTO (the default), the decompressor will automatically detect\n    whether the input is FORMAT_XZ or FORMAT_ALONE.  Streams created with\n    FORMAT_RAW cannot be autodetected.\n  memlimit\n    Limit the amount of memory used by the decompressor.  This will cause\n    decompression to fail if the input cannot be decompressed within the\n    given limit.\n  filters\n    A custom filter chain.  This argument is required for FORMAT_RAW, and\n    not accepted with any other format.  When provided, this should be a\n    sequence of dicts, each indicating the ID and options for a single\n    filter.\n\nFor one-shot decompression, use the decompress() function instead.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def check(self):
        'ID of the integrity check used by the input stream.'
        pass
    
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
    

class LZMAError(_mod_builtins.Exception):
    'Call to liblzma failed.'
    __class__ = LZMAError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Call to liblzma failed.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_lzma'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

MF_BT2 = 18
MF_BT3 = 19
MF_BT4 = 20
MF_HC3 = 3
MF_HC4 = 4
MODE_FAST = 1
MODE_NORMAL = 2
PRESET_DEFAULT = 6
PRESET_EXTREME = 2147483648
__doc__ = None
__file__ = '/usr/lib/python3.7/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_lzma'
__package__ = ''
def _decode_filter_properties(filter_id, encoded_props):
    'Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).\n\nThe result does not include the filter ID itself, only the options.'
    pass

def _encode_filter_properties(filter):
    'Return a bytes object encoding the options (properties) of the filter specified by *filter* (a dict).\n\nThe result does not include the filter ID itself, only the options.'
    pass

def is_check_supported(check_id):
    'Test whether the given integrity check is supported.\n\nAlways returns True for CHECK_NONE and CHECK_CRC32.'
    pass

