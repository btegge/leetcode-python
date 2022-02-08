def intToRoman(num: int) -> str:
    d = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    res = ""

    for k, v in reversed(d.items()):
        while num - v >= 0:
            num -= v
            res += k

    return res
