
import sys
from collections import Iterable

num = 0

class ClassTest:

    def __init__(self, words):
        self.words = words
        print("This is init()")

    # def __str__(self):
    #     return "hello, This is str()"

    def __repr__(self):
        return "hello, This is repr()"
    # def __getitem__(self, position):  # 支持索引取值
    #     return self.words[position]

    def __iter__(self):
        return self

    def __next__(self):
        global num
        if num == 0:
            num += 1
            return self.words
        else:
            raise StopIteration

classTest = ClassTest([1, 2, 3])
print(classTest)
print(__name__)
print(sys.__name__)
print(isinstance(classTest, Iterable))
# c = classTest.__iter__()
for i in classTest:
    print(f"This is ClassTest{classTest.__next__()}")