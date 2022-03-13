
aList = [1,2,3, 4, 5, 6, 7, 9, 8, 7, 10, 2]
bList = ['www', 'pythontab.com']
print(len(aList))
# aList[len(aList):len(aList)] = bList
print(aList)

print(aList[0:-1])
print(len(aList))
print(aList[:len(aList)-1])
print(aList[::-1])
print(aList[0:2])
cList = aList + bList
print(cList)
print(cList*2)
if 2 in cList:
    print(True)
print(200 in cList)
print(sum(aList))
print(min(aList))
print(max(aList))
print(aList)
aList.append(11)
print(aList)
aList.insert(2, 12)
print(aList)
aList.extend(bList)
print(aList)
aList.remove(11)
print(aList)
print(aList.index(12))
print(aList.count(7))
aList.pop()
print(aList)
aList.reverse()
print(aList)
aList.
