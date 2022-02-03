from math import log10, floor


def alternate(x: int) -> int:
    sign = 1 if x >= 0 else -1
    x *= sign
    rev = 0
    min_int_32 = 2 ** 31
    while x > 0:
        rev = rev * 10 + x % 10
        if rev * sign <= -min_int_32 or rev * sign >= min_int_32 - 1:
            return 0
        x //= 10
    return sign * rev


def reverse(vers: int, x: int) -> int:
    if vers == 0:
        if x == 0:
            return x
        sign = 1 if x >= 0 else -1
        intBack = 0
        x *= sign
        place = 1
        power = 10 ** floor(log10(x))
        while x > 0:
            digit = x // power
            x -= digit * power
            intBack += place * digit
            place *= 10
            power //= 10
        intBack *= sign
        if intBack < -2**31 or intBack > (2**31 - 1):
            intBack = 0
        return intBack
    else:
        return alternate(x)