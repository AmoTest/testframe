gen1 = [x for x in range(100)]
gen2 = [x for x in range(2, 100, 2)]
gen3 = [x for x in range(2, 100) if x % 2 == 0]
gen4 = [x + y for x in '123' for y in 'abc']
gen5 = (x for x in range(100))
print(gen1)
print(gen2)
print(gen3)
print(gen4)
print(next(gen5))
print(next(gen5))
for i in [x for x in range(100)]:
    print(i, end=' ')

print(type(gen4))
print(type(gen5))

my_dict = {'a': 10, 'b': 34, 'c': 27}
my_dict1 = {z: j for j, z in my_dict.items()}  # 全部对调
my_dict2 = {z: j for j, z in my_dict.items() if j == "a"}  # 加上判断条件
print("type(my_dict1)", type(my_dict1))
print("my_dict1", my_dict1)
print("my_dict2", my_dict2)

my_dict3 = {z: j for j, z in my_dict.items()}

print(type(my_dict1))

my_set = {x for x in range(100)}
print(type(my_set))