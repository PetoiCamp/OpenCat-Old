import builtins as _mod_builtins

__doc__ = 'Functional tools for creating and using iterators.\n\nInfinite iterators:\ncount(start=0, step=1) --> start, start+step, start+2*step, ...\ncycle(p) --> p0, p1, ... plast, p0, p1, ...\nrepeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times\n\nIterators terminating on the shortest input sequence:\naccumulate(p[, func]) --> p0, p0+p1, p0+p1+p2\nchain(p, q, ...) --> p0, p1, ... plast, q0, q1, ... \nchain.from_iterable([p, q, ...]) --> p0, p1, ... plast, q0, q1, ... \ncompress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...\ndropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails\ngroupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)\nfilterfalse(pred, seq) --> elements of seq where pred(elem) is False\nislice(seq, [start,] stop [, step]) --> elements from\n       seq[start:stop:step]\nstarmap(fun, seq) --> fun(*seq[0]), fun(*seq[1]), ...\ntee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n\ntakewhile(pred, seq) --> seq[0], seq[1], until pred fails\nzip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ... \n\nCombinatoric generators:\nproduct(p, q, ... [repeat=1]) --> cartesian product\npermutations(p[, r])\ncombinations(p, r)\ncombinations_with_replacement(p, r)\n'
__name__ = 'itertools'
__package__ = ''
class _grouper(_mod_builtins.object):
    __class__ = _grouper
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _grouper()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _tee(_mod_builtins.object):
    'Iterator wrapped to make it copyable'
    __class__ = _tee
    def __copy__(self):
        'Returns an independent iterator.'
        pass
    
    def __init__(self, *args, **kwargs):
        'Iterator wrapped to make it copyable'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _tee()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _tee_dataobject(_mod_builtins.object):
    'Data container common to multiple tee objects.'
    __class__ = _tee_dataobject
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        'Data container common to multiple tee objects.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class accumulate(_mod_builtins.object):
    'accumulate(iterable[, func]) --> accumulate object\n\nReturn series of accumulated sums (or other binary function results).'
    __class__ = accumulate
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, iterable, func=None):
        'accumulate(iterable[, func]) --> accumulate object\n\nReturn series of accumulated sums (or other binary function results).'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return accumulate()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class chain(_mod_builtins.object):
    'chain(*iterables) --> chain object\n\nReturn a chain object whose .__next__() method returns elements from the\nfirst iterable until it is exhausted, then elements from the next\niterable, until all of the iterables are exhausted.'
    __class__ = chain
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *iterables):
        'chain(*iterables) --> chain object\n\nReturn a chain object whose .__next__() method returns elements from the\nfirst iterable until it is exhausted, then elements from the next\niterable, until all of the iterables are exhausted.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return chain()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def from_iterable(cls):
        'chain.from_iterable(iterable) --> chain object\n\nAlternate chain() constructor taking a single iterable argument\nthat evaluates lazily.'
        pass
    

class combinations(_mod_builtins.object):
    'combinations(iterable, r) --> combinations object\n\nReturn successive r-length combinations of elements in the iterable.\n\ncombinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)'
    __class__ = combinations
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, iterable, r):
        'combinations(iterable, r) --> combinations object\n\nReturn successive r-length combinations of elements in the iterable.\n\ncombinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return combinations()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    def __sizeof__(self):
        'Returns size in memory, in bytes.'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class combinations_with_replacement(_mod_builtins.object):
    "combinations_with_replacement(iterable, r) --> combinations_with_replacement object\n\nReturn successive r-length combinations of elements in the iterable\nallowing individual elements to have successive repeats.\ncombinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC"
    __class__ = combinations_with_replacement
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, iterable, r):
        "combinations_with_replacement(iterable, r) --> combinations_with_replacement object\n\nReturn successive r-length combinations of elements in the iterable\nallowing individual elements to have successive repeats.\ncombinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return combinations_with_replacement()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    def __sizeof__(self):
        'Returns size in memory, in bytes.'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class compress(_mod_builtins.object):
    'compress(data, selectors) --> iterator over selected data\n\nReturn data elements corresponding to true selector elements.\nForms a shorter iterator from selected data elements using the\nselectors to choose the data elements.'
    __class__ = compress
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, data, selectors):
        'compress(data, selectors) --> iterator over selected data\n\nReturn data elements corresponding to true selector elements.\nForms a shorter iterator from selected data elements using the\nselectors to choose the data elements.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return compress()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class count(_mod_builtins.object):
    'count(start=0, step=1) --> count object\n\nReturn a count object whose .__next__() method returns consecutive values.\nEquivalent to:\n\n    def count(firstval=0, step=1):\n        x = firstval\n        while 1:\n            yield x\n            x += step\n'
    __class__ = count
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, start=0, step=1):
        'count(start=0, step=1) --> count object\n\nReturn a count object whose .__next__() method returns consecutive values.\nEquivalent to:\n\n    def count(firstval=0, step=1):\n        x = firstval\n        while 1:\n            yield x\n            x += step\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return count()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class cycle(_mod_builtins.object):
    'cycle(iterable) --> cycle object\n\nReturn elements from the iterable until it is exhausted.\nThen repeat the sequence indefinitely.'
    __class__ = cycle
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, iterable):
        'cycle(iterable) --> cycle object\n\nReturn elements from the iterable until it is exhausted.\nThen repeat the sequence indefinitely.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return cycle()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class dropwhile(_mod_builtins.object):
    'dropwhile(predicate, iterable) --> dropwhile object\n\nDrop items from the iterable while predicate(item) is true.\nAfterwards, return every element until the iterable is exhausted.'
    __class__ = dropwhile
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, predicate, iterable):
        'dropwhile(predicate, iterable) --> dropwhile object\n\nDrop items from the iterable while predicate(item) is true.\nAfterwards, return every element until the iterable is exhausted.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return dropwhile()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class filterfalse(_mod_builtins.object):
    'filterfalse(function or None, sequence) --> filterfalse object\n\nReturn those items of sequence for which function(item) is false.\nIf function is None, return the items that are false.'
    __class__ = filterfalse
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, functionorNone, sequence):
        'filterfalse(function or None, sequence) --> filterfalse object\n\nReturn those items of sequence for which function(item) is false.\nIf function is None, return the items that are false.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return filterfalse()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class groupby(_mod_builtins.object):
    'groupby(iterable, key=None) -> make an iterator that returns consecutive\nkeys and groups from the iterable.  If the key function is not specified or\nis None, the element itself is used for grouping.\n'
    __class__ = groupby
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, iterable, key=None):
        'groupby(iterable, key=None) -> make an iterator that returns consecutive\nkeys and groups from the iterable.  If the key function is not specified or\nis None, the element itself is used for grouping.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return groupby()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class islice(_mod_builtins.object):
    'islice(iterable, stop) --> islice object\nislice(iterable, start, stop[, step]) --> islice object\n\nReturn an iterator whose next() method returns selected values from an\niterable.  If start is specified, will skip all preceding elements;\notherwise, start defaults to zero.  Step defaults to one.  If\nspecified as another value, step determines how many values are \nskipped between successive calls.  Works like a slice() on a list\nbut returns an iterator.'
    __class__ = islice
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, iterable, start, stop, step=None):
        'islice(iterable, stop) --> islice object\nislice(iterable, start, stop[, step]) --> islice object\n\nReturn an iterator whose next() method returns selected values from an\niterable.  If start is specified, will skip all preceding elements;\notherwise, start defaults to zero.  Step defaults to one.  If\nspecified as another value, step determines how many values are \nskipped between successive calls.  Works like a slice() on a list\nbut returns an iterator.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return islice()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class permutations(_mod_builtins.object):
    'permutations(iterable[, r]) --> permutations object\n\nReturn successive r-length permutations of elements in the iterable.\n\npermutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)'
    __class__ = permutations
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, iterable, r=None):
        'permutations(iterable[, r]) --> permutations object\n\nReturn successive r-length permutations of elements in the iterable.\n\npermutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return permutations()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    def __sizeof__(self):
        'Returns size in memory, in bytes.'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class product(_mod_builtins.object):
    "product(*iterables, repeat=1) --> product object\n\nCartesian product of input iterables.  Equivalent to nested for-loops.\n\nFor example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).\nThe leftmost iterators are in the outermost for-loop, so the output tuples\ncycle in a manner similar to an odometer (with the rightmost element changing\non every iteration).\n\nTo compute the product of an iterable with itself, specify the number\nof repetitions with the optional repeat keyword argument. For example,\nproduct(A, repeat=4) means the same as product(A, A, A, A).\n\nproduct('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)\nproduct((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ..."
    __class__ = product
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *iterables, repeat=1):
        "product(*iterables, repeat=1) --> product object\n\nCartesian product of input iterables.  Equivalent to nested for-loops.\n\nFor example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).\nThe leftmost iterators are in the outermost for-loop, so the output tuples\ncycle in a manner similar to an odometer (with the rightmost element changing\non every iteration).\n\nTo compute the product of an iterable with itself, specify the number\nof repetitions with the optional repeat keyword argument. For example,\nproduct(A, repeat=4) means the same as product(A, A, A, A).\n\nproduct('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)\nproduct((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ..."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return product()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    def __sizeof__(self):
        'Returns size in memory, in bytes.'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class repeat(_mod_builtins.object):
    'repeat(object [,times]) -> create an iterator which returns the object\nfor the specified number of times.  If not specified, returns the object\nendlessly.'
    __class__ = repeat
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, object, times=None):
        'repeat(object [,times]) -> create an iterator which returns the object\nfor the specified number of times.  If not specified, returns the object\nendlessly.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return repeat()
    
    def __length_hint__(self):
        'Private method returning an estimate of len(list(it)).'
        return 0
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class starmap(_mod_builtins.object):
    'starmap(function, sequence) --> starmap object\n\nReturn an iterator whose values are returned from the function evaluated\nwith an argument tuple taken from the given sequence.'
    __class__ = starmap
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, function, sequence):
        'starmap(function, sequence) --> starmap object\n\nReturn an iterator whose values are returned from the function evaluated\nwith an argument tuple taken from the given sequence.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return starmap()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class takewhile(_mod_builtins.object):
    'takewhile(predicate, iterable) --> takewhile object\n\nReturn successive entries from an iterable as long as the \npredicate evaluates to true for each entry.'
    __class__ = takewhile
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, predicate, iterable):
        'takewhile(predicate, iterable) --> takewhile object\n\nReturn successive entries from an iterable as long as the \npredicate evaluates to true for each entry.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return takewhile()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def tee(iterable, n=2):
    'tee(iterable, n=2) --> tuple of n independent iterators.'
    pass

class zip_longest(_mod_builtins.object):
    'zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object\n\nReturn a zip_longest object whose .__next__() method returns a tuple where\nthe i-th element comes from the i-th iterable argument.  The .__next__()\nmethod continues until the longest iterable in the argument sequence\nis exhausted and then it raises StopIteration.  When the shorter iterables\nare exhausted, the fillvalue is substituted in their place.  The fillvalue\ndefaults to None or can be specified by a keyword argument.\n'
    __class__ = zip_longest
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        'zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object\n\nReturn a zip_longest object whose .__next__() method returns a tuple where\nthe i-th element comes from the i-th iterable argument.  The .__next__()\nmethod continues until the longest iterable in the argument sequence\nis exhausted and then it raises StopIteration.  When the shorter iterables\nare exhausted, the fillvalue is substituted in their place.  The fillvalue\ndefaults to None or can be specified by a keyword argument.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return zip_longest()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    def __reduce__(self):
        'Return state information for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Set state information for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

