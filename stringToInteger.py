def myAtoi(s: str) -> int:
    int_min_32 = 2 ** 31
    s = s.strip()
    i = 0
    c = ""
    sign = 1
    if i < len(s):
        c = s[i]
        if c == '-' or c == '+':
            sign = -1 if c == '-' else 1
            i += 1
    val = 0
    while i < len(s):
        c = s[i]
        if not c.isdigit():
            return sign * val
        val = val * 10 + (ord(c) - ord('0'))
        if val * sign < -int_min_32:
            return -int_min_32
        if val * sign > int_min_32 - 1:
            return int_min_32 - 1
        i += 1
    return sign * val