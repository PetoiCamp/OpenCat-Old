__doc__ = 'Module contains faster C implementation of abc.ABCMeta'
__name__ = '_abc'
__package__ = ''
def _abc_init(self):
    'Internal ABC helper for class set-up. Should be never used outside abc module.'
    pass

def _abc_instancecheck(self, instance):
    'Internal ABC helper for instance checks. Should be never used outside abc module.'
    pass

def _abc_register(self, subclass):
    'Internal ABC helper for subclasss registration. Should be never used outside abc module.'
    pass

def _abc_subclasscheck(self, subclass):
    'Internal ABC helper for subclasss checks. Should be never used outside abc module.'
    pass

def _get_dump(self):
    "Internal ABC helper for cache and registry debugging.\n\nReturn shallow copies of registry, of both caches, and\nnegative cache version. Don't call this function directly,\ninstead use ABC._dump_registry() for a nice repr."
    pass

def _reset_caches(self):
    'Internal ABC helper to reset both caches of a given class.\n\nShould be only used by refleak.py'
    pass

def _reset_registry(self):
    'Internal ABC helper to reset registry of a given class.\n\nShould be only used by refleak.py'
    pass

def get_cache_token():
    'Returns the current ABC cache token.\n\nThe token is an opaque object (supporting equality testing) identifying the\ncurrent version of the ABC cache for virtual subclasses. The token changes\nwith every call to register() on any ABC.'
    pass

