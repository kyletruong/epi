# Take as input an array of digits representing a number like <1, 2, 9>
# Increment the number and represent that in the array like <1, 3, 0>

def incrementNumberArray(arr):
    # Add 1 to the last digit
    arr[-1] += 1

    # Carry the 1 if element is 10
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i-1] += 1

    # If list looks like '[10,...]' insert new element to make '[1,0,...]'
    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0, 1)

if __name__ == "__main__":
    arr = [1, 2, 9]
    incrementNumberArray(arr)
    print(arr)
