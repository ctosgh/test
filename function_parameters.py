import os



def func1(*args):
    for arg in args:
        print(arg)


def func2(arg1, *args):
    print("frist arg is {}".format(arg1))
    print("extra args type is {} and value is {}".format(type(args), args))


def func3(**kwargs):
    print("type of **kwargs is {} and value is {} ".format(type(kwargs), kwargs))


if __name__ == "__main__":
    func1("a", "b", "c")
    func1("a")
    func2(1,2,3,4,5)
    func3(first="aaaa", second=45, third="hello, world")

    args = ("what", "the", "fuck", 36)
    func1(*args)

    kwargs = {"arg1":"waht", "arg2":"the", "arg3":"fuck", "arg4":34}
    func3(**kwargs)

