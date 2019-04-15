# Given a pathname return the shortest equivalent path
# Absolute path: /usr/lib/../bin/gcc == /usr/bin/gcc
# Relative path: scripts//./../scripts/awkscripts/././ == scripts/awkscripts

def shortest_path(s):
    stack, tokens = [], s.split('/')
    if s[0] == '/':
        stack.append('/')

    for token in tokens:
        # Empty and '.' means cur directory, so skip that token
        if token and token != '.':
            if token == '..' and stack:
                stack.pop()
            else:
                stack.append(token)

    start = 1 if stack[0] == '/' else 0
    return '/'.join(stack)[start:]

if __name__ == '__main__':
    s = '/usr/lib/../bin/gcc'
    t = 'scripts//./../scripts/awkscripts/././'
    u = 'sc//./../tc/awk/././'
    paths = [s, t, u]
    for path in paths:
        print(path + '  ->  ' + shortest_path(path))
