import signal as _mod_signal

ITIMER_PROF = 2
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ItimerError = _mod_signal.ItimerError
NSIG = 65
SIGABRT = 6
SIGALRM = 14
SIGBUS = 7
SIGCHLD = 17
SIGCLD = 17
SIGCONT = 18
SIGFPE = 8
SIGHUP = 1
SIGILL = 4
SIGINT = 2
SIGIO = 29
SIGIOT = 6
SIGKILL = 9
SIGPIPE = 13
SIGPOLL = 29
SIGPROF = 27
SIGPWR = 30
SIGQUIT = 3
SIGRTMAX = 64
SIGRTMIN = 34
SIGSEGV = 11
SIGSTOP = 19
SIGSYS = 31
SIGTERM = 15
SIGTRAP = 5
SIGTSTP = 20
SIGTTIN = 21
SIGTTOU = 22
SIGURG = 23
SIGUSR1 = 10
SIGUSR2 = 12
SIGVTALRM = 26
SIGWINCH = 28
SIGXCPU = 24
SIGXFSZ = 25
SIG_BLOCK = 0
SIG_DFL = 0
SIG_IGN = 1
SIG_SETMASK = 2
SIG_UNBLOCK = 1
__doc__ = 'This module provides mechanisms to use signal handlers in Python.\n\nFunctions:\n\nalarm() -- cause SIGALRM after a specified time [Unix only]\nsetitimer() -- cause a signal (described below) after a specified\n               float time and the timer may restart then [Unix only]\ngetitimer() -- get current value of timer [Unix only]\nsignal() -- set the action for a given signal\ngetsignal() -- get the signal action for a given signal\npause() -- wait until a signal arrives [Unix only]\ndefault_int_handler() -- default SIGINT handler\n\nsignal constants:\nSIG_DFL -- used to refer to the system default handler\nSIG_IGN -- used to ignore the signal\nNSIG -- number of defined signals\nSIGINT, SIGTERM, etc. -- signal numbers\n\nitimer constants:\nITIMER_REAL -- decrements in real time, and delivers SIGALRM upon\n               expiration\nITIMER_VIRTUAL -- decrements only when the process is executing,\n               and delivers SIGVTALRM upon expiration\nITIMER_PROF -- decrements both when the process is executing and\n               when the system is executing on behalf of the process.\n               Coupled with ITIMER_VIRTUAL, this timer is usually\n               used to profile the time spent by the application\n               in user and kernel space. SIGPROF is delivered upon\n               expiration.\n\n\n*** IMPORTANT NOTICE ***\nA signal handler function is called with two arguments:\nthe first is the signal number, the second is the interrupted stack frame.'
__name__ = '_signal'
__package__ = ''
def alarm(seconds):
    'Arrange for SIGALRM to arrive after the given number of seconds.'
    pass

def default_int_handler():
    'default_int_handler(...)\n\nThe default handler for SIGINT installed by Python.\nIt raises KeyboardInterrupt.'
    pass

def getitimer(which):
    'Returns current value of given itimer.'
    pass

def getsignal(signalnum):
    'Return the current action for the given signal.\n\nThe return value can be:\n  SIG_IGN -- if the signal is being ignored\n  SIG_DFL -- if the default action for the signal is in effect\n  None    -- if an unknown handler is in effect\n  anything else -- the callable Python object used as a handler'
    pass

def pause():
    'Wait until a signal arrives.'
    pass

def pthread_kill(thread_id, signalnum):
    'Send a signal to a thread.'
    pass

def pthread_sigmask(how, mask):
    'Fetch and/or change the signal mask of the calling thread.'
    pass

def set_wakeup_fd(fd, *, warn_on_full_buffer=True):
    'set_wakeup_fd(fd, *, warn_on_full_buffer=True) -> fd\n\nSets the fd to be written to (with the signal number) when a signal\ncomes in.  A library can use this to wakeup select or poll.\nThe previous fd or -1 is returned.\n\nThe fd must be non-blocking.'
    pass

def setitimer(which, seconds, interval):
    'Sets given itimer (one of ITIMER_REAL, ITIMER_VIRTUAL or ITIMER_PROF).\n\nThe timer will fire after value seconds and after that every interval seconds.\nThe itimer can be cleared by setting seconds to zero.\n\nReturns old values as a tuple: (delay, interval).'
    pass

def siginterrupt(signalnum, flag):
    'Change system call restart behaviour.\n\nIf flag is False, system calls will be restarted when interrupted by\nsignal sig, else system calls will be interrupted.'
    pass

def signal(signalnum, handler):
    'Set the action for the given signal.\n\nThe action can be SIG_DFL, SIG_IGN, or a callable Python object.\nThe previous action is returned.  See getsignal() for possible return values.\n\n*** IMPORTANT NOTICE ***\nA signal handler function is called with two arguments:\nthe first is the signal number, the second is the interrupted stack frame.'
    pass

def sigpending():
    'Examine pending signals.\n\nReturns a set of signal numbers that are pending for delivery to\nthe calling thread.'
    pass

def sigtimedwait(sigset, timeout):
    'Like sigwaitinfo(), but with a timeout.\n\nThe timeout is specified in seconds, with floating point numbers allowed.'
    pass

def sigwait(sigset):
    'Wait for a signal.\n\nSuspend execution of the calling thread until the delivery of one of the\nsignals specified in the signal set sigset.  The function accepts the signal\nand returns the signal number.'
    pass

def sigwaitinfo(sigset):
    'Wait synchronously until one of the signals in *sigset* is delivered.\n\nReturns a struct_siginfo containing information about the signal.'
    pass

struct_siginfo = _mod_signal.struct_siginfo
