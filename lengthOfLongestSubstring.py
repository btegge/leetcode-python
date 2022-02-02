def lengthOfLongestSubstring(s: str) -> int:
    length = 0
    candidate = ""
    candLen = 0
    for i, char in enumerate(s):
        if char not in candidate:
            candidate += char
            candLen += 1
        else:
            if candLen > length:
                length = candLen
            while char in candidate:
                candLen -= 1
                candidate = candidate[1:]
            candidate += char
            candLen += 1
    return candLen if candLen > length else length