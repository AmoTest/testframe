
aSet = {2, 3, 4, 5, 2, 7, 8}
bSet = {'a'}
print(type(aSet))
print(aSet)
print(len(aSet))
print(aSet.pop())
print(aSet.pop())
print(aSet)
aSet.remove(5)
print(aSet)
aSet.update(bSet)
print(aSet)
for k, v in enumerate(aSet):
    print(k)
    print(v)

aDic = {"Hello": "World", 1 : 2}
print(type(aDic))
print(aDic)