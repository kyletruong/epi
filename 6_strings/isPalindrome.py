def isPalindrome(s):
    # ~i = -i - 1
    # So s[0] = s[-1]
    return all(s[i] is s[~i] for i in range(len(s) // 2))

def isPalindromeTwo(s):
    return s == s[::-1]

if __name__ == "__main__":
    if isPalindrome('racecar'):
        print('yay')
    else:
        print('nay')

    A = [0,1,2,3,4,5]
    print(A[5:0:-1])