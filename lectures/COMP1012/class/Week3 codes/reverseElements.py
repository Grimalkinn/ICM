aList = ['hi', 12, -2.5, True, 42]
idx = 0
last = len(aList) - 1
print("Original:", aList)
while idx < len(aList)//2:
    aList[idx], aList[last-idx] = \
         aList[last-idx] , aList[idx]
    idx += 1
print("Reversed:", aList)


