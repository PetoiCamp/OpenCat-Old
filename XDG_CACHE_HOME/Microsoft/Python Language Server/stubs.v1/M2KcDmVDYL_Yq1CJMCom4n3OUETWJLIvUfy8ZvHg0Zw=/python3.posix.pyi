import builtins as _mod_builtins
import os as _mod_os

CLD_CONTINUED = 6
CLD_DUMPED = 3
CLD_EXITED = 1
CLD_TRAPPED = 4
class DirEntry(_mod_builtins.object):
    __class__ = DirEntry
    def __fspath__(self):
        'Returns the path for the entry.'
        pass
    
    def __init__(self, *args, **kwargs):
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
    
    def inode(self):
        'Return inode of the entry; cached per entry.'
        pass
    
    def is_dir(self):
        'Return True if the entry is a directory; cached per entry.'
        pass
    
    def is_file(self):
        'Return True if the entry is a file; cached per entry.'
        pass
    
    def is_symlink(self):
        'Return True if the entry is a symbolic link; cached per entry.'
        pass
    
    @property
    def name(self):
        'the entry\'s base filename, relative to scandir() "path" argument'
        pass
    
    @property
    def path(self):
        "the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)"
        pass
    
    def stat(self):
        'Return stat_result object for the entry; cached per entry.'
        pass
    

EX_CANTCREAT = 73
EX_CONFIG = 78
EX_DATAERR = 65
EX_IOERR = 74
EX_NOHOST = 68
EX_NOINPUT = 66
EX_NOPERM = 77
EX_NOUSER = 67
EX_OK = 0
EX_OSERR = 71
EX_OSFILE = 72
EX_PROTOCOL = 76
EX_SOFTWARE = 70
EX_TEMPFAIL = 75
EX_UNAVAILABLE = 69
EX_USAGE = 64
F_LOCK = 1
F_OK = 0
F_TEST = 3
F_TLOCK = 2
F_ULOCK = 0
GRND_NONBLOCK = 1
GRND_RANDOM = 2
NGROUPS_MAX = 65536
O_ACCMODE = 3
O_APPEND = 1024
O_ASYNC = 8192
O_CLOEXEC = 524288
O_CREAT = 64
O_DIRECT = 16384
O_DIRECTORY = 65536
O_DSYNC = 4096
O_EXCL = 128
O_LARGEFILE = 0
O_NDELAY = 2048
O_NOATIME = 262144
O_NOCTTY = 256
O_NOFOLLOW = 131072
O_NONBLOCK = 2048
O_PATH = 2097152
O_RDONLY = 0
O_RDWR = 2
O_RSYNC = 1052672
O_SYNC = 1052672
O_TMPFILE = 4259840
O_TRUNC = 512
O_WRONLY = 1
POSIX_FADV_DONTNEED = 4
POSIX_FADV_NOREUSE = 5
POSIX_FADV_NORMAL = 0
POSIX_FADV_RANDOM = 1
POSIX_FADV_SEQUENTIAL = 2
POSIX_FADV_WILLNEED = 3
PRIO_PGRP = 1
PRIO_PROCESS = 0
PRIO_USER = 2
P_ALL = 0
P_PGID = 2
P_PID = 1
RTLD_DEEPBIND = 8
RTLD_GLOBAL = 256
RTLD_LAZY = 1
RTLD_LOCAL = 0
RTLD_NODELETE = 4096
RTLD_NOLOAD = 4
RTLD_NOW = 2
RWF_DSYNC = 2
RWF_HIPRI = 1
RWF_NOWAIT = 8
RWF_SYNC = 4
R_OK = 4
SCHED_BATCH = 3
SCHED_FIFO = 1
SCHED_IDLE = 5
SCHED_OTHER = 0
SCHED_RESET_ON_FORK = 1073741824
SCHED_RR = 2
SEEK_DATA = 3
SEEK_HOLE = 4
ST_APPEND = 256
ST_MANDLOCK = 64
ST_NOATIME = 1024
ST_NODEV = 4
ST_NODIRATIME = 2048
ST_NOEXEC = 8
ST_NOSUID = 2
ST_RDONLY = 1
ST_RELATIME = 4096
ST_SYNCHRONOUS = 16
ST_WRITE = 128
TMP_MAX = 238328
WCONTINUED = 8
def WCOREDUMP(status):
    'Return True if the process returning status was dumped to a core file.'
    pass

WEXITED = 4
def WEXITSTATUS(status):
    'Return the process return code from status.'
    pass

def WIFCONTINUED(status):
    'Return True if a particular process was continued from a job control stop.\n\nReturn True if the process returning status was continued from a\njob control stop.'
    pass

def WIFEXITED(status):
    'Return True if the process returning status exited via the exit() system call.'
    pass

def WIFSIGNALED(status):
    'Return True if the process returning status was terminated by a signal.'
    pass

def WIFSTOPPED(status):
    'Return True if the process returning status was stopped.'
    pass

WNOHANG = 1
WNOWAIT = 16777216
WSTOPPED = 2
def WSTOPSIG(status):
    'Return the signal that stopped the process that provided the status value.'
    pass

def WTERMSIG(status):
    'Return the signal that terminated the process that provided the status value.'
    pass

WUNTRACED = 2
W_OK = 2
XATTR_CREATE = 1
XATTR_REPLACE = 2
XATTR_SIZE_MAX = 65536
X_OK = 1
__doc__ = 'This module provides access to operating system functionality that is\nstandardized by the C Standard and the POSIX standard (a thinly\ndisguised Unix interface).  Refer to the library manual and\ncorresponding Unix manual entries for more information on calls.'
__name__ = 'posix'
__package__ = ''
def _exit(status):
    'Exit to the system with specified status, without normal exit processing.'
    pass

_have_functions = _mod_builtins.list()
def abort():
    "Abort the interpreter immediately.\n\nThis function 'dumps core' or otherwise fails in the hardest way possible\non the hosting operating system.  This function never returns."
    pass

def access(path, mode):
    'Use the real uid/gid to test for access to a path.\n\n  path\n    Path to be tested; can be string, bytes, or a path-like object.\n  mode\n    Operating-system mode bitfield.  Can be F_OK to test existence,\n    or the inclusive-OR of R_OK, W_OK, and X_OK.\n  dir_fd\n    If not None, it should be a file descriptor open to a directory,\n    and path should be relative; path will then be relative to that\n    directory.\n  effective_ids\n    If True, access will use the effective uid/gid instead of\n    the real uid/gid.\n  follow_symlinks\n    If False, and the last element of the path is a symbolic link,\n    access will examine the symbolic link itself instead of the file\n    the link points to.\n\ndir_fd, effective_ids, and follow_symlinks may not be implemented\n  on your platform.  If they are unavailable, using them will raise a\n  NotImplementedError.\n\nNote that most operations will use the effective uid/gid, therefore this\n  routine can be used in a suid/sgid environment to test if the invoking user\n  has the specified access to the path.'
    pass

def chdir(path):
    'Change the current working directory to the specified path.\n\npath may always be specified as a string.\nOn some platforms, path may also be specified as an open file descriptor.\n  If this functionality is unavailable, using it raises an exception.'
    pass

def chmod(path, mode):
    'Change the access permissions of a file.\n\n  path\n    Path to be modified.  May always be specified as a str, bytes, or a path-like object.\n    On some platforms, path may also be specified as an open file descriptor.\n    If this functionality is unavailable, using it raises an exception.\n  mode\n    Operating-system mode bitfield.\n  dir_fd\n    If not None, it should be a file descriptor open to a directory,\n    and path should be relative; path will then be relative to that\n    directory.\n  follow_symlinks\n    If False, and the last element of the path is a symbolic link,\n    chmod will modify the symbolic link itself instead of the file\n    the link points to.\n\nIt is an error to use dir_fd or follow_symlinks when specifying path as\n  an open file descriptor.\ndir_fd and follow_symlinks may not be implemented on your platform.\n  If they are unavailable, using them will raise a NotImplementedError.'
    pass

def chown(path, uid, gid):
    'Change the owner and group id of path to the numeric uid and gid.\\\n\n  path\n    Path to be examined; can be string, bytes, a path-like object, or open-file-descriptor int.\n  dir_fd\n    If not None, it should be a file descriptor open to a directory,\n    and path should be relative; path will then be relative to that\n    directory.\n  follow_symlinks\n    If False, and the last element of the path is a symbolic link,\n    stat will examine the symbolic link itself instead of the file\n    the link points to.\n\npath may always be specified as a string.\nOn some platforms, path may also be specified as an open file descriptor.\n  If this functionality is unavailable, using it raises an exception.\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\nIf follow_symlinks is False, and the last element of the path is a symbolic\n  link, chown will modify the symbolic link itself instead of the file the\n  link points to.\nIt is an error to use dir_fd or follow_symlinks when specifying path as\n  an open file descriptor.\ndir_fd and follow_symlinks may not be implemented on your platform.\n  If they are unavailable, using them will raise a NotImplementedError.'
    pass

def chroot(path):
    'Change root directory to path.'
    pass

def close(fd):
    'Close a file descriptor.'
    pass

def closerange(fd_low, fd_high):
    'Closes all file descriptors in [fd_low, fd_high), ignoring errors.'
    pass

def confstr(name):
    'Return a string-valued system configuration variable.'
    pass

confstr_names = _mod_builtins.dict()
def cpu_count():
    'Return the number of CPUs in the system; return None if indeterminable.\n\nThis number is not equivalent to the number of CPUs the current process can\nuse.  The number of usable CPUs can be obtained with\n``len(os.sched_getaffinity(0))``'
    pass

def ctermid():
    'Return the name of the controlling terminal for this process.'
    pass

def device_encoding(fd):
    "Return a string describing the encoding of a terminal's file descriptor.\n\nThe file descriptor must be attached to a terminal.\nIf the device is not a terminal, return None."
    pass

def dup(fd):
    'Return a duplicate of a file descriptor.'
    pass

def dup2(fd, fd2, inheritable):
    'Duplicate file descriptor.'
    pass

environ = _mod_builtins.dict()
error = _mod_builtins.OSError
def execv(path, argv):
    'Execute an executable path with arguments, replacing current process.\n\n  path\n    Path of executable file.\n  argv\n    Tuple or list of strings.'
    pass

def execve(path, argv, env):
    'Execute an executable path with arguments, replacing current process.\n\n  path\n    Path of executable file.\n  argv\n    Tuple or list of strings.\n  env\n    Dictionary of strings mapping to strings.'
    pass

def fchdir(fd):
    'Change to the directory of the given file descriptor.\n\nfd must be opened on a directory, not a file.\nEquivalent to os.chdir(fd).'
    pass

def fchmod(fd, mode):
    'Change the access permissions of the file given by file descriptor fd.\n\nEquivalent to os.chmod(fd, mode).'
    pass

def fchown(fd, uid, gid):
    'Change the owner and group id of the file specified by file descriptor.\n\nEquivalent to os.chown(fd, uid, gid).'
    pass

def fdatasync(fd):
    'Force write of fd to disk without forcing update of metadata.'
    pass

def fork():
    'Fork a child process.\n\nReturn 0 to child process and PID of child to parent process.'
    pass

def forkpty():
    'Fork a new process with a new pseudo-terminal as controlling tty.\n\nReturns a tuple of (pid, master_fd).\nLike fork(), return pid of 0 to the child process,\nand pid of child to the parent process.\nTo both, return fd of newly opened pseudo-terminal.'
    pass

def fpathconf(fd, name):
    'Return the configuration limit name for the file descriptor fd.\n\nIf there is no limit, return -1.'
    pass

def fspath(path):
    'Return the file system path representation of the object.\n\nIf the object is str or bytes, then allow it to pass through as-is. If the\nobject defines __fspath__(), then return the result of that method. All other\ntypes raise a TypeError.'
    pass

def fstat(fd):
    'Perform a stat system call on the given file descriptor.\n\nLike stat(), but for an open file descriptor.\nEquivalent to os.stat(fd).'
    pass

def fstatvfs(fd):
    'Perform an fstatvfs system call on the given fd.\n\nEquivalent to statvfs(fd).'
    pass

def fsync(fd):
    'Force write of fd to disk.'
    pass

def ftruncate(fd, length):
    'Truncate a file, specified by file descriptor, to a specific length.'
    pass

def get_blocking(fd):
    'get_blocking(fd) -> bool\n\nGet the blocking mode of the file descriptor:\nFalse if the O_NONBLOCK flag is set, True if the flag is cleared.'
    return True

def get_inheritable(fd):
    'Get the close-on-exe flag of the specified file descriptor.'
    pass

def get_terminal_size():
    'Return the size of the terminal window as (columns, lines).\n\nThe optional argument fd (default standard output) specifies\nwhich file descriptor should be queried.\n\nIf the file descriptor is not connected to a terminal, an OSError\nis thrown.\n\nThis function will only be defined if an implementation is\navailable for this system.\n\nshutil.get_terminal_size is the high-level function which should \nnormally be used, os.get_terminal_size is the low-level implementation.'
    pass

def getcwd():
    'Return a unicode string representing the current working directory.'
    pass

def getcwdb():
    'Return a bytes string representing the current working directory.'
    pass

def getegid():
    "Return the current process's effective group id."
    pass

def geteuid():
    "Return the current process's effective user id."
    pass

def getgid():
    "Return the current process's group id."
    pass

def getgrouplist(user, group):
    'getgrouplist(user, group) -> list of groups to which a user belongs\n\nReturns a list of groups to which a user belongs.\n\n    user: username to lookup\n    group: base group id of the user'
    return list()

def getgroups():
    'Return list of supplemental group IDs for the process.'
    pass

def getloadavg():
    'Return average recent system load information.\n\nReturn the number of processes in the system run queue averaged over\nthe last 1, 5, and 15 minutes as a tuple of three floats.\nRaises OSError if the load average was unobtainable.'
    pass

def getlogin():
    'Return the actual login name.'
    pass

def getpgid(pid):
    'Call the system call getpgid(), and return the result.'
    pass

def getpgrp():
    'Return the current process group id.'
    pass

def getpid():
    'Return the current process id.'
    pass

def getppid():
    "Return the parent's process id.\n\nIf the parent process has already exited, Windows machines will still\nreturn its id; others systems will return the id of the 'init' process (1)."
    pass

def getpriority(which, who):
    'Return program scheduling priority.'
    pass

def getrandom(size, flags):
    'Obtain a series of random bytes.'
    pass

def getresgid():
    "Return a tuple of the current process's real, effective, and saved group ids."
    pass

def getresuid():
    "Return a tuple of the current process's real, effective, and saved user ids."
    pass

def getsid(pid):
    'Call the system call getsid(pid) and return the result.'
    pass

def getuid():
    "Return the current process's user id."
    pass

def getxattr(path, attribute):
    'Return the value of extended attribute attribute on path.\n\npath may be either a string, a path-like object, or an open file descriptor.\nIf follow_symlinks is False, and the last element of the path is a symbolic\n  link, getxattr will examine the symbolic link itself instead of the file\n  the link points to.'
    pass

def initgroups(username, gid):
    'initgroups(username, gid) -> None\n\nCall the system initgroups() to initialize the group access list with all of\nthe groups of which the specified username is a member, plus the specified\ngroup id.'
    pass

def isatty(fd):
    'Return True if the fd is connected to a terminal.\n\nReturn True if the file descriptor is an open file descriptor\nconnected to the slave end of a terminal.'
    pass

def kill(pid, signal):
    'Kill a process with a signal.'
    pass

def killpg(pgid, signal):
    'Kill a process group with a signal.'
    pass

def lchown(path, uid, gid):
    'Change the owner and group id of path to the numeric uid and gid.\n\nThis function will not follow symbolic links.\nEquivalent to os.chown(path, uid, gid, follow_symlinks=False).'
    pass

def link(src, dst):
    'Create a hard link to a file.\n\nIf either src_dir_fd or dst_dir_fd is not None, it should be a file\n  descriptor open to a directory, and the respective path string (src or dst)\n  should be relative; the path will then be relative to that directory.\nIf follow_symlinks is False, and the last element of src is a symbolic\n  link, link will create a link to the symbolic link itself instead of the\n  file the link points to.\nsrc_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your\n  platform.  If they are unavailable, using them will raise a\n  NotImplementedError.'
    pass

def listdir(path):
    "Return a list containing the names of the files in the directory.\n\npath can be specified as either str, bytes, or a path-like object.  If path is bytes,\n  the filenames returned will also be bytes; in all other circumstances\n  the filenames returned will be str.\nIf path is None, uses the path='.'.\nOn some platforms, path may also be specified as an open file descriptor;\\\n  the file descriptor must refer to a directory.\n  If this functionality is unavailable, using it raises NotImplementedError.\n\nThe list is in arbitrary order.  It does not include the special\nentries '.' and '..' even if they are present in the directory."
    pass

def listxattr(path):
    'Return a list of extended attributes on path.\n\npath may be either None, a string, a path-like object, or an open file descriptor.\nif path is None, listxattr will examine the current directory.\nIf follow_symlinks is False, and the last element of the path is a symbolic\n  link, listxattr will examine the symbolic link itself instead of the file\n  the link points to.'
    pass

def lockf(fd, command, length):
    'Apply, test or remove a POSIX lock on an open file descriptor.\n\n  fd\n    An open file descriptor.\n  command\n    One of F_LOCK, F_TLOCK, F_ULOCK or F_TEST.\n  length\n    The number of bytes to lock, starting at the current position.'
    pass

def lseek(fd, position, how):
    'Set the position of a file descriptor.  Return the new position.\n\nReturn the new cursor position in number of bytes\nrelative to the beginning of the file.'
    pass

def lstat(path):
    'Perform a stat system call on the given path, without following symbolic links.\n\nLike stat(), but do not follow symbolic links.\nEquivalent to stat(path, follow_symlinks=False).'
    pass

def major(device):
    'Extracts a device major number from a raw device number.'
    pass

def makedev(major, minor):
    'Composes a raw device number from the major and minor device numbers.'
    pass

def minor(device):
    'Extracts a device minor number from a raw device number.'
    pass

def mkdir(path, mode):
    'Create a directory.\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.\n\nThe mode argument is ignored on Windows.'
    pass

def mkfifo(path, mode):
    'Create a "fifo" (a POSIX named pipe).\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def mknod(path, mode, device):
    'Create a node in the file system.\n\nCreate a node in the file system (file, device special file or named pipe)\nat path.  mode specifies both the permissions to use and the\ntype of node to be created, being combined (bitwise OR) with one of\nS_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO.  If S_IFCHR or S_IFBLK is set on mode,\ndevice defines the newly created device special file (probably using\nos.makedev()).  Otherwise device is ignored.\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def nice(increment):
    'Add increment to the priority of process and return the new priority.'
    pass

def open(path, flags, mode):
    'Open a file for low level IO.  Returns a file descriptor (integer).\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def openpty():
    'Open a pseudo-terminal.\n\nReturn a tuple of (master_fd, slave_fd) containing open file descriptors\nfor both the master and slave ends.'
    pass

def pathconf(path, name):
    'Return the configuration limit name for the file or directory path.\n\nIf there is no limit, return -1.\nOn some platforms, path may also be specified as an open file descriptor.\n  If this functionality is unavailable, using it raises an exception.'
    pass

pathconf_names = _mod_builtins.dict()
def pipe():
    'Create a pipe.\n\nReturns a tuple of two file descriptors:\n  (read_fd, write_fd)'
    pass

def pipe2(flags):
    'Create a pipe with flags set atomically.\n\nReturns a tuple of two file descriptors:\n  (read_fd, write_fd)\n\nflags can be constructed by ORing together one or more of these values:\nO_NONBLOCK, O_CLOEXEC.'
    pass

def posix_fadvise(fd, offset, length, advice):
    'Announce an intention to access data in a specific pattern.\n\nAnnounce an intention to access data in a specific pattern, thus allowing\nthe kernel to make optimizations.\nThe advice applies to the region of the file specified by fd starting at\noffset and continuing for length bytes.\nadvice is one of POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL,\nPOSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, or\nPOSIX_FADV_DONTNEED.'
    pass

def posix_fallocate(fd, offset, length):
    'Ensure a file has allocated at least a particular number of bytes on disk.\n\nEnsure that the file specified by fd encompasses a range of bytes\nstarting at offset bytes from the beginning and continuing for length bytes.'
    pass

def pread(fd, length, offset):
    'Read a number of bytes from a file descriptor starting at a particular offset.\n\nRead length bytes from file descriptor fd, starting at offset bytes from\nthe beginning of the file.  The file offset remains unchanged.'
    pass

def preadv(fd, buffers, offset, flags):
    'Reads from a file descriptor into a number of mutable bytes-like objects.\n\nCombines the functionality of readv() and pread(). As readv(), it will\ntransfer data into each buffer until it is full and then move on to the next\nbuffer in the sequence to hold the rest of the data. Its fourth argument,\nspecifies the file offset at which the input operation is to be performed. It\nwill return the total number of bytes read (which can be less than the total\ncapacity of all the objects).\n\nThe flags argument contains a bitwise OR of zero or more of the following flags:\n\n- RWF_HIPRI\n- RWF_NOWAIT\n\nUsing non-zero flags requires Linux 4.6 or newer.'
    pass

def putenv(name, value):
    'Change or add an environment variable.'
    pass

def pwrite(fd, buffer, offset):
    'Write bytes to a file descriptor starting at a particular offset.\n\nWrite buffer to fd, starting at offset bytes from the beginning of\nthe file.  Returns the number of bytes writte.  Does not change the\ncurrent file offset.'
    pass

def pwritev(fd, buffers, offset, flags):
    'Writes the contents of bytes-like objects to a file descriptor at a given offset.\n\nCombines the functionality of writev() and pwrite(). All buffers must be a sequence\nof bytes-like objects. Buffers are processed in array order. Entire contents of first\nbuffer is written before proceeding to second, and so on. The operating system may\nset a limit (sysconf() value SC_IOV_MAX) on the number of buffers that can be used.\nThis function writes the contents of each object to the file descriptor and returns\nthe total number of bytes written.\n\nThe flags argument contains a bitwise OR of zero or more of the following flags:\n\n- RWF_DSYNC\n- RWF_SYNC\n\nUsing non-zero flags requires Linux 4.7 or newer.'
    pass

def read(fd, length):
    'Read from a file descriptor.  Returns a bytes object.'
    pass

def readlink(path, *, dir_fd=None):
    'readlink(path, *, dir_fd=None) -> path\n\nReturn a string representing the path to which the symbolic link points.\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def readv(fd, buffers):
    'Read from a file descriptor fd into an iterable of buffers.\n\nThe buffers should be mutable buffers accepting bytes.\nreadv will transfer data into each buffer until it is full\nand then move on to the next buffer in the sequence to hold\nthe rest of the data.\n\nreadv returns the total number of bytes read,\nwhich may be less than the total capacity of all the buffers.'
    pass

def register_at_fork():
    "Register callables to be called when forking a new process.\n\n  before\n    A callable to be called in the parent before the fork() syscall.\n  after_in_child\n    A callable to be called in the child after fork().\n  after_in_parent\n    A callable to be called in the parent after fork().\n\n'before' callbacks are called in reverse order.\n'after_in_child' and 'after_in_parent' callbacks are called in order."
    pass

def remove(path):
    'Remove a file (same as unlink()).\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def removexattr(path, attribute):
    'Remove extended attribute attribute on path.\n\npath may be either a string, a path-like object, or an open file descriptor.\nIf follow_symlinks is False, and the last element of the path is a symbolic\n  link, removexattr will modify the symbolic link itself instead of the file\n  the link points to.'
    pass

def rename(src, dst):
    'Rename a file or directory.\n\nIf either src_dir_fd or dst_dir_fd is not None, it should be a file\n  descriptor open to a directory, and the respective path string (src or dst)\n  should be relative; the path will then be relative to that directory.\nsrc_dir_fd and dst_dir_fd, may not be implemented on your platform.\n  If they are unavailable, using them will raise a NotImplementedError.'
    pass

def replace(src, dst):
    'Rename a file or directory, overwriting the destination.\n\nIf either src_dir_fd or dst_dir_fd is not None, it should be a file\n  descriptor open to a directory, and the respective path string (src or dst)\n  should be relative; the path will then be relative to that directory.\nsrc_dir_fd and dst_dir_fd, may not be implemented on your platform.\n  If they are unavailable, using them will raise a NotImplementedError.'
    pass

def rmdir(path):
    'Remove a directory.\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def scandir(path):
    "Return an iterator of DirEntry objects for given path.\n\npath can be specified as either str, bytes, or a path-like object.  If path\nis bytes, the names of yielded DirEntry objects will also be bytes; in\nall other circumstances they will be str.\n\nIf path is None, uses the path='.'."
    pass

def sched_get_priority_max(policy):
    'Get the maximum scheduling priority for policy.'
    pass

def sched_get_priority_min(policy):
    'Get the minimum scheduling priority for policy.'
    pass

def sched_getaffinity(pid):
    'Return the affinity of the process identified by pid (or the current process if zero).\n\nThe affinity is returned as a set of CPU identifiers.'
    pass

def sched_getparam(pid):
    'Returns scheduling parameters for the process identified by pid.\n\nIf pid is 0, returns parameters for the calling process.\nReturn value is an instance of sched_param.'
    pass

def sched_getscheduler(pid):
    'Get the scheduling policy for the process identifiedy by pid.\n\nPassing 0 for pid returns the scheduling policy for the calling process.'
    pass

class sched_param(_mod_builtins.tuple):
    'Current has only one field: sched_priority");\n\n  sched_priority\n    A scheduling parameter.'
    __class__ = sched_param
    def __init__(self, *args, **kwargs):
        'Current has only one field: sched_priority");\n\n  sched_priority\n    A scheduling parameter.'
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
    
    n_fields = 1
    n_sequence_fields = 1
    n_unnamed_fields = 0
    @property
    def sched_priority(self):
        'the scheduling priority'
        pass
    

def sched_rr_get_interval(pid):
    'Return the round-robin quantum for the process identified by pid, in seconds.\n\nValue returned is a float.'
    pass

def sched_setaffinity(pid, mask):
    'Set the CPU affinity of the process identified by pid to mask.\n\nmask should be an iterable of integers identifying CPUs.'
    pass

def sched_setparam(pid, param):
    'Set scheduling parameters for the process identified by pid.\n\nIf pid is 0, sets parameters for the calling process.\nparam should be an instance of sched_param.'
    pass

def sched_setscheduler(pid, policy, param):
    'Set the scheduling policy for the process identified by pid.\n\nIf pid is 0, the calling process is changed.\nparam is an instance of sched_param.'
    pass

def sched_yield():
    'Voluntarily relinquish the CPU.'
    pass

def sendfile(out, in_, offset, count, headers=None, trailers=None, flags=0):
    'sendfile(out, in, offset, count) -> byteswritten\nsendfile(out, in, offset, count[, headers][, trailers], flags=0)\n            -> byteswritten\nCopy count bytes from file descriptor in to file descriptor out.'
    pass

def set_blocking(fd, blocking):
    'set_blocking(fd, blocking)\n\nSet the blocking mode of the specified file descriptor.\nSet the O_NONBLOCK flag if blocking is False,\nclear the O_NONBLOCK flag otherwise.'
    pass

def set_inheritable(fd, inheritable):
    'Set the inheritable flag of the specified file descriptor.'
    pass

def setegid(egid):
    "Set the current process's effective group id."
    pass

def seteuid(euid):
    "Set the current process's effective user id."
    pass

def setgid(gid):
    "Set the current process's group id."
    pass

def setgroups(groups):
    'Set the groups of the current process to list.'
    pass

def setpgid(pid, pgrp):
    'Call the system call setpgid(pid, pgrp).'
    pass

def setpgrp():
    'Make the current process the leader of its process group.'
    pass

def setpriority(which, who, priority):
    'Set program scheduling priority.'
    pass

def setregid(rgid, egid):
    "Set the current process's real and effective group ids."
    pass

def setresgid(rgid, egid, sgid):
    "Set the current process's real, effective, and saved group ids."
    pass

def setresuid(ruid, euid, suid):
    "Set the current process's real, effective, and saved user ids."
    pass

def setreuid(ruid, euid):
    "Set the current process's real and effective user ids."
    pass

def setsid():
    'Call the system call setsid().'
    pass

def setuid(uid):
    "Set the current process's user id."
    pass

def setxattr(path, attribute, value, flags):
    'Set extended attribute attribute on path to value.\n\npath may be either a string, a path-like object,  or an open file descriptor.\nIf follow_symlinks is False, and the last element of the path is a symbolic\n  link, setxattr will modify the symbolic link itself instead of the file\n  the link points to.'
    pass

def stat(path):
    "Perform a stat system call on the given path.\n\n  path\n    Path to be examined; can be string, bytes, a path-like object or\n    open-file-descriptor int.\n  dir_fd\n    If not None, it should be a file descriptor open to a directory,\n    and path should be a relative string; path will then be relative to\n    that directory.\n  follow_symlinks\n    If False, and the last element of the path is a symbolic link,\n    stat will examine the symbolic link itself instead of the file\n    the link points to.\n\ndir_fd and follow_symlinks may not be implemented\n  on your platform.  If they are unavailable, using them will raise a\n  NotImplementedError.\n\nIt's an error to use dir_fd or follow_symlinks when specifying path as\n  an open file descriptor."
    pass

class stat_result(_mod_builtins.tuple):
    'stat_result: Result from stat, fstat, or lstat.\n\nThis object may be accessed either as a tuple of\n  (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)\nor via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.\n\nPosix/windows: If your platform supports st_blksize, st_blocks, st_rdev,\nor st_flags, they are available as attributes only.\n\nSee os.stat for more information.'
    __class__ = stat_result
    def __init__(self, *args, **kwargs):
        'stat_result: Result from stat, fstat, or lstat.\n\nThis object may be accessed either as a tuple of\n  (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)\nor via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.\n\nPosix/windows: If your platform supports st_blksize, st_blocks, st_rdev,\nor st_flags, they are available as attributes only.\n\nSee os.stat for more information.'
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
    
    n_fields = 19
    n_sequence_fields = 10
    n_unnamed_fields = 3
    @property
    def st_atime(self):
        'time of last access'
        pass
    
    @property
    def st_atime_ns(self):
        'time of last access in nanoseconds'
        pass
    
    @property
    def st_blksize(self):
        'blocksize for filesystem I/O'
        pass
    
    @property
    def st_blocks(self):
        'number of blocks allocated'
        pass
    
    @property
    def st_ctime(self):
        'time of last change'
        pass
    
    @property
    def st_ctime_ns(self):
        'time of last change in nanoseconds'
        pass
    
    @property
    def st_dev(self):
        'device'
        pass
    
    @property
    def st_gid(self):
        'group ID of owner'
        pass
    
    @property
    def st_ino(self):
        'inode'
        pass
    
    @property
    def st_mode(self):
        'protection bits'
        pass
    
    @property
    def st_mtime(self):
        'time of last modification'
        pass
    
    @property
    def st_mtime_ns(self):
        'time of last modification in nanoseconds'
        pass
    
    @property
    def st_nlink(self):
        'number of hard links'
        pass
    
    @property
    def st_rdev(self):
        'device type (if inode device)'
        pass
    
    @property
    def st_size(self):
        'total size, in bytes'
        pass
    
    @property
    def st_uid(self):
        'user ID of owner'
        pass
    

def statvfs(path):
    'Perform a statvfs system call on the given path.\n\npath may always be specified as a string.\nOn some platforms, path may also be specified as an open file descriptor.\n  If this functionality is unavailable, using it raises an exception.'
    pass

class statvfs_result(_mod_builtins.tuple):
    'statvfs_result: Result from statvfs or fstatvfs.\n\nThis object may be accessed either as a tuple of\n  (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),\nor via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.\n\nSee os.statvfs for more information.'
    __class__ = statvfs_result
    def __init__(self, *args, **kwargs):
        'statvfs_result: Result from statvfs or fstatvfs.\n\nThis object may be accessed either as a tuple of\n  (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),\nor via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.\n\nSee os.statvfs for more information.'
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
    def f_bavail(self):
        pass
    
    @property
    def f_bfree(self):
        pass
    
    @property
    def f_blocks(self):
        pass
    
    @property
    def f_bsize(self):
        pass
    
    @property
    def f_favail(self):
        pass
    
    @property
    def f_ffree(self):
        pass
    
    @property
    def f_files(self):
        pass
    
    @property
    def f_flag(self):
        pass
    
    @property
    def f_frsize(self):
        pass
    
    @property
    def f_fsid(self):
        pass
    
    @property
    def f_namemax(self):
        pass
    
    n_fields = 11
    n_sequence_fields = 10
    n_unnamed_fields = 0

def strerror(code):
    'Translate an error code to a message string.'
    pass

def symlink(src, dst, target_is_directory):
    'Create a symbolic link pointing to src named dst.\n\ntarget_is_directory is required on Windows if the target is to be\n  interpreted as a directory.  (On Windows, symlink requires\n  Windows 6.0 or greater, and raises a NotImplementedError otherwise.)\n  target_is_directory is ignored on non-Windows platforms.\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def sync():
    'Force write of everything to disk.'
    pass

def sysconf(name):
    'Return an integer-valued system configuration variable.'
    pass

sysconf_names = _mod_builtins.dict()
def system(command):
    'Execute the command in a subshell.'
    pass

def tcgetpgrp(fd):
    'Return the process group associated with the terminal specified by fd.'
    pass

def tcsetpgrp(fd, pgid):
    'Set the process group associated with the terminal specified by fd.'
    pass

terminal_size = _mod_os.terminal_size
def times():
    'Return a collection containing process timing information.\n\nThe object returned behaves like a named tuple with these fields:\n  (utime, stime, cutime, cstime, elapsed_time)\nAll fields are floating point numbers.'
    pass

class times_result(_mod_builtins.tuple):
    'times_result: Result from os.times().\n\nThis object may be accessed either as a tuple of\n  (user, system, children_user, children_system, elapsed),\nor via the attributes user, system, children_user, children_system,\nand elapsed.\n\nSee os.times for more information.'
    __class__ = times_result
    def __init__(self):
        'times_result: Result from os.times().\n\nThis object may be accessed either as a tuple of\n  (user, system, children_user, children_system, elapsed),\nor via the attributes user, system, children_user, children_system,\nand elapsed.\n\nSee os.times for more information.'
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
    def children_system(self):
        'system time of children'
        pass
    
    @property
    def children_user(self):
        'user time of children'
        pass
    
    @property
    def elapsed(self):
        'elapsed time since an arbitrary point in the past'
        pass
    
    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0
    @property
    def system(self):
        'system time'
        pass
    
    @property
    def user(self):
        'user time'
        pass
    

def truncate(path, length):
    'Truncate a file, specified by path, to a specific length.\n\nOn some platforms, path may also be specified as an open file descriptor.\n  If this functionality is unavailable, using it raises an exception.'
    pass

def ttyname(fd):
    "Return the name of the terminal device connected to 'fd'.\n\n  fd\n    Integer file descriptor handle."
    pass

def umask(mask):
    'Set the current numeric umask and return the previous umask.'
    pass

def uname():
    'Return an object identifying the current operating system.\n\nThe object behaves like a named tuple with the following fields:\n  (sysname, nodename, release, version, machine)'
    pass

class uname_result(_mod_builtins.tuple):
    'uname_result: Result from os.uname().\n\nThis object may be accessed either as a tuple of\n  (sysname, nodename, release, version, machine),\nor via the attributes sysname, nodename, release, version, and machine.\n\nSee os.uname for more information.'
    __class__ = uname_result
    def __init__(self):
        'uname_result: Result from os.uname().\n\nThis object may be accessed either as a tuple of\n  (sysname, nodename, release, version, machine),\nor via the attributes sysname, nodename, release, version, and machine.\n\nSee os.uname for more information.'
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
    def machine(self):
        'hardware identifier'
        pass
    
    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0
    @property
    def nodename(self):
        'name of machine on network (implementation-defined)'
        pass
    
    @property
    def release(self):
        'operating system release'
        pass
    
    @property
    def sysname(self):
        'operating system name'
        pass
    
    @property
    def version(self):
        'operating system version'
        pass
    

def unlink(path):
    'Remove a file (same as remove()).\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\ndir_fd may not be implemented on your platform.\n  If it is unavailable, using it will raise a NotImplementedError.'
    pass

def unsetenv(name):
    'Delete an environment variable.'
    pass

def urandom(size):
    'Return a bytes object containing random bytes suitable for cryptographic use.'
    pass

def utime(path, times):
    'Set the access and modified time of path.\n\npath may always be specified as a string.\nOn some platforms, path may also be specified as an open file descriptor.\n  If this functionality is unavailable, using it raises an exception.\n\nIf times is not None, it must be a tuple (atime, mtime);\n    atime and mtime should be expressed as float seconds since the epoch.\nIf ns is specified, it must be a tuple (atime_ns, mtime_ns);\n    atime_ns and mtime_ns should be expressed as integer nanoseconds\n    since the epoch.\nIf times is None and ns is unspecified, utime uses the current time.\nSpecifying tuples for both times and ns is an error.\n\nIf dir_fd is not None, it should be a file descriptor open to a directory,\n  and path should be relative; path will then be relative to that directory.\nIf follow_symlinks is False, and the last element of the path is a symbolic\n  link, utime will modify the symbolic link itself instead of the file the\n  link points to.\nIt is an error to use dir_fd or follow_symlinks when specifying path\n  as an open file descriptor.\ndir_fd and follow_symlinks may not be available on your platform.\n  If they are unavailable, using them will raise a NotImplementedError.'
    pass

def wait():
    'Wait for completion of a child process.\n\nReturns a tuple of information about the child process:\n    (pid, status)'
    pass

def wait3(options):
    'Wait for completion of a child process.\n\nReturns a tuple of information about the child process:\n  (pid, status, rusage)'
    pass

def wait4(pid, options):
    'Wait for completion of a specific child process.\n\nReturns a tuple of information about the child process:\n  (pid, status, rusage)'
    pass

def waitid(idtype, id, options):
    'Returns the result of waiting for a process or processes.\n\n  idtype\n    Must be one of be P_PID, P_PGID or P_ALL.\n  id\n    The id to wait on.\n  options\n    Constructed from the ORing of one or more of WEXITED, WSTOPPED\n    or WCONTINUED and additionally may be ORed with WNOHANG or WNOWAIT.\n\nReturns either waitid_result or None if WNOHANG is specified and there are\nno children in a waitable state.'
    pass

class waitid_result(_mod_builtins.tuple):
    'waitid_result: Result from waitid.\n\nThis object may be accessed either as a tuple of\n  (si_pid, si_uid, si_signo, si_status, si_code),\nor via the attributes si_pid, si_uid, and so on.\n\nSee os.waitid for more information.'
    __class__ = waitid_result
    def __init__(self, *args, **kwargs):
        'waitid_result: Result from waitid.\n\nThis object may be accessed either as a tuple of\n  (si_pid, si_uid, si_signo, si_status, si_code),\nor via the attributes si_pid, si_uid, and so on.\n\nSee os.waitid for more information.'
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
    
    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0
    @property
    def si_code(self):
        pass
    
    @property
    def si_pid(self):
        pass
    
    @property
    def si_signo(self):
        pass
    
    @property
    def si_status(self):
        pass
    
    @property
    def si_uid(self):
        pass
    

def waitpid(pid, options):
    'Wait for completion of a given child process.\n\nReturns a tuple of information regarding the child process:\n    (pid, status)\n\nThe options argument is ignored on Windows.'
    pass

def write(fd, data):
    'Write a bytes object to a file descriptor.'
    pass

def writev(fd, buffers):
    'Iterate over buffers, and write the contents of each to a file descriptor.\n\nReturns the total number of bytes written.\nbuffers must be a sequence of bytes-like objects.'
    pass

