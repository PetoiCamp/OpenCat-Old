import builtins as _mod_builtins

EPOLLERR = 8
EPOLLET = 2147483648
EPOLLEXCLUSIVE = 268435456
EPOLLHUP = 16
EPOLLIN = 1
EPOLLMSG = 1024
EPOLLONESHOT = 1073741824
EPOLLOUT = 4
EPOLLPRI = 2
EPOLLRDBAND = 128
EPOLLRDHUP = 8192
EPOLLRDNORM = 64
EPOLLWRBAND = 512
EPOLLWRNORM = 256
EPOLL_CLOEXEC = 524288
PIPE_BUF = 4096
POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLMSG = 1024
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDHUP = 8192
POLLRDNORM = 64
POLLWRBAND = 512
POLLWRNORM = 256
__doc__ = 'This module supports asynchronous I/O on multiple file descriptors.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file descriptors.'
__file__ = '/usr/lib/python3.7/lib-dynload/select.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'select'
__package__ = ''
class epoll(_mod_builtins.object):
    "select.epoll(sizehint=-1, flags=0)\n\nReturns an epolling object\n\nsizehint must be a positive integer or -1 for the default size. The\nsizehint is used to optimize internal data structures. It doesn't limit\nthe maximum number of monitored events."
    __class__ = epoll
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, sizehint=-1, flags=0):
        "select.epoll(sizehint=-1, flags=0)\n\nReturns an epolling object\n\nsizehint must be a positive integer or -1 for the default size. The\nsizehint is used to optimize internal data structures. It doesn't limit\nthe maximum number of monitored events."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'close() -> None\n\nClose the epoll control file descriptor. Further operations on the epoll\nobject will raise an exception.'
        pass
    
    @property
    def closed(self):
        'True if the epoll handler is closed'
        pass
    
    def fileno(self):
        'fileno() -> int\n\nReturn the epoll control file descriptor.'
        return 1
    
    @classmethod
    def fromfd(cls, fd):
        'fromfd(fd) -> epoll\n\nCreate an epoll object from a given control fd.'
        pass
    
    def modify(self, fd, eventmask):
        'modify(fd, eventmask) -> None\n\nfd is the target file descriptor of the operation\nevents is a bit set composed of the various EPOLL constants'
        pass
    
    def poll(self):
        'poll([timeout=-1[, maxevents=-1]]) -> [(fd, events), (...)]\n\nWait for events on the epoll file descriptor for a maximum time of timeout\nin seconds (as float). -1 makes poll wait indefinitely.\nUp to maxevents are returned to the caller.'
        pass
    
    def register(self, fd, eventmask=None):
        'register(fd[, eventmask]) -> None\n\nRegisters a new fd or raises an OSError if the fd is already registered.\nfd is the target file descriptor of the operation.\nevents is a bit set composed of the various EPOLL constants; the default\nis EPOLLIN | EPOLLOUT | EPOLLPRI.\n\nThe epoll interface supports all file descriptors that support poll.'
        pass
    
    def unregister(self, fd):
        'unregister(fd) -> None\n\nfd is the target file descriptor of the operation.'
        pass
    

error = _mod_builtins.OSError
def poll():
    'Returns a polling object, which supports registering and\nunregistering file descriptors, and then polling them for I/O events.'
    pass

def select(rlist, wlist, xlist, timeout=None):
    "select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)\n\nWait until one or more file descriptors are ready for some kind of I/O.\nThe first three arguments are sequences of file descriptors to be waited for:\nrlist -- wait until ready for reading\nwlist -- wait until ready for writing\nxlist -- wait for an ``exceptional condition''\nIf only one kind of condition is required, pass [] for the other lists.\nA file descriptor is either a socket or file object, or a small integer\ngotten from a fileno() method call on one of those.\n\nThe optional 4th argument specifies a timeout in seconds; it may be\na floating point number to specify fractions of seconds.  If it is absent\nor None, the call will never time out.\n\nThe return value is a tuple of three lists corresponding to the first three\narguments; each contains the subset of the corresponding file descriptors\nthat are ready.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file\ndescriptors can be used."
    return tuple()

