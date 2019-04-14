# Test a string of brackets (){}[] for well-formedness
# Well-formedness means same order opening and closed brackets
# ([]){()} = good,  {) = bad

def well_formed(s):
    stack, lookup = [], {')': '(', '}': '{', ']': '['}
    for c in s:
        # Only need to check if closing bracket matches top of stack
        if stack and c in lookup:
            if lookup[c] == stack[-1]:
                stack.pop()
                continue
        # Append if not a matching closing bracket
        stack.append(c)

    return not stack

if __name__ == '__main__':
    # True
    r = '([]){()}'
    s = '(()[])'
    # False
    t = '[()[]{()()'
    u = '(()][)'
    
    if well_formed(r) and well_formed(s):
        print('r and s True')
    if not well_formed(t) and not well_formed(u):
        print('t and u False')
