# Given an Array A of n elements and a permutation P, apply P to A
# <2, 0, 1, 3> move index 0 to 2; 1 to 0; etc.
# <a, b, c, d> => <b, c, a, d>

# O(n) space
def brute_applyPermutation(perm, A):
    newArray = [None] * len(A)
    for i in range(len(A)):
        newArray[perm[i]] = A[i]

    return newArray

# O(1) space
def applyPermutation(perm, A):
    for i, c in enumerate(perm):
        next = i
        while c >= 0:
            A[i], A[c] = A[c], A[i]
            perm[next] -= len(perm)
            next = c
            c = perm[c]

    # Restore perm
    perm[:] = [x + len(perm) for x in perm]

    # list[:] is slice assignment
    # slice assignment changes current contents of the list
    # perm = [list_comprehension] would simply change the reference to new list
    # Then when func ends and new list goes out of scope, new list obj is gone
    # Then perm reference goes back to its previous reference


def main():
    perm = [3, 2, 1, 0, 5, 4]
    A = ['a', 'b', 'c', 'd', 'e', 'f']
    applyPermutation(perm, A)
    print(A)
    
if __name__ == "__main__":
    main()