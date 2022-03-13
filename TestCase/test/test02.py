
# 《西游记》

def funcOut(func):
     def funcIn():
         print("《{0}》".format(func()))
     return funcIn

def bookName():
    return '西游记'

bookName = funcOut(bookName)
bookName()