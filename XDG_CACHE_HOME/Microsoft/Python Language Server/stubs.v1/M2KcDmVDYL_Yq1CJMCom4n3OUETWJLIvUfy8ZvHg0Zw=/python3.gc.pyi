import builtins as _mod_builtins

DEBUG_COLLECTABLE = 2
DEBUG_LEAK = 38
DEBUG_SAVEALL = 32
DEBUG_STATS = 1
DEBUG_UNCOLLECTABLE = 4
__doc__ = 'This module provides access to the garbage collector for reference cycles.\n\nenable() -- Enable automatic garbage collection.\ndisable() -- Disable automatic garbage collection.\nisenabled() -- Returns true if automatic collection is enabled.\ncollect() -- Do a full collection right now.\nget_count() -- Return the current collection counts.\nget_stats() -- Return list of dictionaries containing per-generation stats.\nset_debug() -- Set debugging flags.\nget_debug() -- Get debugging flags.\nset_threshold() -- Set the collection thresholds.\nget_threshold() -- Return the current the collection thresholds.\nget_objects() -- Return a list of all objects tracked by the collector.\nis_tracked() -- Returns true if a given object is tracked.\nget_referrers() -- Return the list of objects that refer to an object.\nget_referents() -- Return the list of objects that an object refers to.\nfreeze() -- Freeze all tracked objects and ignore them for future collections.\nunfreeze() -- Unfreeze all objects in the permanent generation.\nget_freeze_count() -- Return the number of objects in the permanent generation.\n'
__name__ = 'gc'
__package__ = ''
callbacks = _mod_builtins.list()
def collect(generation):
    'Run the garbage collector.\n\nWith no arguments, run a full collection.  The optional argument\nmay be an integer specifying which generation to collect.  A ValueError\nis raised if the generation number is invalid.\n\nThe number of unreachable objects is returned.'
    pass

def disable():
    'Disable automatic garbage collection.'
    pass

def enable():
    'Enable automatic garbage collection.'
    pass

def freeze():
    'Freeze all current tracked objects and ignore them for future collections.\n\nThis can be used before a POSIX fork() call to make the gc copy-on-write friendly.\nNote: collection before a POSIX fork() call may free pages for future allocation\nwhich can cause copy-on-write.'
    pass

garbage = _mod_builtins.list()
def get_count():
    'Return a three-tuple of the current collection counts.'
    pass

def get_debug():
    'Get the garbage collection debugging flags.'
    pass

def get_freeze_count():
    'Return the number of objects in the permanent generation.'
    pass

def get_objects():
    'Return a list of objects tracked by the collector (excluding the list returned).'
    pass

def get_referents(*objs):
    'get_referents(*objs) -> list\nReturn the list of objects that are directly referred to by objs.'
    return list()

def get_referrers(*objs):
    'get_referrers(*objs) -> list\nReturn the list of objects that directly refer to any of objs.'
    return list()

def get_stats():
    'Return a list of dictionaries containing per-generation statistics.'
    pass

def get_threshold():
    'Return the current collection thresholds.'
    pass

def is_tracked(obj):
    'Returns true if the object is tracked by the garbage collector.\n\nSimple atomic objects will return false.'
    pass

def isenabled():
    'Returns true if automatic garbage collection is enabled.'
    pass

def set_debug(flags):
    'Set the garbage collection debugging flags.\n\n  flags\n    An integer that can have the following bits turned on:\n      DEBUG_STATS - Print statistics during collection.\n      DEBUG_COLLECTABLE - Print collectable objects found.\n      DEBUG_UNCOLLECTABLE - Print unreachable but uncollectable objects\n        found.\n      DEBUG_SAVEALL - Save objects to gc.garbage rather than freeing them.\n      DEBUG_LEAK - Debug leaking programs (everything but STATS).\n\nDebugging information is written to sys.stderr.'
    pass

def set_threshold(threshold0, threshold1=None, threshold2=None):
    'set_threshold(threshold0, [threshold1, threshold2]) -> None\n\nSets the collection thresholds.  Setting threshold0 to zero disables\ncollection.\n'
    pass

def unfreeze():
    'Unfreeze all objects in the permanent generation.\n\nPut all objects in the permanent generation back into oldest generation.'
    pass

