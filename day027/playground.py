# *args: Many positional arguments
def add(*args):
    # add_num = 0
    # for i in args:
    #     add_num += i
    # return add_num
    return sum(args)

print(add(1, 2, 3))

# **kwargs: Many keyword arguments

def calculate(n, **kwargs):
    # print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

