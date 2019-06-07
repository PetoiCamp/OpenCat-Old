__doc__ = 'This module contains functions that can read and write Python values in\na binary format. The format is specific to Python, but independent of\nmachine architecture issues.\n\nNot all Python object types are supported; in general, only objects\nwhose value is independent from a particular invocation of Python can be\nwritten and read by this module. The following types are supported:\nNone, integers, floating point numbers, strings, bytes, bytearrays,\ntuples, lists, sets, dictionaries, and code objects, where it\nshould be understood that tuples, lists and dictionaries are only\nsupported as long as the values contained therein are themselves\nsupported; and recursive lists and dictionaries should not be written\n(they will cause infinite loops).\n\nVariables:\n\nversion -- indicates the format that the module uses. Version 0 is the\n    historical format, version 1 shares interned strings and version 2\n    uses a binary format for floating point numbers.\n    Version 3 shares common object references (New in version 3.4).\n\nFunctions:\n\ndump() -- write value to a file\nload() -- read value from a file\ndumps() -- marshal value as a bytes object\nloads() -- read value from a bytes-like object'
__name__ = 'marshal'
__package__ = ''
def dump(value, file, version):
    'Write the value on the open file.\n\n  value\n    Must be a supported type.\n  file\n    Must be a writeable binary file.\n  version\n    Indicates the data format that dump should use.\n\nIf the value has (or contains an object that has) an unsupported type, a\nValueError exception is raised - but garbage data will also be written\nto the file. The object will not be properly read back by load().'
    pass

def dumps(value, version):
    'Return the bytes object that would be written to a file by dump(value, file).\n\n  value\n    Must be a supported type.\n  version\n    Indicates the data format that dumps should use.\n\nRaise a ValueError exception if value has (or contains an object that has) an\nunsupported type.'
    pass

def load(file):
    "Read one value from the open file and return it.\n\n  file\n    Must be readable binary file.\n\nIf no valid value is read (e.g. because the data has a different Python\nversion's incompatible marshal format), raise EOFError, ValueError or\nTypeError.\n\nNote: If an object containing an unsupported type was marshalled with\ndump(), load() will substitute None for the unmarshallable type."
    pass

def loads(bytes):
    'Convert the bytes-like object to a value.\n\nIf no valid value is found, raise EOFError, ValueError or TypeError.  Extra\nbytes in the input are ignored.'
    pass

version = 4
