def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    returnStr = ""
    for i in range(1, numRows + 1):
        curpos = i - 1
        if curpos < len(s):
            returnStr += s[curpos]
            item = 1
        while curpos < len(s):
            item += 1
            prepos = curpos
            curpos = (curpos + (numRows * 2) - (2 * i)) if item % 2 == 0 else (curpos + (i * 2) - 2)
            if curpos != prepos and curpos < len(s):
                returnStr += s[curpos]
    return returnStr
