import builtins as _mod_builtins

__doc__ = 'Access to the Unix group database.\n\nGroup entries are reported as 4-tuples containing the following fields\nfrom the group database, in order:\n\n  gr_name   - name of the group\n  gr_passwd - group password (encrypted); often empty\n  gr_gid    - numeric ID of the group\n  gr_mem    - list of members\n\nThe gid is an integer, name and password are strings.  (Note that most\nusers are not explicitly listed as members of the groups they are in\naccording to the password database.  Check both databases to get\ncomplete membership information.)'
__file__ = '/usr/lib/python3.7/lib-dynload/grp.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'grp'
__package__ = ''
def getgrall():
    "Return a list of all available group entries, in arbitrary order.\n\nAn entry whose name starts with '+' or '-' represents an instruction\nto use YP/NIS and may not be accessible via getgrnam or getgrgid."
    pass

def getgrgid(id):
    'Return the group database entry for the given numeric group ID.\n\nIf id is not valid, raise KeyError.'
    pass

def getgrnam(name):
    'Return the group database entry for the given group name.\n\nIf name is not valid, raise KeyError.'
    pass

class struct_group(_mod_builtins.tuple):
    'grp.struct_group: Results from getgr*() routines.\n\nThis object may be accessed either as a tuple of\n  (gr_name,gr_passwd,gr_gid,gr_mem)\nor via the object attributes as named in the above tuple.\n'
    __class__ = struct_group
    def __init__(self):
        'grp.struct_group: Results from getgr*() routines.\n\nThis object may be accessed either as a tuple of\n  (gr_name,gr_passwd,gr_gid,gr_mem)\nor via the object attributes as named in the above tuple.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def gr_gid(self):
        'group id'
        pass
    
    @property
    def gr_mem(self):
        'group members'
        pass
    
    @property
    def gr_name(self):
        'group name'
        pass
    
    @property
    def gr_passwd(self):
        'password'
        pass
    
    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0

