

def funcOut(func):
    def funcIn(x, y):
        func(x, y)
    return funcIn

@funcOut
def bookName(a, b):
    print('西游记' + a + b)

bookName('后', '传')


def funcOut(func):
    def funcIn(x, y):
        func(x, y)
    return funcIn

def bookName(a, b):
    print('西游记' + a + b)

bookName = funcOut(bookName)
bookName('前', '传')