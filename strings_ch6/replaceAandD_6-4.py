# Write a program that replaces each 'a' by two 'd's
# Delete each entry containing 'b'
# <a,c,d,b,b,c,a> => <d,d,c,d,c,d,d>
# Assume array is large enough and don't worry about preserving subsequent entries

# Being cheeky and incorporating type annotations for fun
from typing import List

# When deleting a character do A[write_index] to keep track of where you are
# When reinserting 'dd' go backwards
def replace_and_remove(A: List[chr], size: int):
    a_count, write_index = 0, 0
    for i in range(size):
        if A[i] == 'a':
            a_count += 1
        elif A[i] == 'b':
            continue
        A[write_index] = A[i]
        write_index += 1

    # write_index is 1 past correct position after first forward iteration
    cur_index = write_index - 1
    write_index = cur_index + a_count
    while cur_index >= 0:
        if A[cur_index] == 'a':
            A[write_index-1:write_index+1] = 'dd'
            write_index -= 2
        else:
            A[write_index] = A[cur_index]
            write_index -= 1
        cur_index -= 1
        
    
if __name__ == "__main__":
    A = ['a','b','a','c','']
    size = 4
    replace_and_remove(A, size)
    print(A)