__doc__ = 'A POSIX helper for the subprocess module.'
__file__ = '/usr/lib/python3.7/lib-dynload/_posixsubprocess.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_posixsubprocess'
__package__ = ''
def fork_exec():
    "fork_exec(args, executable_list, close_fds, cwd, env,\n          p2cread, p2cwrite, c2pread, c2pwrite,\n          errread, errwrite, errpipe_read, errpipe_write,\n          restore_signals, call_setsid, preexec_fn)\n\nForks a child process, closes parent file descriptors as appropriate in the\nchild and dups the few that are needed before calling exec() in the child\nprocess.\n\nThe preexec_fn, if supplied, will be called immediately before exec.\nWARNING: preexec_fn is NOT SAFE if your application uses threads.\n         It may trigger infrequent, difficult to debug deadlocks.\n\nIf an error occurs in the child process before the exec, it is\nserialized and written to the errpipe_write fd per subprocess.py.\n\nReturns: the child process's PID.\n\nRaises: Only on an error in the parent process.\n"
    pass

