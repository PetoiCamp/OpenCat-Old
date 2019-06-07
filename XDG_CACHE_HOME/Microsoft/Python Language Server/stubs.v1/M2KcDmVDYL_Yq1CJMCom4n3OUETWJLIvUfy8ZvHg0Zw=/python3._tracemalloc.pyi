__doc__ = 'Debug module to trace memory blocks allocated by Python.'
__name__ = '_tracemalloc'
__package__ = ''
def _get_object_traceback(obj):
    'Get the traceback where the Python object obj was allocated.\n\nReturn a tuple of (filename: str, lineno: int) tuples.\nReturn None if the tracemalloc module is disabled or did not\ntrace the allocation of the object.'
    pass

def _get_traces():
    'Get traces of all memory blocks allocated by Python.\n\nReturn a list of (size: int, traceback: tuple) tuples.\ntraceback is a tuple of (filename: str, lineno: int) tuples.\n\nReturn an empty list if the tracemalloc module is disabled.'
    pass

def clear_traces():
    'Clear traces of memory blocks allocated by Python.'
    pass

def get_traceback_limit():
    'Get the maximum number of frames stored in the traceback of a trace.\n\nBy default, a trace of an allocated memory block only stores\nthe most recent frame: the limit is 1.'
    pass

def get_traced_memory():
    'Get the current size and peak size of memory blocks traced by tracemalloc.\n\nReturns a tuple: (current: int, peak: int).'
    pass

def get_tracemalloc_memory():
    'Get the memory usage in bytes of the tracemalloc module.\n\nThis memory is used internally to trace memory allocations.'
    pass

def is_tracing():
    'Return True if the tracemalloc module is tracing Python memory allocations.'
    pass

def start(nframe):
    'Start tracing Python memory allocations.\n\nAlso set the maximum number of frames stored in the traceback of a\ntrace to nframe.'
    pass

def stop():
    'Stop tracing Python memory allocations.\n\nAlso clear traces of memory blocks allocated by Python.'
    pass

