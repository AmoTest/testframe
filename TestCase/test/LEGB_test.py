
#str = 'global test'

def outer():
    #str = "Enclose test"

    def inner():
        #str = "local test"

        print(str)

    inner()
outer()