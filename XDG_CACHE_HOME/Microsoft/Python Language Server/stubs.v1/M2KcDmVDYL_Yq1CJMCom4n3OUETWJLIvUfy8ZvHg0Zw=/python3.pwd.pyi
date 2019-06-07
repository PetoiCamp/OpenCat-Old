import builtins as _mod_builtins

__doc__ = "This module provides access to the Unix password database.\nIt is available on all Unix versions.\n\nPassword database entries are reported as 7-tuples containing the following\nitems from the password database (see `<pwd.h>'), in order:\npw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell.\nThe uid and gid items are integers, all others are strings. An\nexception is raised if the entry asked for cannot be found."
__name__ = 'pwd'
__package__ = ''
def getpwall():
    'Return a list of all available password database entries, in arbitrary order.\n\nSee help(pwd) for more on password database entries.'
    pass

def getpwnam(arg):
    'Return the password database entry for the given user name.\n\nSee `help(pwd)` for more on password database entries.'
    pass

def getpwuid(uidobj):
    'Return the password database entry for the given numeric user ID.\n\nSee `help(pwd)` for more on password database entries.'
    pass

class struct_passwd(_mod_builtins.tuple):
    'pwd.struct_passwd: Results from getpw*() routines.\n\nThis object may be accessed either as a tuple of\n  (pw_name,pw_passwd,pw_uid,pw_gid,pw_gecos,pw_dir,pw_shell)\nor via the object attributes as named in the above tuple.'
    __class__ = struct_passwd
    def __init__(self):
        'pwd.struct_passwd: Results from getpw*() routines.\n\nThis object may be accessed either as a tuple of\n  (pw_name,pw_passwd,pw_uid,pw_gid,pw_gecos,pw_dir,pw_shell)\nor via the object attributes as named in the above tuple.'
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
    
    n_fields = 7
    n_sequence_fields = 7
    n_unnamed_fields = 0
    @property
    def pw_dir(self):
        'home directory'
        pass
    
    @property
    def pw_gecos(self):
        'real name'
        pass
    
    @property
    def pw_gid(self):
        'group id'
        pass
    
    @property
    def pw_name(self):
        'user name'
        pass
    
    @property
    def pw_passwd(self):
        'password'
        pass
    
    @property
    def pw_shell(self):
        'shell program'
        pass
    
    @property
    def pw_uid(self):
        'user id'
        pass
    

