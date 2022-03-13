import time

def deco(func):
    start_time = time.time()
    f()
    end_time = time.time()
    execution_time = (end_time - start_time)*1000
    print("time is %d ms" %execution_time)

def f():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':

    deco(f)
    print("f.__name__ is",f.__name__)
    print()