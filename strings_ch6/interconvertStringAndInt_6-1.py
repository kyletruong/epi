# Interconvert strings to integers and vice versa

def intToString(x):
    isNegative = False
    if x < 0:
        x, isNegative = -x, True
    
    s = []
    while x > 0:
        s.append(chr(ord('0') + (x % 10)))
        x //= 10
    
    return ('-' if isNegative else '') + (''.join(reversed(s)))
    
def stringToInt(s):
    isNegative, start = False, 0
    if s[0] == '-':
        isNegative = True
        start = 1

    num = 0
    for c in s[start:]:
        num = num * 10 + ord(c) - ord('0')

    return -num if isNegative else num
    
if __name__ == "__main__":
    intNumber, strNumber = -12345, '-12345'
    print(intToString(intNumber))
    print(stringToInt(strNumber))