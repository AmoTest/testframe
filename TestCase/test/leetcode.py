

lst1 = [3, 8, 3]  # 383
lst2 = [6, 2, 3]  # 326
a, b = 26%11, 26//11
print(a)
print(b)

def sumList(num1: list, num2: list) -> list:

    str1 = ''
    str2 = ''
    lst3 = []

    for i in range(len(num1)-1, -1, -1):
        str1 = str1 + str(num1[i])

    for i in range(len(num2)-1, -1, -1):
        str2 = str2 + str(num2[i])


    int3 = int(str1) + int(str2)
    str3 = str(int3)

    for i in range(len(str3)-1, -1, -1):
        lst3.append(str3[i])

    print(lst3)
    return lst3

sumList(lst1, lst2)


