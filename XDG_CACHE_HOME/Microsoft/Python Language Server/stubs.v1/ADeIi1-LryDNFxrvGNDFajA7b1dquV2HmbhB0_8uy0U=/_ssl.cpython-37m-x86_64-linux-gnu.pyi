class tuple(object):
    "Built-in immutable sequence.\n\nIf no argument is given, the constructor returns an empty tuple.\nIf iterable is specified the tuple is initialized from iterable's items.\n\nIf the argument is a tuple, the return value is the same object."
    def __add__(self, value):
        'Return self+value.'
        return tuple()
    
    __class__ = tuple
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __getnewargs__(self):
        return ()
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        "Built-in immutable sequence.\n\nIf no argument is given, the constructor returns an empty tuple.\nIf iterable is specified the tuple is initialized from iterable's items.\n\nIf the argument is a tuple, the return value is the same object."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return tuple()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return tuple()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return tuple()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def count(self, value):
        'Return number of occurrences of value.'
        pass
    
    def index(self, value, start, stop):
        'Return first index of value.\n\nRaises ValueError if the value is not present.'
        pass
    

Session = type()
class tuple(object):
    "Built-in immutable sequence.\n\nIf no argument is given, the constructor returns an empty tuple.\nIf iterable is specified the tuple is initialized from iterable's items.\n\nIf the argument is a tuple, the return value is the same object."
    def __add__(self, value):
        'Return self+value.'
        return tuple()
    
    __class__ = tuple
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __getnewargs__(self):
        return ()
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        "Built-in immutable sequence.\n\nIf no argument is given, the constructor returns an empty tuple.\nIf iterable is specified the tuple is initialized from iterable's items.\n\nIf the argument is a tuple, the return value is the same object."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return tuple()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return tuple()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return tuple()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def count(self, value):
        'Return number of occurrences of value.'
        pass
    
    def index(self, value, start, stop):
        'Return first index of value.\n\nRaises ValueError if the value is not present.'
        pass
    

class dict(object):
    "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
    __class__ = dict
    def __contains__(self, key):
        'True if the dictionary has the specified key, else False.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, iterable):
        "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return dict()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __sizeof__(self):
        'D.__sizeof__() -> size of D in memory, in bytes'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        pass
    
    def copy(self):
        'D.copy() -> a shallow copy of D'
        pass
    
    @classmethod
    def fromkeys(cls, type, iterable, value):
        'Create a new dictionary with keys from iterable and values set to value.'
        pass
    
    def get(self, key, default):
        'Return the value for key if key is in the dictionary, else default.'
        pass
    
    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        pass
    
    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        pass
    
    def pop(self):
        'D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\nIf key is not found, d is returned if given, otherwise KeyError is raised'
        pass
    
    def popitem(self):
        'D.popitem() -> (k, v), remove and return some (key, value) pair as a\n2-tuple; but raise KeyError if D is empty.'
        return tuple()
    
    def setdefault(self, key, default):
        'Insert key with a value of default if key is not in the dictionary.\n\nReturn the value for key if key is in the dictionary, else default.'
        pass
    
    def update(self):
        'D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\nIf E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\nIf E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\nIn either case, this is followed by: for k in F:  D[k] = F[k]'
        pass
    
    def values(self):
        "D.values() -> an object providing a view on D's values"
        pass
    

class dict(object):
    "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
    __class__ = dict
    def __contains__(self, key):
        'True if the dictionary has the specified key, else False.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, iterable):
        "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return dict()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __sizeof__(self):
        'D.__sizeof__() -> size of D in memory, in bytes'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        pass
    
    def copy(self):
        'D.copy() -> a shallow copy of D'
        pass
    
    @classmethod
    def fromkeys(cls, type, iterable, value):
        'Create a new dictionary with keys from iterable and values set to value.'
        pass
    
    def get(self, key, default):
        'Return the value for key if key is in the dictionary, else default.'
        pass
    
    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        pass
    
    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        pass
    
    def pop(self):
        'D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\nIf key is not found, d is returned if given, otherwise KeyError is raised'
        pass
    
    def popitem(self):
        'D.popitem() -> (k, v), remove and return some (key, value) pair as a\n2-tuple; but raise KeyError if D is empty.'
        return tuple()
    
    def setdefault(self, key, default):
        'Insert key with a value of default if key is not in the dictionary.\n\nReturn the value for key if key is in the dictionary, else default.'
        pass
    
    def update(self):
        'D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\nIf E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\nIf E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\nIn either case, this is followed by: for k in F:  D[k] = F[k]'
        pass
    
    def values(self):
        "D.values() -> an object providing a view on D's values"
        pass
    

class dict(object):
    "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
    __class__ = dict
    def __contains__(self, key):
        'True if the dictionary has the specified key, else False.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, iterable):
        "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return dict()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __sizeof__(self):
        'D.__sizeof__() -> size of D in memory, in bytes'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        pass
    
    def copy(self):
        'D.copy() -> a shallow copy of D'
        pass
    
    @classmethod
    def fromkeys(cls, type, iterable, value):
        'Create a new dictionary with keys from iterable and values set to value.'
        pass
    
    def get(self, key, default):
        'Return the value for key if key is in the dictionary, else default.'
        pass
    
    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        pass
    
    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        pass
    
    def pop(self):
        'D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\nIf key is not found, d is returned if given, otherwise KeyError is raised'
        pass
    
    def popitem(self):
        'D.popitem() -> (k, v), remove and return some (key, value) pair as a\n2-tuple; but raise KeyError if D is empty.'
        return tuple()
    
    def setdefault(self, key, default):
        'Insert key with a value of default if key is not in the dictionary.\n\nReturn the value for key if key is in the dictionary, else default.'
        pass
    
    def update(self):
        'D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\nIf E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\nIf E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\nIn either case, this is followed by: for k in F:  D[k] = F[k]'
        pass
    
    def values(self):
        "D.values() -> an object providing a view on D's values"
        pass
    

ALERT_DESCRIPTION_ACCESS_DENIED = 49
ALERT_DESCRIPTION_BAD_CERTIFICATE = 42
ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE = 114
ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE = 113
ALERT_DESCRIPTION_BAD_RECORD_MAC = 20
ALERT_DESCRIPTION_CERTIFICATE_EXPIRED = 45
ALERT_DESCRIPTION_CERTIFICATE_REVOKED = 44
ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN = 46
ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE = 111
ALERT_DESCRIPTION_CLOSE_NOTIFY = 0
ALERT_DESCRIPTION_DECODE_ERROR = 50
ALERT_DESCRIPTION_DECOMPRESSION_FAILURE = 30
ALERT_DESCRIPTION_DECRYPT_ERROR = 51
ALERT_DESCRIPTION_HANDSHAKE_FAILURE = 40
ALERT_DESCRIPTION_ILLEGAL_PARAMETER = 47
ALERT_DESCRIPTION_INSUFFICIENT_SECURITY = 71
ALERT_DESCRIPTION_INTERNAL_ERROR = 80
ALERT_DESCRIPTION_NO_RENEGOTIATION = 100
ALERT_DESCRIPTION_PROTOCOL_VERSION = 70
ALERT_DESCRIPTION_RECORD_OVERFLOW = 22
ALERT_DESCRIPTION_UNEXPECTED_MESSAGE = 10
ALERT_DESCRIPTION_UNKNOWN_CA = 48
ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY = 115
ALERT_DESCRIPTION_UNRECOGNIZED_NAME = 112
ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE = 43
ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION = 110
ALERT_DESCRIPTION_USER_CANCELLED = 90
CERT_NONE = 0
CERT_OPTIONAL = 1
CERT_REQUIRED = 2
HAS_ALPN = True
HAS_ECDH = True
HAS_NPN = False
HAS_SNI = True
HAS_SSLv2 = False
HAS_SSLv3 = False
HAS_TLS_UNIQUE = True
HAS_TLSv1 = True
HAS_TLSv1_1 = True
HAS_TLSv1_2 = True
HAS_TLSv1_3 = True
HOSTFLAG_ALWAYS_CHECK_SUBJECT = 1
HOSTFLAG_MULTI_LABEL_WILDCARDS = 8
HOSTFLAG_NEVER_CHECK_SUBJECT = 32
HOSTFLAG_NO_PARTIAL_WILDCARDS = 4
HOSTFLAG_NO_WILDCARDS = 2
HOSTFLAG_SINGLE_LABEL_SUBDOMAINS = 16
class MemoryBIO(object):
    __class__ = MemoryBIO
    def __init__(self, *args, **kwargs):
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
    def eof(self):
        'Whether the memory BIO is at EOF.'
        pass
    
    @property
    def pending(self):
        'The number of bytes pending in the memory BIO.'
        pass
    
    def read(self, size):
        'Read up to size bytes from the memory BIO.\n\nIf size is not specified, read the entire buffer.\nIf the return value is an empty bytes instance, this means either\nEOF or that no data is available. Use the "eof" property to\ndistinguish between the two.'
        pass
    
    def write(self, b):
        'Writes the bytes b into the memory BIO.\n\nReturns the number of bytes written.'
        pass
    
    def write_eof(self):
        'Write an EOF marker to the memory BIO.\n\nWhen all data has been read, the "eof" property will be True.'
        pass
    

OPENSSL_VERSION = 'OpenSSL 1.1.1c  28 May 2019'
OPENSSL_VERSION_INFO = tuple()
OPENSSL_VERSION_NUMBER = 269488191
OP_ALL = 2147483732
OP_CIPHER_SERVER_PREFERENCE = 4194304
OP_ENABLE_MIDDLEBOX_COMPAT = 1048576
OP_NO_COMPRESSION = 131072
OP_NO_RENEGOTIATION = 1073741824
OP_NO_SSLv2 = 0
OP_NO_SSLv3 = 33554432
OP_NO_TICKET = 16384
OP_NO_TLSv1 = 67108864
OP_NO_TLSv1_1 = 268435456
OP_NO_TLSv1_2 = 134217728
OP_NO_TLSv1_3 = 536870912
OP_SINGLE_DH_USE = 0
OP_SINGLE_ECDH_USE = 0
PROTOCOL_SSLv23 = 2
PROTOCOL_TLS = 2
PROTOCOL_TLS_CLIENT = 16
PROTOCOL_TLS_SERVER = 17
PROTOCOL_TLSv1 = 3
PROTOCOL_TLSv1_1 = 4
PROTOCOL_TLSv1_2 = 5
PROTO_MAXIMUM_SUPPORTED = -1
PROTO_MINIMUM_SUPPORTED = -2
PROTO_SSLv3 = 768
PROTO_TLSv1 = 769
PROTO_TLSv1_1 = 770
PROTO_TLSv1_2 = 771
PROTO_TLSv1_3 = 772
def RAND_add(string, entropy):
    'Mix string into the OpenSSL PRNG state.\n\nentropy (a float) is a lower bound on the entropy contained in\nstring.  See RFC 4086.'
    pass

def RAND_bytes(n):
    'Generate n cryptographically strong pseudo-random bytes.'
    pass

def RAND_pseudo_bytes(n):
    'Generate n pseudo-random bytes.\n\nReturn a pair (bytes, is_cryptographic).  is_cryptographic is True\nif the bytes generated are cryptographically strong.'
    pass

def RAND_status():
    'Returns 1 if the OpenSSL PRNG has been seeded with enough data and 0 if not.\n\nIt is necessary to seed the PRNG with RAND_add() on some platforms before\nusing the ssl() function.'
    pass

class SSLCertVerificationError(SSLError,ValueError):
    'A certificate could not be verified.'
    __class__ = SSLCertVerificationError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'A certificate could not be verified.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ssl'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class SSLEOFError(SSLError):
    'SSL/TLS connection terminated abruptly.'
    __class__ = SSLEOFError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'SSL/TLS connection terminated abruptly.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ssl'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class SSLError(OSError):
    'An error occurred in the SSL implementation.'
    __class__ = SSLError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'An error occurred in the SSL implementation.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ssl'
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

SSLSession = Session()
class SSLSyscallError(SSLError):
    'System error when attempting SSL operation.'
    __class__ = SSLSyscallError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'System error when attempting SSL operation.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ssl'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class SSLWantReadError(SSLError):
    'Non-blocking SSL socket needs to read more data\nbefore the requested operation can be completed.'
    __class__ = SSLWantReadError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Non-blocking SSL socket needs to read more data\nbefore the requested operation can be completed.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ssl'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class SSLWantWriteError(SSLError):
    'Non-blocking SSL socket needs to write more data\nbefore the requested operation can be completed.'
    __class__ = SSLWantWriteError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Non-blocking SSL socket needs to write more data\nbefore the requested operation can be completed.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ssl'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class SSLZeroReturnError(SSLError):
    'SSL/TLS session closed cleanly.'
    __class__ = SSLZeroReturnError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'SSL/TLS session closed cleanly.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ssl'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

SSL_ERROR_EOF = 8
SSL_ERROR_INVALID_ERROR_CODE = 10
SSL_ERROR_SSL = 1
SSL_ERROR_SYSCALL = 5
SSL_ERROR_WANT_CONNECT = 7
SSL_ERROR_WANT_READ = 2
SSL_ERROR_WANT_WRITE = 3
SSL_ERROR_WANT_X509_LOOKUP = 4
SSL_ERROR_ZERO_RETURN = 6
VERIFY_CRL_CHECK_CHAIN = 12
VERIFY_CRL_CHECK_LEAF = 4
VERIFY_DEFAULT = 0
VERIFY_X509_STRICT = 32
VERIFY_X509_TRUSTED_FIRST = 32768
_DEFAULT_CIPHERS = 'DEFAULT:!aNULL:!eNULL:!MD5:!3DES:!DES:!RC4:!IDEA:!SEED:!aDSS:!SRP:!PSK'
_OPENSSL_API_VERSION = tuple()
class _SSLContext(object):
    __class__ = _SSLContext
    def __init__(self, *args, **kwargs):
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
    def _host_flags(self):
        pass
    
    def _set_alpn_protocols(self, protos):
        pass
    
    def _set_npn_protocols(self, protos):
        pass
    
    def _wrap_bio(self, incoming, outgoing, server_side, server_hostname):
        pass
    
    def _wrap_socket(self, sock, server_side, server_hostname):
        pass
    
    def cert_store_stats(self):
        "Returns quantities of loaded X.509 certificates.\n\nX.509 certificates with a CA extension and certificate revocation lists\ninside the context's cert store.\n\nNOTE: Certificates in a capath directory aren't loaded unless they have\nbeen used at least once."
        pass
    
    @property
    def check_hostname(self):
        pass
    
    def get_ca_certs(self, binary_form):
        "Returns a list of dicts with information of loaded CA certs.\n\nIf the optional argument is True, returns a DER-encoded copy of the CA\ncertificate.\n\nNOTE: Certificates in a capath directory aren't loaded unless they have\nbeen used at least once."
        pass
    
    def get_ciphers(self):
        pass
    
    def load_cert_chain(self, certfile, keyfile, password):
        pass
    
    def load_dh_params(self, path):
        pass
    
    def load_verify_locations(self, cafile, capath, cadata):
        pass
    
    @property
    def maximum_version(self):
        pass
    
    @property
    def minimum_version(self):
        pass
    
    @property
    def options(self):
        pass
    
    @property
    def post_handshake_auth(self):
        pass
    
    @property
    def protocol(self):
        pass
    
    def session_stats(self):
        pass
    
    def set_ciphers(self, cipherlist):
        pass
    
    def set_default_verify_paths(self):
        pass
    
    def set_ecdh_curve(self, name):
        pass
    
    @property
    def sni_callback(self):
        'Set a callback that will be called when a server name is provided by the SSL/TLS client in the SNI extension.\n\nIf the argument is None then the callback is disabled. The method is called\nwith the SSLSocket, the server name as a string, and the SSLContext object.\nSee RFC 6066 for details of the SNI extension.'
        pass
    
    @property
    def verify_flags(self):
        pass
    
    @property
    def verify_mode(self):
        pass
    

class _SSLSocket(object):
    __class__ = _SSLSocket
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def cipher(self):
        pass
    
    def compression(self):
        pass
    
    @property
    def context(self):
        '_setter_context(ctx)\nThis changes the context associated with the SSLSocket. This is typically\nused from within a callback function set by the sni_callback\non the SSLContext to change the certificate information associated with the\nSSLSocket before the cryptographic exchange handshake messages\n'
        pass
    
    def do_handshake(self):
        pass
    
    def get_channel_binding(self, cb_type):
        "Get channel binding data for current connection.\n\nRaise ValueError if the requested `cb_type` is not supported.  Return bytes\nof the data or None if the data is not available (e.g. before the handshake).\nOnly 'tls-unique' channel binding data from RFC 5929 is supported."
        pass
    
    def getpeercert(self, der):
        "Returns the certificate for the peer.\n\nIf no certificate was provided, returns None.  If a certificate was\nprovided, but not validated, returns an empty dictionary.  Otherwise\nreturns a dict containing information about the peer certificate.\n\nIf the optional argument is True, returns a DER-encoded copy of the\npeer certificate, or None if no certificate was provided.  This will\nreturn the certificate even if it wasn't validated."
        pass
    
    @property
    def owner(self):
        'The Python-level owner of this object.Passed as "self" in servername callback.'
        pass
    
    def pending(self):
        'Returns the number of already decrypted bytes available for read, pending on the connection.'
        pass
    
    def read(self, size, buffer=None):
        'read(size, [buffer])\nRead up to size bytes from the SSL socket.'
        pass
    
    def selected_alpn_protocol(self):
        pass
    
    @property
    def server_hostname(self):
        'The currently set server hostname (for SNI).'
        pass
    
    @property
    def server_side(self):
        'Whether this is a server-side socket.'
        pass
    
    @property
    def session(self):
        '_setter_session(session)\nGet / set SSLSession.'
        pass
    
    @property
    def session_reused(self):
        'Was the client session reused during handshake?'
        pass
    
    def shared_ciphers(self):
        pass
    
    def shutdown(self):
        'Does the SSL shutdown handshake with the remote end.'
        pass
    
    def verify_client_post_handshake(self):
        'Initiate TLS 1.3 post-handshake authentication'
        pass
    
    def version(self):
        pass
    
    def write(self, b):
        'Writes the bytes-like object b into the SSL object.\n\nReturns the number of bytes written.'
        pass
    

__doc__ = 'Implementation module for SSL socket operations.  See the socket module\nfor documentation.'
__file__ = '/usr/lib/python3.7/lib-dynload/_ssl.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_ssl'
__package__ = ''
def _test_decode_cert(path):
    pass

err_codes_to_names = dict()
err_names_to_codes = dict()
def get_default_verify_paths():
    "Return search paths and environment vars that are used by SSLContext's set_default_verify_paths() to load default CAs.\n\nThe values are 'cert_file_env', 'cert_file', 'cert_dir_env', 'cert_dir'."
    pass

lib_codes_to_names = dict()
def nid2obj(nid):
    'Lookup NID, short name, long name and OID of an ASN1_OBJECT by NID.'
    pass

def txt2obj(txt, name):
    'Lookup NID, short name, long name and OID of an ASN1_OBJECT.\n\nBy default objects are looked up by OID. With name=True short and\nlong name are also matched.'
    pass

