import random
my_str = (('凯尔特人', '雄鹿'), ('湖人', '骑士'))

number = [tuple(x) for x in my_str]
print(type(number))
print(number)
for i in number:
    print(type(tuple(i)))
    newStr = ' vs '.join(i)
    print(newStr)

#print('*'.join(tuple(my_str)))

my_DictStr = {'四': 1, '川': 2, ('a', 'b'): 3}
newDictStr = ''
for i in my_DictStr.keys():
    newDictStr = '*'.join(newDictStr + str(i))
    print(newDictStr)

lst1 = [1, 2, 3, 999999999999, 'a', 'b']
lst2 = [1, 2, 3, 999999999999, 'a', 'c']
print(lst1 == lst2)
print(id(lst1) == id(lst2))
print(lst1[0] == lst2[0])
print(id(lst1[0]) == id(lst2[0]))
print(id(lst1[3]) == id(lst2[3]))
print(id(lst1[4]) == id(lst2[4]))
print(id(lst1[5]) == id(lst2[5]))

myInt1 = 99999999
myInt2 = 99999999
print(id(myInt1) == id(myInt2))
print(myInt1 is myInt2)

myStr1 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
myStr2 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print(id(myStr1) == id(myStr2))

myFloat1 = 10.1
myFloat2 = 10.1
print(myFloat1 is myFloat2)

lst3 = [1, 2, 3, 999999999999, 'a', 'b', 2, '3', 2, '3']
lst4 = [1, 2, 3, 999999999999, 'a', 'c']
print(lst4)
del lst4[0]
print(lst4)
print(lst4.pop(0))
print(lst4)
print(lst3)
for num in lst3:
    if num == 2:
        lst3.remove(num)
print(lst3)
for num in lst3[:]:
    if num == 2:
        lst3.remove(num)
print(lst3)
# for num in len(lst3)-1:
#     if num == 2:
#         lst3.remove(num)
# print(lst3)
lst6 = [random.randint(10, 100) for i in range(10)]
print(lst6)













