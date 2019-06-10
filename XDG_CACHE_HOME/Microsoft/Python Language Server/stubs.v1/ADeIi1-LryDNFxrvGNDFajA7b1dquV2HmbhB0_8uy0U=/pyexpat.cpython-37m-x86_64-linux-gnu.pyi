import builtins as _mod_builtins

xmlparser = _mod_builtins.type
EXPAT_VERSION = 'expat_2.2.5'
def ErrorString(code):
    'Returns string error for given number.'
    pass

class ExpatError(_mod_builtins.Exception):
    __class__ = ExpatError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'xml.parsers.expat'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def ParserCreate(encoding, namespace_separator, intern):
    'Return a new XML parser object.'
    pass

XMLParserType = xmlparser()
XML_PARAM_ENTITY_PARSING_ALWAYS = 2
XML_PARAM_ENTITY_PARSING_NEVER = 0
XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE = 1
__doc__ = 'Python wrapper for Expat parser.'
__file__ = '/usr/lib/python3.7/lib-dynload/pyexpat.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'pyexpat'
__package__ = ''
error = ExpatError()
expat_CAPI = _mod_builtins.PyCapsule()
features = _mod_builtins.list()
native_encoding = 'UTF-8'
version_info = _mod_builtins.tuple()
