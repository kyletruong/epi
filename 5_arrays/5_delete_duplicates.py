# Delete duplicates in a sorted array

def deleteDups(sortedArray):
    writeIndex = 1
    for i in range(1, len(sortedArray)):
        if sortedArray[writeIndex-1] != sortedArray[i]:
            sortedArray[writeIndex] = sortedArray[i]
            writeIndex += 1
    return writeIndex

if __name__ == "__main__":
    myList = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    print(deleteDups(myList))