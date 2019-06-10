import builtins as _mod_builtins

class ZipImportError(_mod_builtins.ImportError):
    __class__ = ZipImportError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'zipimport'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__doc__ = "zipimport provides support for importing Python modules from Zip archives.\n\nThis module exports three objects:\n- zipimporter: a class; its constructor takes a path to a Zip archive.\n- ZipImportError: exception raised by zipimporter objects. It's a\n  subclass of ImportError, so it can be caught as ImportError, too.\n- _zip_directory_cache: a dict, mapping archive paths to zip directory\n  info dicts, as used in zipimporter._files.\n\nIt is usually not needed to use the zipimport module explicitly; it is\nused by the builtin import mechanism for sys.path items that are paths\nto Zip archives."
__name__ = 'zipimport'
__package__ = ''
_zip_directory_cache = _mod_builtins.dict()
class zipimporter(_mod_builtins.object):
    "Create a new zipimporter instance.\n\n  archivepath\n    A path-like object to a zipfile, or to a specific path inside\n    a zipfile.\n\n'archivepath' must be a path-like object to a zipfile, or to a specific path\ninside a zipfile. For example, it can be '/tmp/myimport.zip', or\n'/tmp/myimport.zip/mydirectory', if mydirectory is a valid directory inside\nthe archive.\n\n'ZipImportError' is raised if 'archivepath' doesn't point to a valid Zip\narchive.\n\nThe 'archive' attribute of the zipimporter object contains the name of the\nzipfile targeted."
    __class__ = zipimporter
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        "Create a new zipimporter instance.\n\n  archivepath\n    A path-like object to a zipfile, or to a specific path inside\n    a zipfile.\n\n'archivepath' must be a path-like object to a zipfile, or to a specific path\ninside a zipfile. For example, it can be '/tmp/myimport.zip', or\n'/tmp/myimport.zip/mydirectory', if mydirectory is a valid directory inside\nthe archive.\n\n'ZipImportError' is raised if 'archivepath' doesn't point to a valid Zip\narchive.\n\nThe 'archive' attribute of the zipimporter object contains the name of the\nzipfile targeted."
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
    def _files(self):
        pass
    
    @property
    def archive(self):
        pass
    
    def find_loader(self, fullname, path):
        "Search for a module specified by 'fullname'.\n\n'fullname' must be the fully qualified (dotted) module name. It returns the\nzipimporter instance itself if the module was found, a string containing the\nfull path name if it's possibly a portion of a namespace package,\nor None otherwise. The optional 'path' argument is ignored -- it's\nthere for compatibility with the importer protocol."
        pass
    
    def find_module(self, fullname, path):
        "Search for a module specified by 'fullname'.\n\n'fullname' must be the fully qualified (dotted) module name. It returns the\nzipimporter instance itself if the module was found, or None if it wasn't.\nThe optional 'path' argument is ignored -- it's there for compatibility\nwith the importer protocol."
        pass
    
    def get_code(self, fullname):
        "Return the code object for the specified module.\n\nRaise ZipImportError if the module couldn't be found."
        pass
    
    def get_data(self, pathname):
        "Return the data associated with 'pathname'.\n\nRaise OSError if the file was not found."
        pass
    
    def get_filename(self, fullname):
        'Return the filename for the specified module.'
        pass
    
    def get_resource_reader(self, fullname):
        "Return the ResourceReader for a package in a zip file.\n\nIf 'fullname' is a package within the zip file, return the 'ResourceReader'\nobject for the package.  Otherwise return None."
        pass
    
    def get_source(self, fullname):
        "Return the source code for the specified module.\n\nRaise ZipImportError if the module couldn't be found, return None if the\narchive does contain the module, but has no source for it."
        pass
    
    def is_package(self, fullname):
        "Return True if the module specified by fullname is a package.\n\nRaise ZipImportError if the module couldn't be found."
        pass
    
    def load_module(self, fullname):
        "Load the module specified by 'fullname'.\n\n'fullname' must be the fully qualified (dotted) module name. It returns the\nimported module, or raises ZipImportError if it wasn't found."
        pass
    
    @property
    def prefix(self):
        pass
    

