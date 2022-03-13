

gcount = 0

def global_test():
    global gcount
    gcount += 10
    print(gcount)

global_test()

def make_counter():
    count = 1

    def counter():
        nonlocal count
        count +=5

        return count
    return counter

def make_counter_test():
    mc = make_counter()

    print(mc())

make_counter_test()

import time

def deco(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco
def f():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':
    f()
    print("f.__name__ is", f.__name__)