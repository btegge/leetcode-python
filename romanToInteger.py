def romanToInt(s: str) -> int:
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    pre = 0
    total = 0
    for i in s:
        val = d[i]
        if val > pre:
            total = total + val - pre - pre
        else:
            total = total + val
        pre = val
    return total
