# Test whether a string is a palindrome but ignore all nonalphanumeric chars

def isPalindrome(s):
    i, j = 0, len(s) - 1
    
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1

        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        # elif s[i] == s[j]
        i, j = i + 1, j -1

    return True

if __name__ == "__main__":
    s = 'A man, a plan, a canal, Panama.'
    print(isPalindrome(s))