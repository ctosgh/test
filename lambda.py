import os

def myfunc(n):
    return lambda a : a * n

if __name__ == "__main__":
    mytriple = myfunc(3)
    print(mytriple(11))
