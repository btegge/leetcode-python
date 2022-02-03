def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s
    match = bool(s) and p[0] in {s[0], '.'}
    if len(p) >= 2 and p[1] == '*':
        return isMatch(s, p[2:]) or match and isMatch(s[1:], p)
    else:
        return match and isMatch(s[1:], p[1:])