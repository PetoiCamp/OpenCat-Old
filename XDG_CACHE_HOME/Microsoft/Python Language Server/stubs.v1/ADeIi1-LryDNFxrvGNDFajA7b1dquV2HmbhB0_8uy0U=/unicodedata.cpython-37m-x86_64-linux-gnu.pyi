import builtins as _mod_builtins

class UCD(_mod_builtins.object):
    __class__ = UCD
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
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
    
    def bidirectional(self, chr):
        'Returns the bidirectional class assigned to the character chr as string.\n\nIf no such value is defined, an empty string is returned.'
        pass
    
    def category(self, chr):
        'Returns the general category assigned to the character chr as string.'
        pass
    
    def combining(self, chr):
        'Returns the canonical combining class assigned to the character chr as integer.\n\nReturns 0 if no combining class is defined.'
        pass
    
    def decimal(self, chr, default):
        'Converts a Unicode character into its equivalent decimal value.\n\nReturns the decimal value assigned to the character chr as integer.\nIf no such value is defined, default is returned, or, if not given,\nValueError is raised.'
        pass
    
    def decomposition(self, chr):
        'Returns the character decomposition mapping assigned to the character chr as string.\n\nAn empty string is returned in case no such mapping is defined.'
        pass
    
    def digit(self, chr, default):
        'Converts a Unicode character into its equivalent digit value.\n\nReturns the digit value assigned to the character chr as integer.\nIf no such value is defined, default is returned, or, if not given,\nValueError is raised.'
        pass
    
    def east_asian_width(self, chr):
        'Returns the east asian width assigned to the character chr as string.'
        pass
    
    def lookup(self, name):
        'Look up character by name.\n\nIf a character with the given name is found, return the\ncorresponding character.  If not found, KeyError is raised.'
        pass
    
    def mirrored(self, chr):
        'Returns the mirrored property assigned to the character chr as integer.\n\nReturns 1 if the character has been identified as a "mirrored"\ncharacter in bidirectional text, 0 otherwise.'
        pass
    
    def name(self, chr, default):
        'Returns the name assigned to the character chr as a string.\n\nIf no name is defined, default is returned, or, if not given,\nValueError is raised.'
        pass
    
    def normalize(self, form, unistr):
        "Return the normal form 'form' for the Unicode string unistr.\n\nValid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'."
        pass
    
    def numeric(self, chr, default):
        'Converts a Unicode character into its equivalent numeric value.\n\nReturns the numeric value assigned to the character chr as float.\nIf no such value is defined, default is returned, or, if not given,\nValueError is raised.'
        pass
    
    @property
    def unidata_version(self):
        pass
    

__doc__ = 'This module provides access to the Unicode Character Database which\ndefines character properties for all Unicode characters. The data in\nthis database is based on the UnicodeData.txt file version\n11.0.0 which is publicly available from ftp://ftp.unicode.org/.\n\nThe module uses the same names and symbols as defined by the\nUnicodeData File Format 11.0.0.'
__file__ = '/usr/lib/python3.7/lib-dynload/unicodedata.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'unicodedata'
__package__ = ''
def bidirectional(chr):
    'Returns the bidirectional class assigned to the character chr as string.\n\nIf no such value is defined, an empty string is returned.'
    pass

def category(chr):
    'Returns the general category assigned to the character chr as string.'
    pass

def combining(chr):
    'Returns the canonical combining class assigned to the character chr as integer.\n\nReturns 0 if no combining class is defined.'
    pass

def decimal(chr, default):
    'Converts a Unicode character into its equivalent decimal value.\n\nReturns the decimal value assigned to the character chr as integer.\nIf no such value is defined, default is returned, or, if not given,\nValueError is raised.'
    pass

def decomposition(chr):
    'Returns the character decomposition mapping assigned to the character chr as string.\n\nAn empty string is returned in case no such mapping is defined.'
    pass

def digit(chr, default):
    'Converts a Unicode character into its equivalent digit value.\n\nReturns the digit value assigned to the character chr as integer.\nIf no such value is defined, default is returned, or, if not given,\nValueError is raised.'
    pass

def east_asian_width(chr):
    'Returns the east asian width assigned to the character chr as string.'
    pass

def lookup(name):
    'Look up character by name.\n\nIf a character with the given name is found, return the\ncorresponding character.  If not found, KeyError is raised.'
    pass

def mirrored(chr):
    'Returns the mirrored property assigned to the character chr as integer.\n\nReturns 1 if the character has been identified as a "mirrored"\ncharacter in bidirectional text, 0 otherwise.'
    pass

def name(chr, default):
    'Returns the name assigned to the character chr as a string.\n\nIf no name is defined, default is returned, or, if not given,\nValueError is raised.'
    pass

def normalize(form, unistr):
    "Return the normal form 'form' for the Unicode string unistr.\n\nValid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'."
    pass

def numeric(chr, default):
    'Converts a Unicode character into its equivalent numeric value.\n\nReturns the numeric value assigned to the character chr as float.\nIf no such value is defined, default is returned, or, if not given,\nValueError is raised.'
    pass

ucd_3_2_0 = UCD()
ucnhash_CAPI = _mod_builtins.PyCapsule()
unidata_version = '11.0.0'
