import builtins as _mod_builtins

BLAKE2B_MAX_DIGEST_SIZE = 64
BLAKE2B_MAX_KEY_SIZE = 64
BLAKE2B_PERSON_SIZE = 16
BLAKE2B_SALT_SIZE = 16
BLAKE2S_MAX_DIGEST_SIZE = 32
BLAKE2S_MAX_KEY_SIZE = 32
BLAKE2S_PERSON_SIZE = 8
BLAKE2S_SALT_SIZE = 8
__doc__ = '_blake2b provides BLAKE2b for hashlib\n'
__file__ = '/usr/lib/python3.7/lib-dynload/_blake2.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_blake2'
__package__ = ''
class blake2b(_mod_builtins.object):
    'Return a new BLAKE2b hash object.'
    MAX_DIGEST_SIZE = 64
    MAX_KEY_SIZE = 64
    PERSON_SIZE = 16
    SALT_SIZE = 16
    __class__ = blake2b
    def __init__(self, *args, **kwargs):
        'Return a new BLAKE2b hash object.'
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
    def block_size(self):
        pass
    
    def copy(self):
        'Return a copy of the hash object.'
        pass
    
    def digest(self):
        'Return the digest value as a bytes object.'
        pass
    
    @property
    def digest_size(self):
        pass
    
    def hexdigest(self):
        'Return the digest value as a string of hexadecimal digits.'
        pass
    
    @property
    def name(self):
        pass
    
    def update(self, data):
        "Update this hash object's state with the provided bytes-like object."
        pass
    

class blake2s(_mod_builtins.object):
    'Return a new BLAKE2s hash object.'
    MAX_DIGEST_SIZE = 32
    MAX_KEY_SIZE = 32
    PERSON_SIZE = 8
    SALT_SIZE = 8
    __class__ = blake2s
    def __init__(self, *args, **kwargs):
        'Return a new BLAKE2s hash object.'
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
    def block_size(self):
        pass
    
    def copy(self):
        'Return a copy of the hash object.'
        pass
    
    def digest(self):
        'Return the digest value as a bytes object.'
        pass
    
    @property
    def digest_size(self):
        pass
    
    def hexdigest(self):
        'Return the digest value as a string of hexadecimal digits.'
        pass
    
    @property
    def name(self):
        pass
    
    def update(self, data):
        "Update this hash object's state with the provided bytes-like object."
        pass
    

