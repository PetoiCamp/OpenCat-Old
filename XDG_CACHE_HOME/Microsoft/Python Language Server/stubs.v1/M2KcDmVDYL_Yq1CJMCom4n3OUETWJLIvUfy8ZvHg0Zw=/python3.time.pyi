import builtins as _mod_builtins

CLOCK_BOOTTIME = 7
CLOCK_MONOTONIC = 1
CLOCK_MONOTONIC_RAW = 4
CLOCK_PROCESS_CPUTIME_ID = 2
CLOCK_REALTIME = 0
CLOCK_THREAD_CPUTIME_ID = 3
_STRUCT_TM_ITEMS = 11
__doc__ = 'This module provides various functions to manipulate time values.\n\nThere are two standard representations of time.  One is the number\nof seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer\nor a floating point number (to represent fractions of seconds).\nThe Epoch is system-defined; on Unix, it is generally January 1st, 1970.\nThe actual value can be retrieved by calling gmtime(0).\n\nThe other representation is a tuple of 9 integers giving local time.\nThe tuple items are:\n  year (including century, e.g. 1998)\n  month (1-12)\n  day (1-31)\n  hours (0-23)\n  minutes (0-59)\n  seconds (0-59)\n  weekday (0-6, Monday is 0)\n  Julian day (day in the year, 1-366)\n  DST (Daylight Savings Time) flag (-1, 0 or 1)\nIf the DST flag is 0, the time is given in the regular time zone;\nif it is 1, the time is given in the DST time zone;\nif it is -1, mktime() should guess based on the date and time.\n'
__name__ = 'time'
__package__ = ''
altzone = 14400
def asctime(tuple=None):
    "asctime([tuple]) -> string\n\nConvert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.\nWhen the time tuple is not present, current time as returned by localtime()\nis used."
    return ''

def clock():
    'clock() -> floating point number\n\nReturn the CPU time or real time since the start of the process or since\nthe first call to clock().  This has as much precision as the system\nrecords.'
    return 1.0

def clock_getres(clk_id):
    'clock_getres(clk_id) -> floating point number\n\nReturn the resolution (precision) of the specified clock clk_id.'
    return 1.0

def clock_gettime(clk_id):
    'clock_gettime(clk_id) -> float\n\nReturn the time of the specified clock clk_id.'
    return 1.0

def clock_gettime_ns(clk_id):
    'clock_gettime_ns(clk_id) -> int\n\nReturn the time of the specified clock clk_id as nanoseconds.'
    return 1

def clock_settime(clk_id, time):
    'clock_settime(clk_id, time)\n\nSet the time of the specified clock clk_id.'
    pass

def clock_settime_ns(clk_id, time):
    'clock_settime_ns(clk_id, time)\n\nSet the time of the specified clock clk_id with nanoseconds.'
    pass

def ctime(seconds):
    'ctime(seconds) -> string\n\nConvert a time in seconds since the Epoch to a string in local time.\nThis is equivalent to asctime(localtime(seconds)). When the time tuple is\nnot present, current time as returned by localtime() is used.'
    return ''

daylight = 1
def get_clock_info(name: str):
    'get_clock_info(name: str) -> dict\n\nGet information of the specified clock.'
    return dict()

def gmtime():
    "gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,\n                       tm_sec, tm_wday, tm_yday, tm_isdst)\n\nConvert seconds since the Epoch to a time tuple expressing UTC (a.k.a.\nGMT).  When 'seconds' is not passed in, convert the current time instead.\n\nIf the platform supports the tm_gmtoff and tm_zone, they are available as\nattributes only."
    return tuple()

def localtime():
    "localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,\n                          tm_sec,tm_wday,tm_yday,tm_isdst)\n\nConvert seconds since the Epoch to a time tuple expressing local time.\nWhen 'seconds' is not passed in, convert the current time instead."
    return tuple()

def mktime(tuple):
    'mktime(tuple) -> floating point number\n\nConvert a time tuple in local time to seconds since the Epoch.\nNote that mktime(gmtime(0)) will not generally return zero for most\ntime zones; instead the returned value will either be equal to that\nof the timezone or altzone attributes on the time module.'
    return 1.0

def monotonic():
    'monotonic() -> float\n\nMonotonic clock, cannot go backward.'
    return 1.0

def monotonic_ns():
    'monotonic_ns() -> int\n\nMonotonic clock, cannot go backward, as nanoseconds.'
    return 1

def perf_counter():
    'perf_counter() -> float\n\nPerformance counter for benchmarking.'
    return 1.0

def perf_counter_ns():
    'perf_counter_ns() -> int\n\nPerformance counter for benchmarking as nanoseconds.'
    return 1

def process_time():
    'process_time() -> float\n\nProcess time for profiling: sum of the kernel and user-space CPU time.'
    return 1.0

def process_time_ns():
    'process_time() -> int\n\nProcess time for profiling as nanoseconds:\nsum of the kernel and user-space CPU time.'
    return 1

def pthread_getcpuclockid(thread_id):
    "pthread_getcpuclockid(thread_id) -> int\n\nReturn the clk_id of a thread's CPU time clock."
    return 1

def sleep(seconds):
    'sleep(seconds)\n\nDelay execution for a given number of seconds.  The argument may be\na floating point number for subsecond precision.'
    pass

def strftime(format, tuple=None):
    "strftime(format[, tuple]) -> string\n\nConvert a time tuple to a string according to a format specification.\nSee the library reference manual for formatting codes. When the time tuple\nis not present, current time as returned by localtime() is used.\n\nCommonly used format codes:\n\n%Y  Year with century as a decimal number.\n%m  Month as a decimal number [01,12].\n%d  Day of the month as a decimal number [01,31].\n%H  Hour (24-hour clock) as a decimal number [00,23].\n%M  Minute as a decimal number [00,59].\n%S  Second as a decimal number [00,61].\n%z  Time zone offset from UTC.\n%a  Locale's abbreviated weekday name.\n%A  Locale's full weekday name.\n%b  Locale's abbreviated month name.\n%B  Locale's full month name.\n%c  Locale's appropriate date and time representation.\n%I  Hour (12-hour clock) as a decimal number [01,12].\n%p  Locale's equivalent of either AM or PM.\n\nOther codes may be available on your platform.  See documentation for\nthe C library strftime function.\n"
    return ''

def strptime(string, format):
    "strptime(string, format) -> struct_time\n\nParse a string to a time tuple according to a format specification.\nSee the library reference manual for formatting codes (same as\nstrftime()).\n\nCommonly used format codes:\n\n%Y  Year with century as a decimal number.\n%m  Month as a decimal number [01,12].\n%d  Day of the month as a decimal number [01,31].\n%H  Hour (24-hour clock) as a decimal number [00,23].\n%M  Minute as a decimal number [00,59].\n%S  Second as a decimal number [00,61].\n%z  Time zone offset from UTC.\n%a  Locale's abbreviated weekday name.\n%A  Locale's full weekday name.\n%b  Locale's abbreviated month name.\n%B  Locale's full month name.\n%c  Locale's appropriate date and time representation.\n%I  Hour (12-hour clock) as a decimal number [01,12].\n%p  Locale's equivalent of either AM or PM.\n\nOther codes may be available on your platform.  See documentation for\nthe C library strftime function.\n"
    return ''

class struct_time(_mod_builtins.tuple):
    "The time value as returned by gmtime(), localtime(), and strptime(), and\n accepted by asctime(), mktime() and strftime().  May be considered as a\n sequence of 9 integers.\n\n Note that several fields' values are not the same as those defined by\n the C language standard for struct tm.  For example, the value of the\n field tm_year is the actual year, not year - 1900.  See individual\n fields' descriptions for details."
    __class__ = struct_time
    def __init__(self):
        "The time value as returned by gmtime(), localtime(), and strptime(), and\n accepted by asctime(), mktime() and strftime().  May be considered as a\n sequence of 9 integers.\n\n Note that several fields' values are not the same as those defined by\n the C language standard for struct tm.  For example, the value of the\n field tm_year is the actual year, not year - 1900.  See individual\n fields' descriptions for details."
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
    
    n_fields = 11
    n_sequence_fields = 9
    n_unnamed_fields = 0
    @property
    def tm_gmtoff(self):
        'offset from UTC in seconds'
        pass
    
    @property
    def tm_hour(self):
        'hours, range [0, 23]'
        pass
    
    @property
    def tm_isdst(self):
        '1 if summer time is in effect, 0 if not, and -1 if unknown'
        pass
    
    @property
    def tm_mday(self):
        'day of month, range [1, 31]'
        pass
    
    @property
    def tm_min(self):
        'minutes, range [0, 59]'
        pass
    
    @property
    def tm_mon(self):
        'month of year, range [1, 12]'
        pass
    
    @property
    def tm_sec(self):
        'seconds, range [0, 61])'
        pass
    
    @property
    def tm_wday(self):
        'day of week, range [0, 6], Monday is 0'
        pass
    
    @property
    def tm_yday(self):
        'day of year, range [1, 366]'
        pass
    
    @property
    def tm_year(self):
        'year, for example, 1993'
        pass
    
    @property
    def tm_zone(self):
        'abbreviation of timezone name'
        pass
    

def thread_time():
    'thread_time() -> float\n\nThread time for profiling: sum of the kernel and user-space CPU time.'
    return 1.0

def thread_time_ns():
    'thread_time() -> int\n\nThread time for profiling as nanoseconds:\nsum of the kernel and user-space CPU time.'
    return 1

def time():
    'time() -> floating point number\n\nReturn the current time in seconds since the Epoch.\nFractions of a second may be present if the system clock provides them.'
    return 1.0

def time_ns():
    'time_ns() -> int\n\nReturn the current time in nanoseconds since the Epoch.'
    return 1

timezone = 18000
tzname = _mod_builtins.tuple()
def tzset():
    "tzset()\n\nInitialize, or reinitialize, the local timezone to the value stored in\nos.environ['TZ']. The TZ environment variable should be specified in\nstandard Unix timezone format as documented in the tzset man page\n(eg. 'US/Eastern', 'Europe/Amsterdam'). Unknown timezones will silently\nfall back to UTC. If the TZ environment variable is not set, the local\ntimezone is set to the systems best guess of wallclock time.\nChanging the TZ environment variable without calling tzset *may* change\nthe local timezone used by methods such as localtime, but this behaviour\nshould not be relied on."
    pass

