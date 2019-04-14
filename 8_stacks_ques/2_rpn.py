# Make an rpn calculator that takes comma separated string
# 1,2,+ = 3 or 1,2,3 = 123

def eval(rpn):
    symbols, stack = rpn.split(','), []
    for s in symbols:
        if s in '+-/*':
            if len(stack) >= 2:
                x = int(stack[-2])
                y = int(stack[-1])
            else:
                raise ValueError('malformed RPN at: ' + s)

        if s == '+':
            stack.pop()
            stack[-1] = x + y
        elif s == '-':
            stack.pop()
            stack[-1] = x - y
        elif s == '/':
            stack.pop()
            stack[-1] = x / y
        elif s == '*':
            stack.pop()
            stack[-1] = x * y
        else:
            stack.append(s)
    
    # If multiple numbers are inputted and no operator, just retrieve last number
    # This is how calculators work anyways
    return stack[-1]

if __name__ == '__main__':
    a = '3,4,+,2,*,1,+'
    b = '2,3,/'
    c = '+,1'
    print(eval(a))
    print(eval(b))

    # Raise exception
    try:
        print(eval(c))
    except ValueError:
        print("Malformed RPN: '" + c + "'")
