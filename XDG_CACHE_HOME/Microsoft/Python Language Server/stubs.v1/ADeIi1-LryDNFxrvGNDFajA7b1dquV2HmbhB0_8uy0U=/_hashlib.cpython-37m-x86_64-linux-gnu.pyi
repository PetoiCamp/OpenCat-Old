import builtins as _mod_builtins

class HASH(_mod_builtins.object):
    'A hash represents the object used to calculate a checksum of a\nstring of information.\n\nMethods:\n\nupdate() -- updates the current digest with an additional string\ndigest() -- return the current digest value\nhexdigest() -- return the current digest as a string of hexadecimal digits\ncopy() -- return a copy of the current hash object\n\nAttributes:\n\nname -- the hash algorithm being used by this object\ndigest_size -- number of bytes in this hashes output\n'
    __class__ = HASH
    def __init__(self, *args, **kwargs):
        'A hash represents the object used to calculate a checksum of a\nstring of information.\n\nMethods:\n\nupdate() -- updates the current digest with an additional string\ndigest() -- return the current digest value\nhexdigest() -- return the current digest as a string of hexadecimal digits\ncopy() -- return a copy of the current hash object\n\nAttributes:\n\nname -- the hash algorithm being used by this object\ndigest_size -- number of bytes in this hashes output\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
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
        'algorithm name.'
        pass
    
    def update(self):
        "Update this hash object's state with the provided string."
        pass
    

__doc__ = None
__file__ = '/usr/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_hashlib'
__package__ = ''
def hmac_digest(key, msg, digest):
    'Single-shot HMAC.'
    pass

def new():
    'Return a new hash object using the named algorithm.\nAn optional string argument may be provided and will be\nautomatically hashed.\n\nThe MD5 and SHA1 algorithms are always supported.\n'
    pass

def openssl_md5():
    'Returns a md5 hash object; optionally initialized with a string'
    pass

openssl_md_meth_names = _mod_builtins.frozenset()
def openssl_sha1():
    'Returns a sha1 hash object; optionally initialized with a string'
    pass

def openssl_sha224():
    'Returns a sha224 hash object; optionally initialized with a string'
    pass

def openssl_sha256():
    'Returns a sha256 hash object; optionally initialized with a string'
    pass

def openssl_sha384():
    'Returns a sha384 hash object; optionally initialized with a string'
    pass

def openssl_sha512():
    'Returns a sha512 hash object; optionally initialized with a string'
    pass

def pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None):
    'pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) -> key\n\nPassword based key derivation function 2 (PKCS #5 v2.0) with HMAC as\npseudorandom function.'
    pass

def scrypt(password):
    'scrypt password-based key derivation function.'
    pass

