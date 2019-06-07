class PyCapsule(object):
    'Capsule objects let you wrap a C "void *" pointer in a Python\nobject.  They\'re a way of passing data through the Python interpreter\nwithout creating your own custom type.\n\nCapsules are used for communication between extension modules.\nThey provide a way for an extension module to export a C interface\nto other extension modules, so that extension modules can use the\nPython import mechanism to link to one another.\n'
    __class__ = PyCapsule
    def __init__(self, *args, **kwargs):
        'Capsule objects let you wrap a C "void *" pointer in a Python\nobject.  They\'re a way of passing data through the Python interpreter\nwithout creating your own custom type.\n\nCapsules are used for communication between extension modules.\nThey provide a way for an extension module to export a C interface\nto other extension modules, so that extension modules can use the\nPython import mechanism to link to one another.\n'
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
    

OSError = type()
AF_ALG = 38
AF_APPLETALK = 5
AF_ASH = 18
AF_ATMPVC = 8
AF_ATMSVC = 20
AF_AX25 = 3
AF_BRIDGE = 7
AF_CAN = 29
AF_DECnet = 12
AF_ECONET = 19
AF_INET = 2
AF_INET6 = 10
AF_IPX = 4
AF_IRDA = 23
AF_KEY = 15
AF_LLC = 26
AF_NETBEUI = 13
AF_NETLINK = 16
AF_NETROM = 6
AF_PACKET = 17
AF_PPPOX = 24
AF_RDS = 21
AF_ROSE = 11
AF_ROUTE = 16
AF_SECURITY = 14
AF_SNA = 22
AF_TIPC = 30
AF_UNIX = 1
AF_UNSPEC = 0
AF_VSOCK = 40
AF_WANPIPE = 25
AF_X25 = 9
AI_ADDRCONFIG = 32
AI_ALL = 16
AI_CANONNAME = 2
AI_NUMERICHOST = 4
AI_NUMERICSERV = 1024
AI_PASSIVE = 1
AI_V4MAPPED = 8
ALG_OP_DECRYPT = 0
ALG_OP_ENCRYPT = 1
ALG_OP_SIGN = 2
ALG_OP_VERIFY = 3
ALG_SET_AEAD_ASSOCLEN = 4
ALG_SET_AEAD_AUTHSIZE = 5
ALG_SET_IV = 2
ALG_SET_KEY = 1
ALG_SET_OP = 3
ALG_SET_PUBKEY = 6
CAN_BCM = 2
CAN_BCM_RX_CHANGED = 12
CAN_BCM_RX_DELETE = 6
CAN_BCM_RX_READ = 7
CAN_BCM_RX_SETUP = 5
CAN_BCM_RX_STATUS = 10
CAN_BCM_RX_TIMEOUT = 11
CAN_BCM_TX_DELETE = 2
CAN_BCM_TX_EXPIRED = 9
CAN_BCM_TX_READ = 3
CAN_BCM_TX_SEND = 4
CAN_BCM_TX_SETUP = 1
CAN_BCM_TX_STATUS = 8
CAN_EFF_FLAG = 2147483648
CAN_EFF_MASK = 536870911
CAN_ERR_FLAG = 536870912
CAN_ERR_MASK = 536870911
CAN_ISOTP = 6
CAN_RAW = 1
CAN_RAW_ERR_FILTER = 2
CAN_RAW_FD_FRAMES = 5
CAN_RAW_FILTER = 1
CAN_RAW_LOOPBACK = 3
CAN_RAW_RECV_OWN_MSGS = 4
CAN_RTR_FLAG = 1073741824
CAN_SFF_MASK = 2047
CAPI = PyCapsule()
def CMSG_LEN(length):
    'CMSG_LEN(length) -> control message length\n\nReturn the total length, without trailing padding, of an ancillary\ndata item with associated data of the given length.  This value can\noften be used as the buffer size for recvmsg() to receive a single\nitem of ancillary data, but RFC 3542 requires portable applications to\nuse CMSG_SPACE() and thus include space for padding, even when the\nitem will be the last in the buffer.  Raises OverflowError if length\nis outside the permissible range of values.'
    pass

def CMSG_SPACE(length):
    'CMSG_SPACE(length) -> buffer size\n\nReturn the buffer size needed for recvmsg() to receive an ancillary\ndata item with associated data of the given length, along with any\ntrailing padding.  The buffer space needed to receive multiple items\nis the sum of the CMSG_SPACE() values for their associated data\nlengths.  Raises OverflowError if length is outside the permissible\nrange of values.'
    pass

EAI_ADDRFAMILY = -9
EAI_AGAIN = -3
EAI_BADFLAGS = -1
EAI_FAIL = -4
EAI_FAMILY = -6
EAI_MEMORY = -10
EAI_NODATA = -5
EAI_NONAME = -2
EAI_OVERFLOW = -12
EAI_SERVICE = -8
EAI_SOCKTYPE = -7
EAI_SYSTEM = -11
INADDR_ALLHOSTS_GROUP = 3758096385
INADDR_ANY = 0
INADDR_BROADCAST = 4294967295
INADDR_LOOPBACK = 2130706433
INADDR_MAX_LOCAL_GROUP = 3758096639
INADDR_NONE = 4294967295
INADDR_UNSPEC_GROUP = 3758096384
IOCTL_VM_SOCKETS_GET_LOCAL_CID = 1977
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000
IPPROTO_AH = 51
IPPROTO_DSTOPTS = 60
IPPROTO_EGP = 8
IPPROTO_ESP = 50
IPPROTO_FRAGMENT = 44
IPPROTO_GRE = 47
IPPROTO_HOPOPTS = 0
IPPROTO_ICMP = 1
IPPROTO_ICMPV6 = 58
IPPROTO_IDP = 22
IPPROTO_IGMP = 2
IPPROTO_IP = 0
IPPROTO_IPIP = 4
IPPROTO_IPV6 = 41
IPPROTO_NONE = 59
IPPROTO_PIM = 103
IPPROTO_PUP = 12
IPPROTO_RAW = 255
IPPROTO_ROUTING = 43
IPPROTO_RSVP = 46
IPPROTO_SCTP = 132
IPPROTO_TCP = 6
IPPROTO_TP = 29
IPPROTO_UDP = 17
IPV6_CHECKSUM = 7
IPV6_DONTFRAG = 62
IPV6_DSTOPTS = 59
IPV6_HOPLIMIT = 52
IPV6_HOPOPTS = 54
IPV6_JOIN_GROUP = 20
IPV6_LEAVE_GROUP = 21
IPV6_MULTICAST_HOPS = 18
IPV6_MULTICAST_IF = 17
IPV6_MULTICAST_LOOP = 19
IPV6_NEXTHOP = 9
IPV6_PATHMTU = 61
IPV6_PKTINFO = 50
IPV6_RECVDSTOPTS = 58
IPV6_RECVHOPLIMIT = 51
IPV6_RECVHOPOPTS = 53
IPV6_RECVPATHMTU = 60
IPV6_RECVPKTINFO = 49
IPV6_RECVRTHDR = 56
IPV6_RECVTCLASS = 66
IPV6_RTHDR = 57
IPV6_RTHDRDSTOPTS = 55
IPV6_RTHDR_TYPE_0 = 0
IPV6_TCLASS = 67
IPV6_UNICAST_HOPS = 16
IPV6_V6ONLY = 26
IP_ADD_MEMBERSHIP = 35
IP_DEFAULT_MULTICAST_LOOP = 1
IP_DEFAULT_MULTICAST_TTL = 1
IP_DROP_MEMBERSHIP = 36
IP_HDRINCL = 3
IP_MAX_MEMBERSHIPS = 20
IP_MULTICAST_IF = 32
IP_MULTICAST_LOOP = 34
IP_MULTICAST_TTL = 33
IP_OPTIONS = 4
IP_RECVOPTS = 6
IP_RECVRETOPTS = 7
IP_RETOPTS = 7
IP_TOS = 1
IP_TRANSPARENT = 19
IP_TTL = 2
MSG_CMSG_CLOEXEC = 1073741824
MSG_CONFIRM = 2048
MSG_CTRUNC = 8
MSG_DONTROUTE = 4
MSG_DONTWAIT = 64
MSG_EOR = 128
MSG_ERRQUEUE = 8192
MSG_FASTOPEN = 536870912
MSG_MORE = 32768
MSG_NOSIGNAL = 16384
MSG_OOB = 1
MSG_PEEK = 2
MSG_TRUNC = 32
MSG_WAITALL = 256
NETLINK_CRYPTO = 21
NETLINK_DNRTMSG = 14
NETLINK_FIREWALL = 3
NETLINK_IP6_FW = 13
NETLINK_NFLOG = 5
NETLINK_ROUTE = 0
NETLINK_USERSOCK = 2
NETLINK_XFRM = 6
NI_DGRAM = 16
NI_MAXHOST = 1025
NI_MAXSERV = 32
NI_NAMEREQD = 8
NI_NOFQDN = 4
NI_NUMERICHOST = 1
NI_NUMERICSERV = 2
PACKET_BROADCAST = 1
PACKET_FASTROUTE = 6
PACKET_HOST = 0
PACKET_LOOPBACK = 5
PACKET_MULTICAST = 2
PACKET_OTHERHOST = 3
PACKET_OUTGOING = 4
PF_CAN = 29
PF_PACKET = 17
PF_RDS = 21
SCM_CREDENTIALS = 2
SCM_RIGHTS = 1
SHUT_RD = 0
SHUT_RDWR = 2
SHUT_WR = 1
SOCK_CLOEXEC = 524288
SOCK_DGRAM = 2
SOCK_NONBLOCK = 2048
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SOCK_STREAM = 1
SOL_ALG = 279
SOL_CAN_BASE = 100
SOL_CAN_RAW = 101
SOL_IP = 0
SOL_RDS = 276
SOL_SOCKET = 1
SOL_TCP = 6
SOL_TIPC = 271
SOL_UDP = 17
SOMAXCONN = 128
SO_ACCEPTCONN = 30
SO_BINDTODEVICE = 25
SO_BROADCAST = 6
SO_DEBUG = 1
SO_DOMAIN = 39
SO_DONTROUTE = 5
SO_ERROR = 4
SO_KEEPALIVE = 9
SO_LINGER = 13
SO_MARK = 36
SO_OOBINLINE = 10
SO_PASSCRED = 16
SO_PASSSEC = 34
SO_PEERCRED = 17
SO_PEERSEC = 31
SO_PRIORITY = 12
SO_PROTOCOL = 38
SO_RCVBUF = 8
SO_RCVLOWAT = 18
SO_RCVTIMEO = 20
SO_REUSEADDR = 2
SO_REUSEPORT = 15
SO_SNDBUF = 7
SO_SNDLOWAT = 19
SO_SNDTIMEO = 21
SO_TYPE = 3
SO_VM_SOCKETS_BUFFER_MAX_SIZE = 2
SO_VM_SOCKETS_BUFFER_MIN_SIZE = 1
SO_VM_SOCKETS_BUFFER_SIZE = 0
SocketType = socket()
TCP_CONGESTION = 13
TCP_CORK = 3
TCP_DEFER_ACCEPT = 9
TCP_FASTOPEN = 23
TCP_INFO = 11
TCP_KEEPCNT = 6
TCP_KEEPIDLE = 4
TCP_KEEPINTVL = 5
TCP_LINGER2 = 8
TCP_MAXSEG = 2
TCP_NODELAY = 1
TCP_NOTSENT_LOWAT = 25
TCP_QUICKACK = 12
TCP_SYNCNT = 7
TCP_USER_TIMEOUT = 18
TCP_WINDOW_CLAMP = 10
TIPC_ADDR_ID = 3
TIPC_ADDR_NAME = 2
TIPC_ADDR_NAMESEQ = 1
TIPC_CFG_SRV = 0
TIPC_CLUSTER_SCOPE = 2
TIPC_CONN_TIMEOUT = 130
TIPC_CRITICAL_IMPORTANCE = 3
TIPC_DEST_DROPPABLE = 129
TIPC_HIGH_IMPORTANCE = 2
TIPC_IMPORTANCE = 127
TIPC_LOW_IMPORTANCE = 0
TIPC_MEDIUM_IMPORTANCE = 1
TIPC_NODE_SCOPE = 3
TIPC_PUBLISHED = 1
TIPC_SRC_DROPPABLE = 128
TIPC_SUBSCR_TIMEOUT = 3
TIPC_SUB_CANCEL = 4
TIPC_SUB_PORTS = 1
TIPC_SUB_SERVICE = 2
TIPC_TOP_SRV = 1
TIPC_WAIT_FOREVER = -1
TIPC_WITHDRAWN = 2
TIPC_ZONE_SCOPE = 1
VMADDR_CID_ANY = 4294967295
VMADDR_CID_HOST = 2
VMADDR_PORT_ANY = 4294967295
VM_SOCKETS_INVALID_VERSION = 4294967295
__doc__ = 'Implementation module for socket operations.\n\nSee the socket module for documentation.'
__file__ = '/usr/lib/python3.7/lib-dynload/_socket.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_socket'
__package__ = ''
def close(integer):
    "close(integer) -> None\n\nClose an integer socket file descriptor.  This is like os.close(), but for\nsockets; on some platforms os.close() won't work for socket file descriptors."
    pass

def dup(integer):
    "dup(integer) -> integer\n\nDuplicate an integer socket file descriptor.  This is like os.dup(), but for\nsockets; on some platforms os.dup() won't work for socket file descriptors."
    return 1

error = OSError()
class gaierror(OSError):
    __class__ = gaierror
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def getaddrinfo(host, port, family=None, type=None, proto=None, flags=None):
    'getaddrinfo(host, port [, family, type, proto, flags])\n    -> list of (family, type, proto, canonname, sockaddr)\n\nResolve host and port into addrinfo struct.'
    pass

def getdefaulttimeout():
    'getdefaulttimeout() -> timeout\n\nReturns the default timeout in seconds (float) for new socket objects.\nA value of None indicates that new socket objects have no timeout.\nWhen the socket module is first imported, the default is None.'
    pass

def gethostbyaddr(host):
    'gethostbyaddr(host) -> (name, aliaslist, addresslist)\n\nReturn the true host name, a list of aliases, and a list of IP addresses,\nfor a host.  The host argument is a string giving a host name or IP number.'
    return tuple()

def gethostbyname(host):
    "gethostbyname(host) -> address\n\nReturn the IP address (a string of the form '255.255.255.255') for a host."
    pass

def gethostbyname_ex(host):
    'gethostbyname_ex(host) -> (name, aliaslist, addresslist)\n\nReturn the true host name, a list of aliases, and a list of IP addresses,\nfor a host.  The host argument is a string giving a host name or IP number.'
    return tuple()

def gethostname():
    'gethostname() -> string\n\nReturn the current host name.'
    return ''

def getnameinfo(sockaddr, flags):
    'getnameinfo(sockaddr, flags) --> (host, port)\n\nGet host and port for a sockaddr.'
    return tuple()

def getprotobyname(name):
    'getprotobyname(name) -> integer\n\nReturn the protocol number for the named protocol.  (Rarely used.)'
    return 1

def getservbyname(servicename, protocolname=None):
    "getservbyname(servicename[, protocolname]) -> integer\n\nReturn a port number from a service name and protocol name.\nThe optional protocol name, if given, should be 'tcp' or 'udp',\notherwise any protocol will match."
    return 1

def getservbyport(port, protocolname=None):
    "getservbyport(port[, protocolname]) -> string\n\nReturn the service name from a port number and protocol name.\nThe optional protocol name, if given, should be 'tcp' or 'udp',\notherwise any protocol will match."
    return ''

has_ipv6 = True
class herror(OSError):
    __class__ = herror
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def htonl(integer):
    'htonl(integer) -> integer\n\nConvert a 32-bit integer from host to network byte order.'
    return 1

def htons(integer):
    'htons(integer) -> integer\n\nConvert a 16-bit unsigned integer from host to network byte order.\nNote that in case the received integer does not fit in 16-bit unsigned\ninteger, but does fit in a positive C int, it is silently truncated to\n16-bit unsigned integer.\nHowever, this silent truncation feature is deprecated, and will raise an \nexception in future versions of Python.'
    return 1

def if_indextoname(if_index):
    'if_indextoname(if_index)\n\nReturns the interface name corresponding to the interface index if_index.'
    pass

def if_nameindex():
    'if_nameindex()\n\nReturns a list of network interface information (index, name) tuples.'
    pass

def if_nametoindex(if_name):
    'if_nametoindex(if_name)\n\nReturns the interface index corresponding to the interface name if_name.'
    pass

def inet_aton(string):
    'inet_aton(string) -> bytes giving packed 32-bit IP representation\n\nConvert an IP address in string format (123.45.67.89) to the 32-bit packed\nbinary format used in low-level network functions.'
    pass

def inet_ntoa(packed_ip):
    'inet_ntoa(packed_ip) -> ip_address_string\n\nConvert an IP address from 32-bit packed binary format to string format'
    pass

def inet_ntop(af, packed_ip):
    'inet_ntop(af, packed_ip) -> string formatted IP address\n\nConvert a packed IP address of the given family to string format.'
    return ''

def inet_pton(af, ip):
    'inet_pton(af, ip) -> packed IP address string\n\nConvert an IP address from string format to a packed string suitable\nfor use with low-level network functions.'
    pass

def ntohl(integer):
    'ntohl(integer) -> integer\n\nConvert a 32-bit integer from network to host byte order.'
    return 1

def ntohs(integer):
    'ntohs(integer) -> integer\n\nConvert a 16-bit unsigned integer from network to host byte order.\nNote that in case the received integer does not fit in 16-bit unsigned\ninteger, but does fit in a positive C int, it is silently truncated to\n16-bit unsigned integer.\nHowever, this silent truncation feature is deprecated, and will raise an \nexception in future versions of Python.'
    return 1

def setdefaulttimeout(timeout):
    'setdefaulttimeout(timeout)\n\nSet the default timeout in seconds (float) for new socket objects.\nA value of None indicates that new socket objects have no timeout.\nWhen the socket module is first imported, the default is None.'
    pass

def sethostname(name):
    'sethostname(name)\n\nSets the hostname to name.'
    pass

class socket(object):
    "socket(family=AF_INET, type=SOCK_STREAM, proto=0) -> socket object\nsocket(family=-1, type=-1, proto=-1, fileno=None) -> socket object\n\nOpen a socket of the given type.  The family argument specifies the\naddress family; it defaults to AF_INET.  The type argument specifies\nwhether this is a stream (SOCK_STREAM, this is the default)\nor datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,\nspecifying the default protocol.  Keyword arguments are accepted.\nThe socket is created as non-inheritable.\n\nWhen a fileno is passed in, family, type and proto are auto-detected,\nunless they are explicitly set.\n\nA socket object represents one endpoint of a network connection.\n\nMethods of socket objects (keyword arguments not allowed):\n\n_accept() -- accept connection, returning new socket fd and client address\nbind(addr) -- bind the socket to a local address\nclose() -- close the socket\nconnect(addr) -- connect the socket to a remote address\nconnect_ex(addr) -- connect, return an error code instead of an exception\ndup() -- return a new socket fd duplicated from fileno()\nfileno() -- return underlying file descriptor\ngetpeername() -- return remote address [*]\ngetsockname() -- return local address\ngetsockopt(level, optname[, buflen]) -- get socket options\ngettimeout() -- return timeout or None\nlisten([n]) -- start listening for incoming connections\nrecv(buflen[, flags]) -- receive data\nrecv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)\nrecvfrom(buflen[, flags]) -- receive data and sender's address\nrecvfrom_into(buffer[, nbytes, [, flags])\n  -- receive data and sender's address (into a buffer)\nsendall(data[, flags]) -- send all data\nsend(data[, flags]) -- send data, may not send all of it\nsendto(data[, flags], addr) -- send data to a given address\nsetblocking(0 | 1) -- set or clear the blocking I/O flag\ngetblocking() -- return True if socket is blocking, False if non-blocking\nsetsockopt(level, optname, value[, optlen]) -- set socket options\nsettimeout(None | float) -- set or clear the timeout\nshutdown(how) -- shut down traffic in one or both directions\nif_nameindex() -- return all network interface indices and names\nif_nametoindex(name) -- return the corresponding interface index\nif_indextoname(index) -- return the corresponding interface name\n\n [*] not available on all platforms!"
    __class__ = socket
    def __del__(self):
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        "socket(family=AF_INET, type=SOCK_STREAM, proto=0) -> socket object\nsocket(family=-1, type=-1, proto=-1, fileno=None) -> socket object\n\nOpen a socket of the given type.  The family argument specifies the\naddress family; it defaults to AF_INET.  The type argument specifies\nwhether this is a stream (SOCK_STREAM, this is the default)\nor datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,\nspecifying the default protocol.  Keyword arguments are accepted.\nThe socket is created as non-inheritable.\n\nWhen a fileno is passed in, family, type and proto are auto-detected,\nunless they are explicitly set.\n\nA socket object represents one endpoint of a network connection.\n\nMethods of socket objects (keyword arguments not allowed):\n\n_accept() -- accept connection, returning new socket fd and client address\nbind(addr) -- bind the socket to a local address\nclose() -- close the socket\nconnect(addr) -- connect the socket to a remote address\nconnect_ex(addr) -- connect, return an error code instead of an exception\ndup() -- return a new socket fd duplicated from fileno()\nfileno() -- return underlying file descriptor\ngetpeername() -- return remote address [*]\ngetsockname() -- return local address\ngetsockopt(level, optname[, buflen]) -- get socket options\ngettimeout() -- return timeout or None\nlisten([n]) -- start listening for incoming connections\nrecv(buflen[, flags]) -- receive data\nrecv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)\nrecvfrom(buflen[, flags]) -- receive data and sender's address\nrecvfrom_into(buffer[, nbytes, [, flags])\n  -- receive data and sender's address (into a buffer)\nsendall(data[, flags]) -- send all data\nsend(data[, flags]) -- send data, may not send all of it\nsendto(data[, flags], addr) -- send data to a given address\nsetblocking(0 | 1) -- set or clear the blocking I/O flag\ngetblocking() -- return True if socket is blocking, False if non-blocking\nsetsockopt(level, optname, value[, optlen]) -- set socket options\nsettimeout(None | float) -- set or clear the timeout\nshutdown(how) -- shut down traffic in one or both directions\nif_nameindex() -- return all network interface indices and names\nif_nametoindex(name) -- return the corresponding interface index\nif_indextoname(index) -- return the corresponding interface name\n\n [*] not available on all platforms!"
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
    
    def _accept(self):
        '_accept() -> (integer, address info)\n\nWait for an incoming connection.  Return a new socket file descriptor\nrepresenting the connection, and the address of the client.\nFor IP sockets, the address info is a pair (hostaddr, port).'
        return tuple()
    
    def bind(self, address):
        'bind(address)\n\nBind the socket to a local address.  For IP sockets, the address is a\npair (host, port); the host must refer to the local host. For raw packet\nsockets the address is a tuple (ifname, proto [,pkttype [,hatype [,addr]]])'
        pass
    
    def close(self):
        'close()\n\nClose the socket.  It cannot be used after this call.'
        pass
    
    def connect(self, address):
        'connect(address)\n\nConnect the socket to a remote address.  For IP sockets, the address\nis a pair (host, port).'
        pass
    
    def connect_ex(self, address):
        'connect_ex(address) -> errno\n\nThis is like connect(address), but returns an error code (the errno value)\ninstead of raising an exception when an error occurs.'
        pass
    
    def detach(self):
        'detach()\n\nClose the socket object without closing the underlying file descriptor.\nThe object cannot be used after this call, but the file descriptor\ncan be reused for other purposes.  The file descriptor is returned.'
        pass
    
    @property
    def family(self):
        'the socket family'
        pass
    
    def fileno(self):
        'fileno() -> integer\n\nReturn the integer file descriptor of the socket.'
        return 1
    
    def getblocking(self):
        'getblocking()\n\nReturns True if socket is in blocking mode, or False if it\nis in non-blocking mode.'
        pass
    
    def getpeername(self):
        'getpeername() -> address info\n\nReturn the address of the remote endpoint.  For IP sockets, the address\ninfo is a pair (hostaddr, port).'
        pass
    
    def getsockname(self):
        'getsockname() -> address info\n\nReturn the address of the local endpoint.  For IP sockets, the address\ninfo is a pair (hostaddr, port).'
        pass
    
    def getsockopt(self, level, option, buffersize=None):
        'getsockopt(level, option[, buffersize]) -> value\n\nGet a socket option.  See the Unix manual for level and option.\nIf a nonzero buffersize argument is given, the return value is a\nstring of that length; otherwise it is an integer.'
        pass
    
    def gettimeout(self):
        'gettimeout() -> timeout\n\nReturns the timeout in seconds (float) associated with socket \noperations. A timeout of None indicates that timeouts on socket \noperations are disabled.'
        pass
    
    def listen(self, backlog=None):
        'listen([backlog])\n\nEnable a server to accept connections.  If backlog is specified, it must be\nat least 0 (if it is lower, it is set to 0); it specifies the number of\nunaccepted connections that the system will allow before refusing new\nconnections. If not specified, a default reasonable value is chosen.'
        pass
    
    @property
    def proto(self):
        'the socket protocol'
        pass
    
    def recv(self, buffersize, flags=None):
        'recv(buffersize[, flags]) -> data\n\nReceive up to buffersize bytes from the socket.  For the optional flags\nargument, see the Unix manual.  When no data is available, block until\nat least one byte is available or until the remote end is closed.  When\nthe remote end is closed and all data is read, return the empty string.'
        pass
    
    def recv_into(self, buffer, nbytes=None, flags=None):
        'recv_into(buffer, [nbytes[, flags]]) -> nbytes_read\n\nA version of recv() that stores its data into a buffer rather than creating \na new string.  Receive up to buffersize bytes from the socket.  If buffersize \nis not specified (or 0), receive up to the size available in the given buffer.\n\nSee recv() for documentation about the flags.'
        pass
    
    def recvfrom(self, buffersize, flags=None):
        "recvfrom(buffersize[, flags]) -> (data, address info)\n\nLike recv(buffersize, flags) but also return the sender's address info."
        return tuple()
    
    def recvfrom_into(self, buffer, nbytes=None, flags=None):
        "recvfrom_into(buffer[, nbytes[, flags]]) -> (nbytes, address info)\n\nLike recv_into(buffer[, nbytes[, flags]]) but also return the sender's address info."
        return tuple()
    
    def recvmsg(self, bufsize, ancbufsize=None, flags=None):
        'recvmsg(bufsize[, ancbufsize[, flags]]) -> (data, ancdata, msg_flags, address)\n\nReceive normal data (up to bufsize bytes) and ancillary data from the\nsocket.  The ancbufsize argument sets the size in bytes of the\ninternal buffer used to receive the ancillary data; it defaults to 0,\nmeaning that no ancillary data will be received.  Appropriate buffer\nsizes for ancillary data can be calculated using CMSG_SPACE() or\nCMSG_LEN(), and items which do not fit into the buffer might be\ntruncated or discarded.  The flags argument defaults to 0 and has the\nsame meaning as for recv().\n\nThe return value is a 4-tuple: (data, ancdata, msg_flags, address).\nThe data item is a bytes object holding the non-ancillary data\nreceived.  The ancdata item is a list of zero or more tuples\n(cmsg_level, cmsg_type, cmsg_data) representing the ancillary data\n(control messages) received: cmsg_level and cmsg_type are integers\nspecifying the protocol level and protocol-specific type respectively,\nand cmsg_data is a bytes object holding the associated data.  The\nmsg_flags item is the bitwise OR of various flags indicating\nconditions on the received message; see your system documentation for\ndetails.  If the receiving socket is unconnected, address is the\naddress of the sending socket, if available; otherwise, its value is\nunspecified.\n\nIf recvmsg() raises an exception after the system call returns, it\nwill first attempt to close any file descriptors received via the\nSCM_RIGHTS mechanism.'
        return tuple()
    
    def recvmsg_into(self, buffers, ancbufsize=None, flags=None):
        'recvmsg_into(buffers[, ancbufsize[, flags]]) -> (nbytes, ancdata, msg_flags, address)\n\nReceive normal data and ancillary data from the socket, scattering the\nnon-ancillary data into a series of buffers.  The buffers argument\nmust be an iterable of objects that export writable buffers\n(e.g. bytearray objects); these will be filled with successive chunks\nof the non-ancillary data until it has all been written or there are\nno more buffers.  The ancbufsize argument sets the size in bytes of\nthe internal buffer used to receive the ancillary data; it defaults to\n0, meaning that no ancillary data will be received.  Appropriate\nbuffer sizes for ancillary data can be calculated using CMSG_SPACE()\nor CMSG_LEN(), and items which do not fit into the buffer might be\ntruncated or discarded.  The flags argument defaults to 0 and has the\nsame meaning as for recv().\n\nThe return value is a 4-tuple: (nbytes, ancdata, msg_flags, address).\nThe nbytes item is the total number of bytes of non-ancillary data\nwritten into the buffers.  The ancdata item is a list of zero or more\ntuples (cmsg_level, cmsg_type, cmsg_data) representing the ancillary\ndata (control messages) received: cmsg_level and cmsg_type are\nintegers specifying the protocol level and protocol-specific type\nrespectively, and cmsg_data is a bytes object holding the associated\ndata.  The msg_flags item is the bitwise OR of various flags\nindicating conditions on the received message; see your system\ndocumentation for details.  If the receiving socket is unconnected,\naddress is the address of the sending socket, if available; otherwise,\nits value is unspecified.\n\nIf recvmsg_into() raises an exception after the system call returns,\nit will first attempt to close any file descriptors received via the\nSCM_RIGHTS mechanism.'
        return tuple()
    
    def send(self, data, flags=None):
        'send(data[, flags]) -> count\n\nSend a data string to the socket.  For the optional flags\nargument, see the Unix manual.  Return the number of bytes\nsent; this may be less than len(data) if the network is busy.'
        pass
    
    def sendall(self, data, flags=None):
        "sendall(data[, flags])\n\nSend a data string to the socket.  For the optional flags\nargument, see the Unix manual.  This calls send() repeatedly\nuntil all data is sent.  If an error occurs, it's impossible\nto tell how much data has been sent."
        pass
    
    def sendmsg(self, buffers, ancdata=None, flags=None, address=None):
        'sendmsg(buffers[, ancdata[, flags[, address]]]) -> count\n\nSend normal and ancillary data to the socket, gathering the\nnon-ancillary data from a series of buffers and concatenating it into\na single message.  The buffers argument specifies the non-ancillary\ndata as an iterable of bytes-like objects (e.g. bytes objects).\nThe ancdata argument specifies the ancillary data (control messages)\nas an iterable of zero or more tuples (cmsg_level, cmsg_type,\ncmsg_data), where cmsg_level and cmsg_type are integers specifying the\nprotocol level and protocol-specific type respectively, and cmsg_data\nis a bytes-like object holding the associated data.  The flags\nargument defaults to 0 and has the same meaning as for send().  If\naddress is supplied and not None, it sets a destination address for\nthe message.  The return value is the number of bytes of non-ancillary\ndata sent.'
        pass
    
    def sendmsg_afalg(self, msg=None, *, op=None, iv=None, assoclen=None, flags=MSG_MORE):
        'sendmsg_afalg([msg], *, op[, iv[, assoclen[, flags=MSG_MORE]]])\n\nSet operation mode, IV and length of associated data for an AF_ALG\noperation socket.'
        pass
    
    def sendto(self, data, flags=None, address=None):
        'sendto(data[, flags], address) -> count\n\nLike send(data, flags) but allows specifying the destination address.\nFor IP sockets, the address is a pair (hostaddr, port).'
        pass
    
    def setblocking(self, flag):
        'setblocking(flag)\n\nSet the socket to blocking (flag is true) or non-blocking (false).\nsetblocking(True) is equivalent to settimeout(None);\nsetblocking(False) is equivalent to settimeout(0.0).'
        pass
    
    def setsockopt(self, level, option, None_, optlen: int):
        'setsockopt(level, option, value: int)\nsetsockopt(level, option, value: buffer)\nsetsockopt(level, option, None, optlen: int)\n\nSet a socket option.  See the Unix manual for level and option.\nThe value argument can either be an integer, a string buffer, or \nNone, optlen.'
        pass
    
    def settimeout(self, timeout):
        "settimeout(timeout)\n\nSet a timeout on socket operations.  'timeout' can be a float,\ngiving in seconds, or None.  Setting a timeout of None disables\nthe timeout feature and is equivalent to setblocking(1).\nSetting a timeout of zero is the same as setblocking(0)."
        pass
    
    def shutdown(self, flag):
        'shutdown(flag)\n\nShut down the reading side of the socket (flag == SHUT_RD), the writing side\nof the socket (flag == SHUT_WR), or both ends (flag == SHUT_RDWR).'
        pass
    
    @property
    def timeout(self):
        'the socket timeout'
        pass
    
    @property
    def type(self):
        'the socket type'
        pass
    

def socketpair(family=None, type=None, proto=None):
    'socketpair([family[, type [, proto]]]) -> (socket object, socket object)\n\nCreate a pair of socket objects from the sockets returned by the platform\nsocketpair() function.\nThe arguments are the same as for socket() except the default family is\nAF_UNIX if defined on the platform; otherwise, the default is AF_INET.'
    return tuple()

class timeout(OSError):
    __class__ = timeout
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

