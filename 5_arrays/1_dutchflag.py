import random

# Partition an array so that all elements <= k1 are in first partition
# elements > k1 && <= k2 in middle partition
# elements > k2 in third partition

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partitionArray(array, k1, k2):
    curr, low, high = 0, 0, len(array)-1

    while curr <= high:
        if array[curr] <= k1:
            swap(array, curr, low)
            low += 1
        elif array[curr] > k2:
            swap(array, curr, high)
            high -= 1
            continue
        curr += 1

if __name__ == "__main__":
    myList = []
    low, high = 33, 66
    for i in range(20):
        myList.append(random.randint(0, 100))

    print(f'low = {low}, high = {high}')
    print(myList)
    partitionArray(myList, low, high)
    print(myList)
