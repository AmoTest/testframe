
# 《西游记》

def funcOut(func):
     def funcIn():
         return "《{0}》".format(func())
     return funcIn

@funcOut
def bookName():
    return '西游记'


print(bookName())