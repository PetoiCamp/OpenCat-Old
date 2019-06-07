BasicContext = Context()
class Clamped(DecimalException):
    __class__ = Clamped
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Context(object):
    'The context affects almost all operations and controls rounding,\nOver/Underflow, raising of exceptions and much more.  A new context\ncan be constructed as follows:\n\n    >>> c = Context(prec=28, Emin=-425000000, Emax=425000000,\n    ...             rounding=ROUND_HALF_EVEN, capitals=1, clamp=1,\n    ...             traps=[InvalidOperation, DivisionByZero, Overflow],\n    ...             flags=[])\n    >>>\n\n\n'
    @property
    def Emax(self):
        pass
    
    @property
    def Emin(self):
        pass
    
    def Etiny(self):
        'Return a value equal to Emin - prec + 1, which is the minimum exponent value\nfor subnormal results.  When underflow occurs, the exponent is set to Etiny.\n\n'
        pass
    
    def Etop(self):
        'Return a value equal to Emax - prec + 1.  This is the maximum exponent\nif the _clamp field of the context is set to 1 (IEEE clamp mode).  Etop()\nmust not be negative.\n\n'
        pass
    
    __class__ = Context
    def __copy__(self):
        pass
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        'The context affects almost all operations and controls rounding,\nOver/Underflow, raising of exceptions and much more.  A new context\ncan be constructed as follows:\n\n    >>> c = Context(prec=28, Emin=-425000000, Emax=425000000,\n    ...             rounding=ROUND_HALF_EVEN, capitals=1, clamp=1,\n    ...             traps=[InvalidOperation, DivisionByZero, Overflow],\n    ...             flags=[])\n    >>>\n\n\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply(self):
        pass
    
    def abs(self, x):
        'Return the absolute value of x.\n\n'
        pass
    
    def add(self, x, y):
        'Return the sum of x and y.\n\n'
        pass
    
    def canonical(self, x):
        'Return a new instance of x.\n\n'
        pass
    
    @property
    def capitals(self):
        pass
    
    @property
    def clamp(self):
        pass
    
    def clear_flags(self):
        'Reset all flags to False.\n\n'
        pass
    
    def clear_traps(self):
        'Set all traps to False.\n\n'
        pass
    
    def compare(self, x, y):
        'Compare x and y numerically.\n\n'
        pass
    
    def compare_signal(self, x, y):
        'Compare x and y numerically.  All NaNs signal.\n\n'
        pass
    
    def compare_total(self, x, y):
        'Compare x and y using their abstract representation.\n\n'
        pass
    
    def compare_total_mag(self, x, y):
        'Compare x and y using their abstract representation, ignoring sign.\n\n'
        pass
    
    def copy(self):
        'Return a duplicate of the context with all flags cleared.\n\n'
        pass
    
    def copy_abs(self, x):
        'Return a copy of x with the sign set to 0.\n\n'
        pass
    
    def copy_decimal(self, x):
        'Return a copy of Decimal x.\n\n'
        pass
    
    def copy_negate(self, x):
        'Return a copy of x with the sign inverted.\n\n'
        pass
    
    def copy_sign(self, x, y):
        'Copy the sign from y to x.\n\n'
        pass
    
    def create_decimal(self, num):
        'Create a new Decimal instance from num, using self as the context. Unlike the\nDecimal constructor, this function observes the context limits.\n\n'
        pass
    
    def create_decimal_from_float(self, f):
        'Create a new Decimal instance from float f.  Unlike the Decimal.from_float()\nclass method, this function observes the context limits.\n\n'
        pass
    
    def divide(self, x, y):
        'Return x divided by y.\n\n'
        pass
    
    def divide_int(self, x, y):
        'Return x divided by y, truncated to an integer.\n\n'
        pass
    
    def divmod(self, x, y):
        'Return quotient and remainder of the division x / y.\n\n'
        pass
    
    def exp(self, x):
        'Return e ** x.\n\n'
        pass
    
    def fma(self, x, y, z):
        'Return x multiplied by y, plus z.\n\n'
        pass
    
    def is_canonical(self, x):
        'Return True if x is canonical, False otherwise.\n\n'
        pass
    
    def is_finite(self, x):
        'Return True if x is finite, False otherwise.\n\n'
        pass
    
    def is_infinite(self, x):
        'Return True if x is infinite, False otherwise.\n\n'
        pass
    
    def is_nan(self, x):
        'Return True if x is a qNaN or sNaN, False otherwise.\n\n'
        pass
    
    def is_normal(self, x):
        'Return True if x is a normal number, False otherwise.\n\n'
        pass
    
    def is_qnan(self, x):
        'Return True if x is a quiet NaN, False otherwise.\n\n'
        pass
    
    def is_signed(self, x):
        'Return True if x is negative, False otherwise.\n\n'
        pass
    
    def is_snan(self, x):
        'Return True if x is a signaling NaN, False otherwise.\n\n'
        pass
    
    def is_subnormal(self, x):
        'Return True if x is subnormal, False otherwise.\n\n'
        pass
    
    def is_zero(self, x):
        'Return True if x is a zero, False otherwise.\n\n'
        pass
    
    def ln(self, x):
        'Return the natural (base e) logarithm of x.\n\n'
        pass
    
    def log10(self, x):
        'Return the base 10 logarithm of x.\n\n'
        pass
    
    def logb(self, x):
        "Return the exponent of the magnitude of the operand's MSD.\n\n"
        pass
    
    def logical_and(self, x, y):
        'Digit-wise and of x and y.\n\n'
        pass
    
    def logical_invert(self, x):
        'Invert all digits of x.\n\n'
        pass
    
    def logical_or(self, x, y):
        'Digit-wise or of x and y.\n\n'
        pass
    
    def logical_xor(self, x, y):
        'Digit-wise xor of x and y.\n\n'
        pass
    
    def max(self, x, y):
        'Compare the values numerically and return the maximum.\n\n'
        pass
    
    def max_mag(self, x, y):
        'Compare the values numerically with their sign ignored.\n\n'
        pass
    
    def min(self, x, y):
        'Compare the values numerically and return the minimum.\n\n'
        pass
    
    def min_mag(self, x, y):
        'Compare the values numerically with their sign ignored.\n\n'
        pass
    
    def minus(self, x):
        'Minus corresponds to the unary prefix minus operator in Python, but applies\nthe context to the result.\n\n'
        pass
    
    def multiply(self, x, y):
        'Return the product of x and y.\n\n'
        pass
    
    def next_minus(self, x):
        'Return the largest representable number smaller than x.\n\n'
        pass
    
    def next_plus(self, x):
        'Return the smallest representable number larger than x.\n\n'
        pass
    
    def next_toward(self, x, y):
        'Return the number closest to x, in the direction towards y.\n\n'
        pass
    
    def normalize(self, x):
        'Reduce x to its simplest form. Alias for reduce(x).\n\n'
        pass
    
    def number_class(self, x):
        'Return an indication of the class of x.\n\n'
        pass
    
    def plus(self, x):
        'Plus corresponds to the unary prefix plus operator in Python, but applies\nthe context to the result.\n\n'
        pass
    
    def power(self, a, b, modulo):
        "Compute a**b. If 'a' is negative, then 'b' must be integral. The result\nwill be inexact unless 'a' is integral and the result is finite and can\nbe expressed exactly in 'precision' digits.  In the Python version the\nresult is always correctly rounded, in the C version the result is almost\nalways correctly rounded.\n\nIf modulo is given, compute (a**b) % modulo. The following restrictions\nhold:\n\n    * all three arguments must be integral\n    * 'b' must be nonnegative\n    * at least one of 'a' or 'b' must be nonzero\n    * modulo must be nonzero and less than 10**prec in absolute value\n\n\n"
        pass
    
    @property
    def prec(self):
        pass
    
    def quantize(self, x, y):
        'Return a value equal to x (rounded), having the exponent of y.\n\n'
        pass
    
    def radix(self):
        'Return 10.\n\n'
        pass
    
    def remainder(self, x, y):
        'Return the remainder from integer division.  The sign of the result,\nif non-zero, is the same as that of the original dividend.\n\n'
        pass
    
    def remainder_near(self, x, y):
        'Return x - y * n, where n is the integer nearest the exact value of x / y\n(if the result is 0 then its sign will be the sign of x).\n\n'
        pass
    
    def rotate(self, x, y):
        'Return a copy of x, rotated by y places.\n\n'
        pass
    
    @property
    def rounding(self):
        pass
    
    def same_quantum(self, x, y):
        'Return True if the two operands have the same exponent.\n\n'
        pass
    
    def scaleb(self, x, y):
        'Return the first operand after adding the second value to its exp.\n\n'
        pass
    
    def shift(self, x, y):
        'Return a copy of x, shifted by y places.\n\n'
        pass
    
    def sqrt(self, x):
        'Square root of a non-negative number to context precision.\n\n'
        pass
    
    def subtract(self, x, y):
        'Return the difference between x and y.\n\n'
        pass
    
    def to_eng_string(self, x):
        'Convert a number to a string, using engineering notation.\n\n'
        pass
    
    def to_integral(self, x):
        'Identical to to_integral_value(x).\n\n'
        pass
    
    def to_integral_exact(self, x):
        'Round to an integer. Signal if the result is rounded or inexact.\n\n'
        pass
    
    def to_integral_value(self, x):
        'Round to an integer.\n\n'
        pass
    
    def to_sci_string(self, x):
        'Convert a number to a string using scientific notation.\n\n'
        pass
    

class ConversionSyntax(InvalidOperation):
    __class__ = ConversionSyntax
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Decimal(object):
    "Construct a new Decimal object. 'value' can be an integer, string, tuple,\nor another Decimal object. If no value is given, return Decimal('0'). The\ncontext does not affect the conversion and is only passed to determine if\nthe InvalidOperation trap is active.\n\n"
    def __abs__(self):
        'abs(self)'
        return Decimal()
    
    def __add__(self, value):
        'Return self+value.'
        return Decimal()
    
    def __bool__(self):
        'self != 0'
        return False
    
    def __ceil__(self):
        return Decimal()
    
    __class__ = Decimal
    def __complex__(self):
        pass
    
    def __copy__(self):
        pass
    
    def __deepcopy__(self):
        pass
    
    def __divmod__(self, value):
        'Return divmod(self, value).'
        return (0, 0)
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __floor__(self):
        return Decimal()
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
    def __format__(self, format_spec):
        return ''
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        "Construct a new Decimal object. 'value' can be an integer, string, tuple,\nor another Decimal object. If no value is given, return Decimal('0'). The\ncontext does not affect the conversion and is only passed to determine if\nthe InvalidOperation trap is active.\n\n"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mod__(self, value):
        'Return self%value.'
        return Decimal()
    
    __module__ = 'decimal'
    def __mul__(self, value):
        'Return self*value.'
        return Decimal()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return Decimal()
    
    def __pos__(self):
        '+self'
        return Decimal()
    
    def __pow__(self, value, mod):
        'Return pow(self, value, mod).'
        return Decimal()
    
    def __radd__(self, value):
        'Return value+self.'
        return Decimal()
    
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        return (0, 0)
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return Decimal()
    
    def __rmod__(self, value):
        'Return value%self.'
        return Decimal()
    
    def __rmul__(self, value):
        'Return value*self.'
        return Decimal()
    
    def __round__(self, ndigits=0):
        return Decimal()
    
    def __rpow__(self, value, mod):
        'Return pow(value, self, mod).'
        return Decimal()
    
    def __rsub__(self, value):
        'Return value-self.'
        return Decimal()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Decimal()
    
    def __sizeof__(self):
        return 0
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return Decimal()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def __trunc__(self):
        return Decimal()
    
    def adjusted(self):
        'Return the adjusted exponent of the number.  Defined as exp + digits - 1.\n\n'
        pass
    
    def as_integer_ratio(self):
        'Decimal.as_integer_ratio() -> (int, int)\n\nReturn a pair of integers, whose ratio is exactly equal to the original\nDecimal and with a positive denominator. The ratio is in lowest terms.\nRaise OverflowError on infinities and a ValueError on NaNs.\n\n'
        return tuple()
    
    def as_tuple(self):
        'Return a tuple representation of the number.\n\n'
        pass
    
    def canonical(self):
        'Return the canonical encoding of the argument.  Currently, the encoding\nof a Decimal instance is always canonical, so this operation returns its\nargument unchanged.\n\n'
        pass
    
    def compare(self, other, context):
        "Compare self to other.  Return a decimal value:\n\n    a or b is a NaN ==> Decimal('NaN')\n    a < b           ==> Decimal('-1')\n    a == b          ==> Decimal('0')\n    a > b           ==> Decimal('1')\n\n"
        pass
    
    def compare_signal(self, other, context):
        'Identical to compare, except that all NaNs signal.\n\n'
        pass
    
    def compare_total(self, other, context):
        "Compare two operands using their abstract representation rather than\ntheir numerical value.  Similar to the compare() method, but the result\ngives a total ordering on Decimal instances.  Two Decimal instances with\nthe same numeric value but different representations compare unequal\nin this ordering:\n\n    >>> Decimal('12.0').compare_total(Decimal('12'))\n    Decimal('-1')\n\nQuiet and signaling NaNs are also included in the total ordering. The result\nof this function is Decimal('0') if both operands have the same representation,\nDecimal('-1') if the first operand is lower in the total order than the second,\nand Decimal('1') if the first operand is higher in the total order than the\nsecond operand. See the specification for details of the total order.\n\nThis operation is unaffected by context and is quiet: no flags are changed\nand no rounding is performed. As an exception, the C version may raise\nInvalidOperation if the second operand cannot be converted exactly.\n\n"
        pass
    
    def compare_total_mag(self, other, context):
        'Compare two operands using their abstract representation rather than their\nvalue as in compare_total(), but ignoring the sign of each operand.\n\nx.compare_total_mag(y) is equivalent to x.copy_abs().compare_total(y.copy_abs()).\n\nThis operation is unaffected by context and is quiet: no flags are changed\nand no rounding is performed. As an exception, the C version may raise\nInvalidOperation if the second operand cannot be converted exactly.\n\n'
        pass
    
    def conjugate(self):
        'Return self.\n\n'
        pass
    
    def copy_abs(self):
        'Return the absolute value of the argument.  This operation is unaffected by\ncontext and is quiet: no flags are changed and no rounding is performed.\n\n'
        pass
    
    def copy_negate(self):
        'Return the negation of the argument.  This operation is unaffected by context\nand is quiet: no flags are changed and no rounding is performed.\n\n'
        pass
    
    def copy_sign(self, other, context):
        "Return a copy of the first operand with the sign set to be the same as the\nsign of the second operand. For example:\n\n    >>> Decimal('2.3').copy_sign(Decimal('-1.5'))\n    Decimal('-2.3')\n\nThis operation is unaffected by context and is quiet: no flags are changed\nand no rounding is performed. As an exception, the C version may raise\nInvalidOperation if the second operand cannot be converted exactly.\n\n"
        pass
    
    def exp(self, context):
        'Return the value of the (natural) exponential function e**x at the given\nnumber.  The function always uses the ROUND_HALF_EVEN mode and the result\nis correctly rounded.\n\n'
        pass
    
    def fma(self, other, third, context):
        "Fused multiply-add.  Return self*other+third with no rounding of the\nintermediate product self*other.\n\n    >>> Decimal(2).fma(3, 5)\n    Decimal('11')\n\n\n"
        pass
    
    @classmethod
    def from_float(cls, type, f):
        "Class method that converts a float to a decimal number, exactly.\nSince 0.1 is not exactly representable in binary floating point,\nDecimal.from_float(0.1) is not the same as Decimal('0.1').\n\n    >>> Decimal.from_float(0.1)\n    Decimal('0.1000000000000000055511151231257827021181583404541015625')\n    >>> Decimal.from_float(float('nan'))\n    Decimal('NaN')\n    >>> Decimal.from_float(float('inf'))\n    Decimal('Infinity')\n    >>> Decimal.from_float(float('-inf'))\n    Decimal('-Infinity')\n\n\n"
        pass
    
    @property
    def imag(self):
        pass
    
    def is_canonical(self):
        'Return True if the argument is canonical and False otherwise.  Currently,\na Decimal instance is always canonical, so this operation always returns\nTrue.\n\n'
        pass
    
    def is_finite(self):
        'Return True if the argument is a finite number, and False if the argument\nis infinite or a NaN.\n\n'
        pass
    
    def is_infinite(self):
        'Return True if the argument is either positive or negative infinity and\nFalse otherwise.\n\n'
        pass
    
    def is_nan(self):
        'Return True if the argument is a (quiet or signaling) NaN and False\notherwise.\n\n'
        pass
    
    def is_normal(self, context):
        'Return True if the argument is a normal finite non-zero number with an\nadjusted exponent greater than or equal to Emin. Return False if the\nargument is zero, subnormal, infinite or a NaN.\n\n'
        pass
    
    def is_qnan(self):
        'Return True if the argument is a quiet NaN, and False otherwise.\n\n'
        pass
    
    def is_signed(self):
        'Return True if the argument has a negative sign and False otherwise.\nNote that both zeros and NaNs can carry signs.\n\n'
        pass
    
    def is_snan(self):
        'Return True if the argument is a signaling NaN and False otherwise.\n\n'
        pass
    
    def is_subnormal(self, context):
        'Return True if the argument is subnormal, and False otherwise. A number is\nsubnormal if it is non-zero, finite, and has an adjusted exponent less\nthan Emin.\n\n'
        pass
    
    def is_zero(self):
        'Return True if the argument is a (positive or negative) zero and False\notherwise.\n\n'
        pass
    
    def ln(self, context):
        'Return the natural (base e) logarithm of the operand. The function always\nuses the ROUND_HALF_EVEN mode and the result is correctly rounded.\n\n'
        pass
    
    def log10(self, context):
        'Return the base ten logarithm of the operand. The function always uses the\nROUND_HALF_EVEN mode and the result is correctly rounded.\n\n'
        pass
    
    def logb(self, context):
        "For a non-zero number, return the adjusted exponent of the operand as a\nDecimal instance.  If the operand is a zero, then Decimal('-Infinity') is\nreturned and the DivisionByZero condition is raised. If the operand is\nan infinity then Decimal('Infinity') is returned.\n\n"
        pass
    
    def logical_and(self, other, context):
        "Return the digit-wise 'and' of the two (logical) operands.\n\n"
        pass
    
    def logical_invert(self, context):
        'Return the digit-wise inversion of the (logical) operand.\n\n'
        pass
    
    def logical_or(self, other, context):
        "Return the digit-wise 'or' of the two (logical) operands.\n\n"
        pass
    
    def logical_xor(self, other, context):
        "Return the digit-wise 'exclusive or' of the two (logical) operands.\n\n"
        pass
    
    def max(self, other, context):
        'Maximum of self and other.  If one operand is a quiet NaN and the other is\nnumeric, the numeric operand is returned.\n\n'
        pass
    
    def max_mag(self, other, context):
        'Similar to the max() method, but the comparison is done using the absolute\nvalues of the operands.\n\n'
        pass
    
    def min(self, other, context):
        'Minimum of self and other. If one operand is a quiet NaN and the other is\nnumeric, the numeric operand is returned.\n\n'
        pass
    
    def min_mag(self, other, context):
        'Similar to the min() method, but the comparison is done using the absolute\nvalues of the operands.\n\n'
        pass
    
    def next_minus(self, context):
        'Return the largest number representable in the given context (or in the\ncurrent default context if no context is given) that is smaller than the\ngiven operand.\n\n'
        pass
    
    def next_plus(self, context):
        'Return the smallest number representable in the given context (or in the\ncurrent default context if no context is given) that is larger than the\ngiven operand.\n\n'
        pass
    
    def next_toward(self, other, context):
        'If the two operands are unequal, return the number closest to the first\noperand in the direction of the second operand.  If both operands are\nnumerically equal, return a copy of the first operand with the sign set\nto be the same as the sign of the second operand.\n\n'
        pass
    
    def normalize(self, context):
        "Normalize the number by stripping the rightmost trailing zeros and\nconverting any result equal to Decimal('0') to Decimal('0e0').  Used\nfor producing canonical values for members of an equivalence class.\nFor example, Decimal('32.100') and Decimal('0.321000e+2') both normalize\nto the equivalent value Decimal('32.1').\n\n"
        pass
    
    def number_class(self, context):
        "Return a string describing the class of the operand.  The returned value\nis one of the following ten strings:\n\n    * '-Infinity', indicating that the operand is negative infinity.\n    * '-Normal', indicating that the operand is a negative normal number.\n    * '-Subnormal', indicating that the operand is negative and subnormal.\n    * '-Zero', indicating that the operand is a negative zero.\n    * '+Zero', indicating that the operand is a positive zero.\n    * '+Subnormal', indicating that the operand is positive and subnormal.\n    * '+Normal', indicating that the operand is a positive normal number.\n    * '+Infinity', indicating that the operand is positive infinity.\n    * 'NaN', indicating that the operand is a quiet NaN (Not a Number).\n    * 'sNaN', indicating that the operand is a signaling NaN.\n\n\n"
        pass
    
    def quantize(self, exp, rounding, context):
        "Return a value equal to the first operand after rounding and having the\nexponent of the second operand.\n\n    >>> Decimal('1.41421356').quantize(Decimal('1.000'))\n    Decimal('1.414')\n\nUnlike other operations, if the length of the coefficient after the quantize\noperation would be greater than precision, then an InvalidOperation is signaled.\nThis guarantees that, unless there is an error condition, the quantized exponent\nis always equal to that of the right-hand operand.\n\nAlso unlike other operations, quantize never signals Underflow, even if the\nresult is subnormal and inexact.\n\nIf the exponent of the second operand is larger than that of the first, then\nrounding may be necessary. In this case, the rounding mode is determined by the\nrounding argument if given, else by the given context argument; if neither\nargument is given, the rounding mode of the current thread's context is used.\n\n"
        pass
    
    def radix(self):
        'Return Decimal(10), the radix (base) in which the Decimal class does\nall its arithmetic. Included for compatibility with the specification.\n\n'
        pass
    
    @property
    def real(self):
        pass
    
    def remainder_near(self, other, context):
        'Return the remainder from dividing self by other.  This differs from\nself % other in that the sign of the remainder is chosen so as to minimize\nits absolute value. More precisely, the return value is self - n * other\nwhere n is the integer nearest to the exact value of self / other, and\nif two integers are equally near then the even one is chosen.\n\nIf the result is zero then its sign will be the sign of self.\n\n'
        pass
    
    def rotate(self, other, context):
        'Return the result of rotating the digits of the first operand by an amount\nspecified by the second operand.  The second operand must be an integer in\nthe range -precision through precision. The absolute value of the second\noperand gives the number of places to rotate. If the second operand is\npositive then rotation is to the left; otherwise rotation is to the right.\nThe coefficient of the first operand is padded on the left with zeros to\nlength precision if necessary. The sign and exponent of the first operand are\nunchanged.\n\n'
        pass
    
    def same_quantum(self, other, context):
        'Test whether self and other have the same exponent or whether both are NaN.\n\nThis operation is unaffected by context and is quiet: no flags are changed\nand no rounding is performed. As an exception, the C version may raise\nInvalidOperation if the second operand cannot be converted exactly.\n\n'
        pass
    
    def scaleb(self, other, context):
        'Return the first operand with the exponent adjusted the second.  Equivalently,\nreturn the first operand multiplied by 10**other. The second operand must be\nan integer.\n\n'
        pass
    
    def shift(self, other, context):
        'Return the result of shifting the digits of the first operand by an amount\nspecified by the second operand.  The second operand must be an integer in\nthe range -precision through precision. The absolute value of the second\noperand gives the number of places to shift. If the second operand is\npositive, then the shift is to the left; otherwise the shift is to the\nright. Digits shifted into the coefficient are zeros. The sign and exponent\nof the first operand are unchanged.\n\n'
        pass
    
    def sqrt(self, context):
        'Return the square root of the argument to full precision. The result is\ncorrectly rounded using the ROUND_HALF_EVEN rounding mode.\n\n'
        pass
    
    def to_eng_string(self, context):
        "Convert to an engineering-type string.  Engineering notation has an exponent\nwhich is a multiple of 3, so there are up to 3 digits left of the decimal\nplace. For example, Decimal('123E+1') is converted to Decimal('1.23E+3').\n\nThe value of context.capitals determines whether the exponent sign is lower\nor upper case. Otherwise, the context does not affect the operation.\n\n"
        pass
    
    def to_integral(self, rounding, context):
        'Identical to the to_integral_value() method.  The to_integral() name has been\nkept for compatibility with older versions.\n\n'
        pass
    
    def to_integral_exact(self, rounding, context):
        'Round to the nearest integer, signaling Inexact or Rounded as appropriate if\nrounding occurs.  The rounding mode is determined by the rounding parameter\nif given, else by the given context. If neither parameter is given, then the\nrounding mode of the current default context is used.\n\n'
        pass
    
    def to_integral_value(self, rounding, context):
        'Round to the nearest integer without signaling Inexact or Rounded.  The\nrounding mode is determined by the rounding parameter if given, else by\nthe given context. If neither parameter is given, then the rounding mode\nof the current default context is used.\n\n'
        pass
    

class DecimalException(ArithmeticError):
    __class__ = DecimalException
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class DecimalTuple(tuple):
    'DecimalTuple(sign, digits, exponent)'
    __class__ = DecimalTuple
    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return ()
    
    def __init__(self, sign, digits, exponent):
        'DecimalTuple(sign, digits, exponent)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    def __repr__(self):
        'Return a nicely formatted representation string'
        return ''
    
    __slots__ = tuple()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        pass
    
    _fields = tuple()
    _fields_defaults = dict()
    def _make(self, cls, iterable):
        'Make a new DecimalTuple object from a sequence or iterable'
        pass
    
    def _replace(self, _self, **kwds):
        'Return a new DecimalTuple object replacing specified fields with new values'
        pass
    
    digits = property()
    exponent = property()
    sign = property()

DefaultContext = Context()
class DivisionByZero(DecimalException,ZeroDivisionError):
    __class__ = DivisionByZero
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DivisionImpossible(InvalidOperation):
    __class__ = DivisionImpossible
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DivisionUndefined(InvalidOperation,ZeroDivisionError):
    __class__ = DivisionUndefined
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

ExtendedContext = Context()
class FloatOperation(DecimalException,TypeError):
    __class__ = FloatOperation
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

HAVE_THREADS = True
class Inexact(DecimalException):
    __class__ = Inexact
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class InvalidContext(InvalidOperation):
    __class__ = InvalidContext
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class InvalidOperation(DecimalException):
    __class__ = InvalidOperation
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

MAX_EMAX = 999999999999999999
MAX_PREC = 999999999999999999
MIN_EMIN = -999999999999999999
MIN_ETINY = -1999999999999999997
class Overflow(Inexact,Rounded):
    __class__ = Overflow
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

ROUND_05UP = 'ROUND_05UP'
ROUND_CEILING = 'ROUND_CEILING'
ROUND_DOWN = 'ROUND_DOWN'
ROUND_FLOOR = 'ROUND_FLOOR'
ROUND_HALF_DOWN = 'ROUND_HALF_DOWN'
ROUND_HALF_EVEN = 'ROUND_HALF_EVEN'
ROUND_HALF_UP = 'ROUND_HALF_UP'
ROUND_UP = 'ROUND_UP'
class Rounded(DecimalException):
    __class__ = Rounded
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Subnormal(DecimalException):
    __class__ = Subnormal
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Underflow(Inexact,Rounded,Subnormal):
    __class__ = Underflow
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'decimal'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__doc__ = 'C decimal arithmetic module'
__file__ = '/usr/lib/python3.7/lib-dynload/_decimal.cpython-37m-x86_64-linux-gnu.so'
__libmpdec_version__ = '2.4.2'
__name__ = 'decimal'
__package__ = ''
__version__ = '1.70'
def getcontext():
    'Get the current default context.\n\n'
    pass

def localcontext(ctx):
    'Return a context manager that will set the default context to a copy of ctx\non entry to the with-statement and restore the previous default context when\nexiting the with-statement. If no context is specified, a copy of the current\ndefault context is used.\n\n'
    pass

def setcontext(context):
    'Set a new default context.\n\n'
    pass

