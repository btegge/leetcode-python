def alternate(s: str) -> str:
    longest = ""

    def expand(s: str, i: int, longest: str) -> str:
        L = i
        R = i
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if len(s[L:R + 1]) > len(longest):
                longest = s[L:R + 1]
            L -= 1
            R += 1
        L = i
        R = i + 1
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if len(s[L:R + 1]) > len(longest):
                longest = s[L:R + 1]
            L -= 1
            R += 1
        return longest

    for i in range(len(s)):
        longest = expand(s, i, longest)
    return longest


def longestPalindrome(vers: int, s: str) -> str:
    if vers == 0:
        def isPalindrome(s: str) -> bool:
            first = 0
            last = len(s) - 1
            while last > first:
                if s[first] != s[last]:
                    return False
                first += 1
                last -= 1
            return True

        size = len(s)
        while size > 0:
            for start in range(0, len(s) - size + 1):
                end = start + size
                candidate = s[start:end]
                if isPalindrome(candidate):
                    return candidate
            size -= 1
    else:
        return alternate(s)
