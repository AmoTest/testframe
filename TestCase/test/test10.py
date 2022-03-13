
my_EngStr = 'Hello World'
my_ChnStr = '人生苦短 用Python'

print(my_EngStr.encode('utf-8'))
print(len(my_EngStr.encode('utf-8')))

print(my_EngStr.encode('gbk'))
print(len(my_EngStr.encode('gbk')))

print(my_ChnStr.encode('utf-8'))
print(len(my_ChnStr.encode('utf-8')))

print(my_ChnStr.encode('gbk'))
print(len(my_ChnStr.encode('gbk').decode('gbk')))

print(my_ChnStr.encode('utf-8').decode('utf-8'))
print(len(my_ChnStr.encode('utf-8')))

print(my_ChnStr.encode('gbk').decode('gbk'))
print(len(my_ChnStr.encode('gbk').decode('gbk')))